from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_ipo_data():
    url = 'https://www.twse.com.tw/IPO/newListing?response=json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    json_data = res.json()

    # 取出表格資料
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
