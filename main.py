import datetime
from pydantic import BaseModel
from fastapi import FastAPI

from bot_logic import bot
api_bot = bot.chat_bot()

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat/")
async def chat_bot(msg: Message):
    return str(api_bot.response(msg.text))
