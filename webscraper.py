import requests
from bs4 import BeautifulSoup
from string import punctuation
import os


number_of_pages = int(input())
type_of_article = input()
first_base = "https://www.nature.com"
second_base = "https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page="
cwd = os.getcwd()

for i in range(1, number_of_pages + 1):
    full_path = os.path.join(cwd, "PAGE_" + str(i))
    if not os.path.exists(full_path):
        os.mkdir(full_path)
    url = second_base + str(i)
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    articles = BeautifulSoup(r.content, "html.parser").find_all('article')

    for article in articles:
        possible_type = article.find("span", {"data-test": "article.type"}).text.strip()
        if possible_type == type_of_article:
            translator = str.maketrans('', '', punctuation)
            title_link = article.find("a", {"data-track-action": "view article"})
            title = title_link.text.strip().translate(translator).replace(" ", "_")
            n = requests.get(first_base + title_link.get("href"), headers={'Accept-Language': 'en-US,en;q=0.5'})
            bodies = BeautifulSoup(n.content, "html.parser").find_all("div")

            for body in bodies:
                class_value = body.get("class")
                if class_value is not None and "body" in "".join(class_value):
                    article_body = body.text
                    file_path = os.path.join(full_path, title + ".txt")
                    with open(file_path, "wb") as f:
                        f.write(article_body.encode("utf-8"))
