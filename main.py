from utils.story import GetPosts
from utils.voiceover import Voice

post = GetPosts('https://www.reddit.com/r/AITAH')[0]

v = Voice()

v.generate(post.text)