from faster_whisper import WhisperModel


model_size = "large-v3"


"""
uses fast-whisper to get subtitle 
timestamps from the voiceover.py output (.wav file)
no idea how it works tbh credits will be at the bottom
of the github
"""

def segment(path):
    model = WhisperModel(model_size, device='cpu', compute_type="int8")

    segments, info = model.transcribe(path, beam_size=5)

    segs = []
    for segment in segments:
        segs.append(Segment(segment.start, segment.end, segment.text))

    return segs

class Segment:

    def __init__(self, start, end, text):
        self.start = start
        self.end = end
        self.text = text

    def __str__(self):
        return f"""
Start - {self.start}
End - {self.end}
Text - {self.text}
"""
    


