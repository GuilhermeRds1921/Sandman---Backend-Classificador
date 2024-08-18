import numpy as np
import pickle
import os

HZ = 100
MODEL = pickle.load(open(os.path.join(".", "classifier", "knn_model.pkl"), "rb"))

def __extract_features(window: np.ndarray):
    fft_vals = np.fft.fft(window)
    power_spectrum = np.abs(fft_vals)**2
    freqs = np.fft.fftfreq(len(window), d=1/100)

    mean_freq = np.sum(freqs * power_spectrum) / np.sum(power_spectrum)
    peak_freq = freqs[np.argmax(power_spectrum)]
    min_freq = freqs[np.argmin(power_spectrum)]
    freq_difference = peak_freq - min_freq

    return [mean_freq, peak_freq, min_freq, freq_difference]

def __pre_process_signal(eeg: list[float]):
    features = []
    aux_signal = np.array(eeg)
    aux_signal = aux_signal.reshape(aux_signal.shape[0] // 100, 100) 

    for window in aux_signal:
        features.append(__extract_features(window))

    return np.array(features)

def process_job(job_id, jobs: dict):
    job = jobs.get(job_id)
    if job:
        windows = __pre_process_signal(job["eeg_reading"])
        stages = []
        for w in windows:
            X = np.array(w).reshape(1, -1)
            stages.extend([int(MODEL.predict(X)[0])])

        job["classified"] = True
        job["classified_eeg_reading"] = stages
        job["plots"] = {
            "eeg_reading_plot": "eeg_reading_plot_data",
            "classified_eeg_reading_plot": "classified_eeg_reading_plot_data",
            "sleep_stages_distribution_plot": "sleep_stages_distribution_plot_data"
        }

        print(f"JOB: {job_id} DONE")