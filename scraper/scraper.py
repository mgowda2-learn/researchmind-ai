import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

def fetch_page(url):
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    response = requests.get(url,headers=headers, timeout=10)
    return response.text

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    main_content = soup.find("div", {"id": "mw-content-text"})

    if not main_content:
        main_content = soup

    for tag in main_content(["script", "style", "nav", "footer",
                              "sup", "header", "aside", "figure",
                              "button", "table"]):
        tag.decompose()

    texts = []
    for tag in main_content.find_all(["p", "h1", "h2", "h3", "h4"]):
        text = tag.get_text().strip()
        if text:
            texts.append(text)

    return "\n".join(texts)

def save_to_file(content, topic):
    os.makedirs("data/raw", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/{topic}_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Saved to {filename}")
    return filename


if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    topic = "artificial_intelligence"

    print(f"fetching {url}....")
    html = fetch_page(url)

    print("Extract content......")
    content = clean_html(html)

    print("Save to file.....")
    filename = save_to_file(content, topic)

    print(content[:500])


