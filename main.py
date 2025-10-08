from utils.story import GetPosts
from utils.voiceover import Voice

v = Voice()

post = GetPosts('https://www.reddit.com/r/AITAH/.json')[0]

v.generate(post.text)