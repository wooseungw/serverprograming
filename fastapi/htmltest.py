from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"))

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>Hello</h1><img src=/static/movie4.jpg width=100 height=100>"