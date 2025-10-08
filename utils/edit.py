from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import os


clip = VideoFileClip(
    filename= 'video/video.mp4',
).subclipped("00:00:00.00", "00:0:15.00")

txt_clip = TextClip(
    text="Hello there!",
    font="font/TikTokSans-VariableFont_opsz,slnt,wdth,wght.ttf",
    font_size=70,
    color='white',
    method='caption', 
    size=clip.size  # match video size
).with_duration(10).with_position('center')


final = CompositeVideoClip([clip, txt_clip])
final.write_videofile("result.mp4")