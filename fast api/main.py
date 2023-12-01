from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse
import yt
# import ./index.html as index
index = open("index.html").read()

app = FastAPI()


@app.get("/")
async def root():
    return HTMLResponse(content=index, status_code=200)


@app.get("/about/developer")
async def about():
    return {"Name": "Anurag Dahal",
            "Address": "Birtamode,Jhapa",
            "Age": "20"}


@app.post("/about/developer/{name}/{address}/{age}")
async def put_details(name: str, address: str, age: int, sort=Optional[str]):
    return {"Name": f"{name}",
            "Address": f"{address}",
            "Age": f"{age}"}


@app.get("/blog/latest")
async def blog_latest():
    return {"title": "Latest Blog",
            "content": "This is the content of the latest blog"}


@app.post("/blog/{id}/comments")
async def comments(id: int, limit: int):
    return {"blog_id": id,
            "comments": f"{limit} comments of the blog id {id}"}


@app.get("/blog/{id}")
async def update(id: int, limit, update: bool):
    if update:
        return {f"{limit} updated blogs from the db"}
    else:
        return {f"{id} blog is not updated"}


@app.delete("/blog/{id}")
async def delete_blog(id: int):
    return {f"{id} blog is deleted from the db"}


@app.get("/yt/")
async def download(link: str):
    yt.download(link)
    return {"Downloaded": "Downloaded"}
