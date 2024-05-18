import sys
import requests
from bs4 import BeautifulSoup
import json
import os
import datetime

def search_wikipedia(phrase, proxy_url=None):
    base_url = "https://en.wikipedia.org/wiki/"
    search_url = base_url + phrase.replace(' ', '_')
    
    proxies = {}
    if proxy_url:
        proxies = {
            "http": proxy_url,
            "https": proxy_url,
        }

    print(f"Fetching URL: {search_url}")
    try:
        response = requests.get(search_url, proxies=proxies)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to access {search_url}")
        print(e)
        return None

    print("Parsing response content")
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    if not title:
        print("Error: Unable to find title in the page")
        return None

    title = title.text
    paragraphs = soup.find_all('p')
    content = "\n".join([para.text for para in paragraphs if para.text.strip()])

    return {
        "title": title,
        "url": search_url,
        "content": content
    }

def save_to_json(data):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"wikipedia_{timestamp}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")

def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("Usage: ./run_scraper.sh [phrase] [proxy_url]")
        return

    phrase = args[0]
    proxy_url = args[1] if len(args) > 1 else None

    print(f"Searching Wikipedia for phrase: {phrase}")
    data = search_wikipedia(phrase, proxy_url)
    if data:
        save_to_json(data)
    else:
        print("No data to save.")

if __name__ == "__main__":
    main()
