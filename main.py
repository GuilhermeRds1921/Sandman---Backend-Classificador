from flask import Flask, request, jsonify
from classifier import process_job
from pdf import generate_pdf
import threading
import uuid

app = Flask(__name__)
jobs = {}

@app.route("/classifier/exam", methods=["POST"])
def send_exam():
    data: dict = request.get_json()
    eeg_reading = data.get("eeg_reading")
    job_id = str(uuid.uuid4())

    job = {
        "eeg_reading": eeg_reading,
        "classified": False,
        "stage_table": None,
        "classified_eeg_reading": None,
        "plots": {
            "eeg_reading_plot": None,
            "classified_eeg_reading_plot": None,
            "sleep_stages_distribution_plot": None
        }
    }
    jobs[job_id] = job
    threading.Thread(target=process_job, args=(job_id, jobs)).start()
    return jsonify({"job_id": job_id})

@app.route("/classifier/exam/<job_id>", methods=["GET"])
def get_exam(job_id):
    job = jobs.get(job_id)
    
    if not job:
        return jsonify({"error": "Job not found"}), 404
    
    return jsonify({
        "done": job["classified"],
        "stage_table": job["stage_table"],
        "classified_eeg_reading": job["classified_eeg_reading"],
        "eeg_reading_plot": job["plots"]["eeg_reading_plot"],
        "classified_eeg_reading_plot": job["plots"]["classified_eeg_reading_plot"],
        "sleep_stages_distribution_plot": job["plots"]["sleep_stages_distribution_plot"]
    })

@app.route("/classifier/generate_report", methods=["POST"])
def generate_report():
    data: dict = request.get_json()
    job_id = data.get("job_id")
    notes = data.get("notes")
    name = data.get("name")
    technician = data.get("technician")
    CDEnf = data.get("CDEnf")
    
    job = jobs.get(job_id)
    
    if not job: return jsonify({"error": "Job not found"}), 404
    if not job["classified"]: return jsonify({"error": "Classification not completed"}), 404
    
    return jsonify({"report_pdf": generate_pdf(job, notes, name, technician, CDEnf)})

if __name__ == "__main__":
    app.run(debug=True)