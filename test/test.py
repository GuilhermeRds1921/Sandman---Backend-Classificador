import requests
import random
import time
import json
import os

BASE_URL = "http://127.0.0.1:5000/classifier"

def list_similarity(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length.")
    matches = sum(1 for x, y in zip(list1, list2) if x == y)

    similarity_percentage = (matches / len(list1)) * 100
    return similarity_percentage

def submit_exam(eeg_reading):
    url = f"{BASE_URL}/exam"
    response = requests.post(url, json={"eeg_reading": eeg_reading})
    response_data = response.json()
    return response_data["job_id"]

def check_exam(job_id):
    url = f"{BASE_URL}/exam/{job_id}"
    response = requests.get(url)
    response_data = response.json()
    if response_data["classified"]:
        return {
            "classified_eeg_reading": response_data["classified_eeg_reading"],
            "eeg_reading_plot": response_data["eeg_reading_plot"],
            "classified_eeg_reading_plot": response_data["classified_eeg_reading_plot"],
            "sleep_stages_distribution_plot": response_data["sleep_stages_distribution_plot"]
        }
    else:
        return None

if __name__ == "__main__":
    dataset_path = [
        (os.path.join(".", "test", "awake.json"), 0, 100000),
        (os.path.join(".", "test", "n1.json"), 1, 100000),
        (os.path.join(".", "test", "n2.json"), 2, 100000),
        (os.path.join(".", "test", "n3.json"), 3, 100000),
        (os.path.join(".", "test", "rem.json"), 4, 100000)
    ]

    X = []
    y = []
    for path in dataset_path:
        with open(path[0], "r") as file:
            windows = json.load(file)
            stages = random.choices(windows, k=path[2])
            y.extend([path[1]] * len(stages))

            for w in stages:
                X.extend(w)

    print(len(X), len(y))

    job_id = submit_exam(X)
    print(f"Exam submitted. Job ID: {job_id}")

    while True:
        result = check_exam(job_id)
        if result:
            print("Classification completed!")
            print(f"Similarity: {list_similarity(y, result['classified_eeg_reading']):.3f}%")
            break
        else:
            print("Classification not yet completed. Retrying...")
            time.sleep(30)