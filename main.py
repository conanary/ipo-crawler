from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '🎉 IPO 資料 API 已啟動！'

@app.route('/ipo')
def ipo():
    try:
        with open('ipo.json', encoding='utf-8') as f:
            json_data = json.load(f)

        raw_data = json_data.get('data', [])
        result = []
        for row in raw_data:
            result.append({
                'stock_name': row[0],
                'stock_code': row[1],
                'underwriter': row[2],
                'apply_start': row[3],
                'apply_end': row[4],
                'draw_date': row[5],
            })

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})
