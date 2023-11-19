import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 44100  # This is the sample rate for aux in
SECONDS = 10
DEVICE = ""  # to list all available devices: python -m sounddevice


input(f"Press [enter] to start recording for {SECONDS} seconds.")


recording = sd.rec(int(SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, device=DEVICE)
sd.wait()


write("brain_data.wav", SAMPLE_RATE, recording)
