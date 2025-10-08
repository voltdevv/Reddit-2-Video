from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from subtitles import Segment



class Editor():

    def __init__(self, video_path, audio_path):

        self.video = VideoFileClip(video_path)
        self.audio = AudioFileClip(audio_path)
        self.text_clips = []

    def add_subtitles(self, *segments: Segment):

        for seg in segments:

            duration = seg.end - seg.start

            text = (
                TextClip(font="resources/font/TikTokSans-VariableFont_opsz,slnt,wdth,wght.ttf",
                         color="white", text=seg.text, font_size=70, vertical_align="center",
                         horizontal_align="center", duration=duration)
                         .with_start(seg.start)
                         .with_end(seg.end)
            )
            self.text_clips.append(text)

    
    def complete(self):
        pass


        

        
        


    
        