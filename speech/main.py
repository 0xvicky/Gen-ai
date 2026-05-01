import speech_recognition as sr
from speech_recognition.recognizers import google


def main():
    r = sr.Recognizer()

    # Try with explicit sample rate
    with sr.Microphone(device_index=2, sample_rate=44100) as source:
        print("Calibrating...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2
        print("Speak something...")

        audio = r.listen(source)
        print("Processing audio...")

        stt = google.recognize_legacy(r, audio, language="en-IN")
        print("You said:", stt)


main()
