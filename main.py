import aiogram.types
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
from bot import sendto_telegram
from schemas import ProblemNotification
from Event import TelegramEvent
from bot import sendto_telegram


app = FastAPI()


@app.post("/to_telegram/{telegram}", response_model=ProblemNotification)
async def send_to_telegram(problem_notification: ProblemNotification):
    problem_notification = jsonable_encoder(problem_notification)
    telegram_message: aiogram.types.Message = TelegramEvent(problem_notification).make_message()
    await sendto_telegram(telegram_message)
    return {"problem_notification": ProblemNotification}


if __name__ == '__main__':
    uvicorn.run('main:app', host='192.168.0.2', port=8000)
