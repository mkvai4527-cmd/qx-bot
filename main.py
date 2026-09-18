import asyncio, random, os
from datetime import datetime, timedelta
from telegram import Bot
import threading
from flask import Flask

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = "@qx_hasan_signal_bot"
PAIRS = ["EUR/USD OTC", "GBP/USD OTC", "USD/JPY OTC", "AUD/CAD OTC", "EUR/JPY OTC", "GBP/JPY OTC", "EUR/GBP OTC"]

bot = Bot(token=BOT_TOKEN)
app = Flask(__name__)

@app.route("/")
def home(): 
    return "Bot is Running"

async def send_signal():
    while True:
        pair = random.choice(PAIRS)
        direction = random.choice(["CALL 🔼", "PUT 🔽"])
        time_str = (datetime.now() + timedelta(minutes=2)).strftime("%H:%M")
        text = f"🔥 **QX HASAN VIP SIGNAL** 🔥\n\n💱 Pair: **{pair}**\n⏰ Time: **{time_str}** (2 Min)\n📊 Direction: **{direction}**\n\n⚡️ MTG: 1 STEP"
        try:
            await bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode="Markdown")
        except Exception as e:
            print(e)
        await asyncio.sleep(180)

def run_bot():
    asyncio.run(send_signal())

threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
