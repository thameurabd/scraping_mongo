import uvicorn
from fastapi import FastAPI
from articles_routes import articles_router

#create app
app = FastAPI()

#register router
app.include_router(articles_router)

# run as entry point
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

