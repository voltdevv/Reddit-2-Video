from moviepy import VideoFileClip

class Editer:
    def __init__(self, path_to_video):
        self.video = VideoFileClip(path_to_video)

    def tiktok_crop(self):
        w, h = self.video.size

        if w > h:
            left = (w - h) // 2
            right = left + h
            cropped = self.video.cropped(x1=left, x2=right, y1=0, y2=h)
        else:
            cropped = self.video  

        vertical = cropped.resized(new_size=(1080, 1920))
        vertical.write_videofile("result.mp4")

