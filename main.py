from concurrent.futures import ThreadPoolExecutor
from utils.story import GetPosts
from utils.voiceover import Voice
from utils.filter import filter
from utils.subtitles import segment
from utils.edit import Editor

# ----------- Config -----------
REDDIT_URL = ''
NUMBER_OF_POSTS = 1 # 25 max
# ------------------------------