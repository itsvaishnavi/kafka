# app.py
from flask import Flask, render_template, jsonify
import json
import time
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chart.html')

@app.route('/data')
def get_data():
    try:
        with open('data.json', 'r') as f:
            raw_data = json.load(f)
    except FileNotFoundError:
        raw_data = []

    # Convert numeric timestamp to readable string
    for item in raw_data:
        ts = item.get('timestamp')
        if isinstance(ts, (int, float, str)) and str(ts).isdigit():
            readable_time = datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S')
            item['timestamp'] = readable_time

    return jsonify(raw_data)

if __name__ == '__main__':
    app.run(debug=True)
