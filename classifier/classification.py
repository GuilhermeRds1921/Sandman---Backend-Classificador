import time

def process_job(job_id, jobs: dict):
    time.sleep(5)  # Simula a execução do job com um atraso de 5 segundos
    
    job = jobs.get(job_id)
    if job:
        job["classified"] = True
        job["classified_eeg_reading"] = "Classified EEG Reading Data"
        job["plots"] = {
            "eeg_reading_plot": "eeg_reading_plot_data",
            "classified_eeg_reading_plot": "classified_eeg_reading_plot_data",
            "sleep_stages_distribution_plot": "sleep_stages_distribution_plot_data"
        }