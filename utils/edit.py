from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from subtitles import segment


clip = VideoFileClip('test.mp4')


segments = segment('output/test.wav')


subtitle_clips = []

for seg in segments:
    txt_clip = TextClip(
    seg.text,
    fontsize=80,
    color="white",
    font="Arial-Bold"
    ).set_start(seg.start).set_end(seg.end)
    subtitle_clips.append(txt_clip)


final_clip = CompositeVideoClip([clip, *subtitle_clips])


final_clip.write_videofile("video_with_subs.mp4")
