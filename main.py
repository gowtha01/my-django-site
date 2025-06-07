from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <h1>Welcome to Landing Page 1</h1>
    <p>This is your FastAPI landing page. Replace this with your actual content.</p>
    <a href="/landing2">Next</a>
    """

@app.get("/landing2", response_class=HTMLResponse)
async def landing2():
    return """
    <h1>Welcome to Landing Page 2</h1>
    <p>This is your FastAPI landing page 2. Replace this with your actual content.</p>
    <a href="/">Back</a>
    """