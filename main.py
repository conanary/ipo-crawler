from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)  # ← gunicorn 就是找這個

def fetch_ipo_data():
    url = 'https://www.twse.com.tw/zh/page/IPO/new_listing.html'
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    data_list = []

    table = soup.find('table')
    if not table:
        return []

    rows = table.find_all('tr')[1:]
    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 5:
            continue
        data = {
            'stock_name': cols[0].text.strip(),
            'stock_code': cols[1].text.strip(),
            'underwriter': cols[2].text.strip(),
            'apply_start': cols[3].text.strip(),
            'apply_end': cols[4].text.strip(),
            'draw_date': cols[5].text.strip() if len(cols) > 5 else ''
        }
        data_list.append(data)

    return data_list

@app.route('/')
def hello():
    return '🎉 IPO 爬蟲 Web API 正常啟動！'

@app.route('/ipo')
def ipo():
    return jsonify(fetch_ipo_data())
﻿import requests
from bs4 import BeautifulSoup
import json

def fetch_ipo_data():
    url = 'https://www.twse.com.tw/zh/page/IPO/new_listing.html'
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    data_list = []

    table = soup.find('table')
    if not table:
        print("找不到資料表")
        return

    rows = table.find_all('tr')[1:]
    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 5:
            continue
        data = {
            'stock_name': cols[0].text.strip(),
            'stock_code': cols[1].text.strip(),
            'underwriter': cols[2].text.strip(),
            'apply_start': cols[3].text.strip(),
            'apply_end': cols[4].text.strip(),
            'draw_date': cols[5].text.strip() if len(cols) > 5 else ''
        }
        data_list.append(data)

    with open('ipo.json', 'w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=2)

    print(f'已儲存 {len(data_list)} 筆資料到 ipo.json')

if __name__ == '__main__':
    fetch_ipo_data()
