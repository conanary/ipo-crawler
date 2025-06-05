from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_ipo_data():
    url = 'https://www.twse.com.tw/IPO/newListing?response=json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36'
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()  # 自動丟出 HTTP 錯誤
        json_data = res.json()
    except Exception as e:
        return {'error': str(e)}  # 回傳錯誤內容給你看

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
    return result

@app.route('/')
def home():
    return '🎉 IPO 資料 API 正常啟動！'

@app.route('/ipo')
def ipo():
    return jsonify(fetch_ipo_data())
