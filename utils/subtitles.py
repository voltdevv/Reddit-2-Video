from faster_whisper import WhisperModel
from tqdm import tqdm

model_size = "large-v3"

class Segment:
    def __init__(self, start, end, text):
        self.start = start
        self.end = end
        self.text = text

    def __str__(self):
        return f"""
Start - {self.start}s | End - {self.end}s | Text - {self.text}
"""
    
    def __repr__(self):
        return f"""
Start - {self.start}s | End - {self.end}s | Text - {self.text}
"""

def segment(path):
    model = WhisperModel(model_size, device='cpu', compute_type="int8")

    segments, info = model.transcribe(path, beam_size=5)

    segs = []
    for segment in tqdm(list(segments), desc="Creating Segments", ncols=80):
        segs.append(Segment(segment.start, segment.end, segment.text))

    return segs
