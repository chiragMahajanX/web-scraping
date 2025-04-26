import requests
from bs4 import BeautifulSoup
import csv


url = 'https://timesofindia.indiatimes.com/'
try:
    r = requests.get(url)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error:", e)
    exit()


soup = BeautifulSoup(r.content, 'html.parser')


headlines = soup.find_all('p', class_='CRKrj')


print("News Headlines:\n")
with open("toi_headlines.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])

    for tag in headlines:
        text = tag.get_text(strip=True)
        print(text)
        writer.writerow([text])  