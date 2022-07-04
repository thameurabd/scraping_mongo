#serialiser et convertir mongodb format

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

