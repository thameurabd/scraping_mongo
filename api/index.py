from fastapi import FastAPI
from articles_routes import articles_router

#create app
app = FastAPI()

#register router
app.include_router(articles_router)
print("job done")

