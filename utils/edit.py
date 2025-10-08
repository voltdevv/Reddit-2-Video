from moviepy import VideoFileClip, TextClip, CompositeVideoClip


class Editor():

    def __init__(self, video, audio):

        self.video = video
        self.audio = audio
        self.subtitle_clips = []

    def subtitles(self):
        