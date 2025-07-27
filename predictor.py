import time
from telegram_bot import send_telegram
import random
import datetime

def fetch_next_matchday():
    # Simulate dynamic matchday detection logic
    now = datetime.datetime.now()
    return f"Matchday {now.minute % 50 + 1}"  # Simulated rotating matchday

def advanced_rng_prediction():
    # Simulate an RNG-based prediction with weighted logic
    outcomes = ["1", "X", "2"]
    weights = [0.5, 0.2, 0.3]  # More likely to predict "1"
    predictions = random.choices(outcomes, weights=weights, k=5)
    return predictions

def run_prediction_loop():
    last_matchday = None
    while True:
        try:
            current_matchday = fetch_next_matchday()
            if current_matchday != last_matchday:
                predictions = advanced_rng_prediction()
                message = (
                    f"🎯 *Life Changer Predictor Bot*
"
                    f"🕐 {datetime.datetime.now().strftime('%H:%M:%S')} | {current_matchday}

"
                    f"📊 Predictions:
"
                    + '\n'.join([f"Game {i+1}: *{pred}*" for i, pred in enumerate(predictions)]) +
                    "\n\n_Updated every 5 min automatically_"
                )
                send_telegram(message)
                last_matchday = current_matchday
            else:
                print("Same matchday — skipping...")
        except Exception as e:
            print("Error during prediction:", e)
        time.sleep(300)  # Sleep 5 minutes