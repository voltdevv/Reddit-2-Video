import pyttsx3
import os
from tqdm import tqdm 

class Voice:
    
    def __init__(self, rate=150, output_path="output", file_name="test"):
        self.rate = rate
        self.output_path = output_path
        self.file_name = file_name if file_name.endswith(".wav") else file_name + ".wav"
        self.files = []
        self.count = 0

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def get_full_path(self):
        return os.path.join(self.output_path, self.file_name)

    def generate(self, text: str):
        if not text.strip():
            raise ValueError("Text cannot be empty.")
        
        engine = pyttsx3.init()

        steps = [
            lambda: engine.setProperty("rate", self.rate),
            lambda: self.__check(),
            lambda: engine.save_to_file(text, self.get_full_path()),
            lambda: engine.runAndWait(),
            lambda: engine.stop()
        ]
        
        for step in tqdm(steps, desc="Generating..", ncols=80):
            step()

        print(f"[✔] Audio saved to: {self.get_full_path()}")

    
    def __check(self):
        
        while self.file_name in self.files:
            name, ext = os.path.splitext(self.file_name)
            self.file_name = name + str(self.count) + ext
            self.count += 1

        self.files.append(self.file_name)