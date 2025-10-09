from utils.story import GetPosts
from utils.voiceover import Voice
from utils.filter import filter
from utils.subtitles import segment
from utils.edit import Editor



post = GetPosts('https://www.reddit.com/r/AITAH/', 3)[1].text

v = Voice()
video = 'resources/video/video.mp4'

audio_file = v.generate(filter(post))
subtitles = segment(audio_file)

e = Editor(video, audio_file)


e.add_subtitles(subtitles)
e.set_video_duration(3)
e.complete()
