import requests
from fake_useragent import UserAgent
from tqdm import tqdm


class Post:

    def __init__(self, title, text, url):
        self.title = title
        self.text = text
        self.url = url

    def __str__(self):
        return f"""
URL: {self.url}
Title: {self.title}
Text: {len(self.text)} characters
\n
"""


def GetPosts(url, story_count=1) -> list:

    if ".json" not in url:
        url += ".json"

    data = requests.get(url, headers={"User-Agent": UserAgent().chrome}).json()

    results = []

    for story in tqdm(range(story_count), desc="Fetching Posts", ncols=80): # max per request 
    
        post = data['data']['children'][story]['data']
        title = post['title']
        text = post['selftext']
        postURL = post['url']

        results.append(Post(title, text, postURL))

    return results
    

