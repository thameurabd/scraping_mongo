from fastapi import APIRouter
from models.articles_model import BBC
from database import connexion


# defining models to serialize and convert mongo records into dicts and visversa
def articles_entity(db_item) -> dict:
    return {
        "title": db_item["title"],
        "author": db_item["author"],
        "summary": db_item["summary"]

    }


def list_articles_entities(db_item_list) -> list:
    list_art_entit = []
    for it in db_item_list:
        list_art_entit.append(articles_entity(it))

    return list_art_entit


articles_router = APIRouter()

@articles_router.get("/hello")
async def hello_world():
    return "hello world !"

@articles_router.get("/articles")
async def get_all_articles():
    return list_articles_entities(connexion.scraping.articles_db.find())

#get article by title
@articles_router.get("/articles/{title}")
async def get_article_by_title(title:str):
    return list_articles_entities(connexion.scraping.articles_db.find({"title":title}))
    