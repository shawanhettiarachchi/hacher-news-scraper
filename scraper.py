import csv
import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
titles = soup.find_all('span', class_='titleline')
print("Found titles:", len(titles))

with open("news.csv", "w", newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL"])



    for title in titles:
        a_tag = title.find('a')
        news_title = a_tag.text
        news_link = a_tag("href")
        writer.writerow([news_title, news_link])
print("News data saved to news.csv successfully.")




