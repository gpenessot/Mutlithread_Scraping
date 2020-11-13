import requests
import time
import concurrent.futures
from numpy import random

# On définit le nombre max de thread
MAX_THREADS = 30

def download_url(url):
    print(url)
    resp = requests.get(url)
    title = ''.join(x for x in url if x.isalpha()) + "html"
    
    with open(title, "wb") as fh:
        fh.write(resp.content)
        
    time.sleep(random(0.1, 0.25))
    
def download_stories(story_urls):
    threads = min(MAX_THREADS, len(story_urls))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(download_url, story_urls)

def main(story_urls):
    t0 = time.time()
    download_stories(story_urls)
    t1 = time.time()
    print(f"{t1-t0} seconds to download {len(story_urls)} stories.")
