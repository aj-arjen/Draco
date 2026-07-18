import os
from threading import Thread

from flask import Flask

from bot import Draco
from settings import TOKEN

print("========== MAIN.PY STARTED ==========")

app = Flask(__name__)


@app.route("/")
def home():
    return "DracoBot is running!", 200


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


Thread(target=run_web, daemon=True).start()

bot = Draco()

print("Starting Draco...")
bot.run(TOKEN)