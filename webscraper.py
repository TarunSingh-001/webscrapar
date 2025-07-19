

import requests
from bs4 import BeautifulSoup
url = 'https://www.bbc.com/news'

try:
    response = requests.get(url)
    response.raise_for_status()  
except Exception as e:
    print("Something went wrong while fetching the webpage:", e)
    exit()
soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all('h3')
titles = []
for h in headlines:
    text = h.get_text(strip=True)
    if text:  
        titles.append(text)

with open('headlines.txt', 'w', encoding='utf-8') as f:
    for title in titles:
        f.write(title + '\n')

print("Done! Headlines saved to 'headlines.txt'")
