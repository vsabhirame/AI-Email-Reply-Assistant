from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def generate_reply(email, tone):
    return f"[{tone}] Thanks for your email. I will get back to you shortly."

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/reply")
async def reply(email: str = Form(...), tone: str = Form(...)):
    response = generate_reply(email, tone)
    return {"reply": response}