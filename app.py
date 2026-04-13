from flask_cors import CORS
from flask import Flask, request, jsonify
import pandas as pd
import requests


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "backend Hackathon"

@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "GET":
        return jsonify({"message": "Send a JSON POST with 'study hours' and 'mood'"}), 200

    if not request.is_json:
        return jsonify({"error": "Invalid input, expected JSON"}), 400

    data = request.get_json()
    hours = data.get("study_hours")
    mood = data.get("mood")
    if hours is None or mood is None:
        return jsonify({"error": "Missing 'study hours' or 'mood' in input"}), 400
    
    try:
        github_response = requests.get("https://api.github.com")
        github_data = github_response.json()
        github_url = github_data.get("current_user_url", "N/A")
    except Exception:
        github_url = "API Error"

    try:
        weather_response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin_data = weather_response.json()
        bitcoin_price = bitcoin_data.get("bpi", {}).get("USD", {}).get("rate", "N/A")
    except Exception:
        bitcoin_data = {}
        bitcoin_price = "API Error"

    df =pd.read_csv("student_data.csv")
    avg_marks=df["marks"].mean()
    low_marks=df[df["marks"]<50].shape[0]
    avg_by_mood=df.groupby("mood")["marks"].mean().to_dict()

    # Ensure hours is numeric
    try:
        hours_num = float(hours)
    except (TypeError, ValueError):
        return jsonify({"error": "'study hours' must be a number"}), 400

    if hours_num < 3:
        suggestion = "You should study more to improve your performance."
    elif mood == "tired":
        suggestion = "Make sure to get enough rest and take breaks while studying."
    else:
        suggestion = "Keep up the good work and maintain a balanced study routine."

    return jsonify({
        "suggestion": suggestion,
        "average_marks": avg_marks,
        "students_below_50": low_marks,
        "average_by_mood": avg_by_mood,
        "bitcoin_price_usd": bitcoin_price,
        "github_url": github_url
    }), 200
    

if __name__ == "__main__":
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5000, debug=True)


