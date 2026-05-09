import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from starlette.requests import Request
from openai import OpenAI

load_dotenv("../.env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)

app = FastAPI()

def generate_reply(email, tone):
    prompt = f"""
Write a {tone.lower()} professional email reply.

Email:
{email}

Reply:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r") as f:
        return f.read()


@app.post("/reply")
async def reply(email: str = Form(...), tone: str = Form(...)):
    response = generate_reply(email, tone)
    return {"reply": response}