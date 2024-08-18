import matplotlib.pyplot as plt
import numpy as np
import pickle
import base64
import os
import io

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

def __plot_eeg(eeg: list[float]):
    _, ax = plt.subplots(figsize=(10, 6))
    ax.plot(eeg)
    ax.set_xlabel("Tempo (10⁻²s)")
    ax.set_ylabel("Amplitude (µV)")
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    img = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()
    return img

def __plot_classified_eeg(stages: list[int]):
    _, ax = plt.subplots(figsize=(10, 6))
    ax.step(range(len(stages)), stages, where="post")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Estágio do Sono")
    plt.yticks([0, 1, 2, 3, 4], ["Acordado", "N1", "N2", "N3", "REM"])
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    img = base64.b64encode(buffer.getvalue()).decode("utf-8")
    buffer.close()
    return img

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
            "eeg_reading_plot": __plot_eeg(job["eeg_reading"]),
            "classified_eeg_reading_plot": __plot_classified_eeg(stages),
            "sleep_stages_distribution_plot": "sleep_stages_distribution_plot_data"
        }

        print(f"JOB: {job_id} DONE")