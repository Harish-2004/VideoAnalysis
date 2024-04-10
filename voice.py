import librosa
import numpy as np

def compute_voice(audio):
    y, sr = librosa.load(audio)

    frame_length = 2048
    hop_length = 512
    energy = librosa.feature.rms(y=y, frame_length=frame_length, hop_length=hop_length)[0]

    mean_energy = np.mean(energy)
    std_energy = np.std(energy)

    soft_threshold = mean_energy - 0.5 * std_energy
    medium_threshold = mean_energy + 0.5 * std_energy

    soft_duration = 0
    medium_duration = 0
    high_duration = 0

    for e in energy:
        if e < soft_threshold:
            soft_duration += hop_length / sr
        elif soft_threshold <= e < medium_threshold:
            medium_duration += hop_length / sr
        else:
            high_duration += hop_length / sr

    total_duration = librosa.get_duration(y=y, sr=sr)

    percentage_soft = (soft_duration / total_duration) * 100
    percentage_medium = (medium_duration / total_duration) * 100
    percentage_high = (high_duration / total_duration) * 100

    voice_duration = (soft_duration,medium_duration,high_duration)
    voice_percentage = (percentage_soft,percentage_medium,percentage_high)

    return voice_duration,voice_percentage