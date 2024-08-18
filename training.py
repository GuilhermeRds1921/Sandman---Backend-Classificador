from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pickle
import json
import os

def __extract_features(window: np.ndarray):
    fft_vals = np.fft.fft(window)
    power_spectrum = np.abs(fft_vals)**2
    freqs = np.fft.fftfreq(len(window), d=1/100)

    mean_freq = np.sum(freqs * power_spectrum) / np.sum(power_spectrum)
    peak_freq = freqs[np.argmax(power_spectrum)]
    min_freq = freqs[np.argmin(power_spectrum)]
    freq_difference = peak_freq - min_freq

    return [mean_freq, peak_freq, min_freq, freq_difference]

if __name__ == "__main__":
    dataset_path = [
        (os.path.join(".", "test", "awake.json"), 0),
        (os.path.join(".", "test", "n1.json"), 1),
        (os.path.join(".", "test", "n2.json"), 2),
        (os.path.join(".", "test", "n3.json"), 3),
        (os.path.join(".", "test", "rem.json"), 4)
    ]

    X = []
    y = []
    for path in dataset_path:
        with open(path[0], "r") as file:
            windows = json.load(file)
            y.extend([path[1]] * len(windows))
            for w in windows:
                X.append(__extract_features(np.array(w)))
    
    X_train, X_test, y_train, y_test = train_test_split(X, y,
        stratify=y, test_size=0.7, random_state=42
    )

    classifier = KNeighborsClassifier(n_neighbors=5, weights="distance")
    classifier.fit(X, y)
    pickle.dump(classifier, open(os.path.join(".", "classifier", "knn_model.pkl"), "wb"))
