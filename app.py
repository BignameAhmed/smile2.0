from flask import Flask
from threading import Thread
from predictor import run_prediction_loop

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Life Changer Predictor Bot is Running!"

def start_background():
    Thread(target=run_prediction_loop, daemon=True).start()

if __name__ == '__main__':
    start_background()
    app.run(host='0.0.0.0', port=10000)