from moviepy import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from utils.subtitles import Segment
from random import randint



class Editor():

    def __init__(self, video_path, audio_path, output_path = "output/result.mp4"):

        self.video = VideoFileClip(video_path)
        self.audio = AudioFileClip(audio_path)
        self.text_clips = []
        self.output_path = output_path

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
        
        result = CompositeVideoClip([self.video, *self.text_clips])
        result.with_audio(self.audio)
        #cropping
        result.write_videofile(self.output_path)
        print(f'✔️ Completed at {self.output_path}')


    def set_video_duration(self, short_length):
        # MINUTES !
        duration = self.video.duration / 60
        start = randint(0, int(duration - short_length))
        end = start + short_length

        self.video = self.video.subclipped((start, 0),(end, 0))
        return self.video

