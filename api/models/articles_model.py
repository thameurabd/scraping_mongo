import requests
from bs4 import BeautifulSoup as bs
from config.database import connexion
class BBC:
    def __init__(self, url:str):
        article = requests.get(url)
        self.soup = bs(article.content, "html.parser")
        self.title = self.get_title()
        self.author = self.get_author()
        self.summary = self.get_summary()
    #get article title
    def get_title(self) -> str:
        return self.soup.find(class_="ssrcss-15xko80-StyledHeading e1fj1fc10").text
    #get article author
    def get_author(self) -> str:
        return self.soup.find(class_="ssrcss-ugte5s-Contributor e5xb54n2").text
    #get article summary
    def get_summary(self) -> str:
        return self.soup.find(class_="ssrcss-1q0x1qg-Paragraph eq5iqo00").text        

parsed = BBC("https://www.bbc.com/news/uk-politics-62025612")

print(parsed.author)
print(parsed.title)
print(parsed.summary)

#converting parsed object to to dict
parsed_dict = {"title":parsed.title, "author":parsed.author, "summary":parsed.summary}

#inserting into MongoDB 
connexion["scraping"]["articles_db"].insert_one(parsed_dict)

