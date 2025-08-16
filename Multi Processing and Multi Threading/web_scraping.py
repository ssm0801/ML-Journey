"""
Web scraping often involes making numerous network requests to fetch web pages.
These tasks are IO bound because they spend lot of time waiting for responses from servers.
Multi threading can significantly improve performance by allowing multiple web pages to be fetched concurrently.
"""

import threading
import time
import requests
from bs4 import BeautifulSoup

urls = [
    "https://python.langchain.com/docs/introduction/",
    "https://python.langchain.com/docs/concepts/",
    "https://python.langchain.com/docs/tutorials/",
]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"Character count {len(soup.text)} from {url}")


start_time = time.time()
for url in urls:
    fetch_content(url)
end_time = time.time()
print(f"Time taken = {end_time - start_time}")


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)

start_time = time.time()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
end_time = time.time()
print(f"Time taken = {end_time - start_time}")
