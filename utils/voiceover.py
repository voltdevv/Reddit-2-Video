import pyttsx3
import os


class Voice:
    
    def __init__(self, rate=125, output_path="output", file_name="test.wav"):
        self.rate = rate
        self.output_path = output_path
        self.file_name = file_name if file_name.endswith(".wav") else file_name + ".wav"

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def get_full_path(self):
        return os.path.join(self.output_path, self.file_name)

    def generate(self, text: str):
        if not text.strip():
            raise ValueError("Text cannot be empty.")

        engine = pyttsx3.init()
        engine.setProperty("rate", self.rate)
        engine.save_to_file(text, self.get_full_path())
        engine.runAndWait()
        engine.stop()

        print(f"[✔] Audio saved to: {self.get_full_path()}")

