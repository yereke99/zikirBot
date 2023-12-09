from load import bot, storage
from main import dp
import aioschedule
import asyncio
from database import Database
from datetime import datetime


db = Database()

async def sendToTelegram(data):

    for item in data:
        message = f"""**{item[0]}**"""
        print(f"Sending to Telegram Channel: {message}")

        await bot.send_message(
            "@salauat_group", 
            message,
            parse_mode="Markdown",
        )
    

async def sendNoti():
    current_time = datetime.now()
    formatted_data = current_time.strftime("%H:%M")
    print(formatted_data)
    data = db.Fetch(formatted_data)

    if len(data) != 0:
        await sendToTelegram(data=data)


async def sendNotiTest(time: str):
    t = time
    data = db.FetchAll()

    if len(data) != 0:
        await sendToTelegram(data=data)



# Async-Schedule here is working every 5 seconds fo async-engine.
async def scheduler():
    aioschedule.every(3).seconds.do(sendNoti)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_start(dp):
    asyncio.create_task(scheduler())


async def on_stop(dp):
    await bot.close()
    await storage.close()

def main():
    from aiogram import executor
    #executor.start_polling(dp, on_shutdown=on_stop)
    executor.start_polling(dp, on_startup=on_start, on_shutdown=on_stop)

if __name__ == "__main__":
    main()
