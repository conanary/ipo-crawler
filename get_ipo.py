import requests
import json

url = 'https://openapi.twse.com.tw/v1/opendata/t187ap03_L'

try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
    data = res.json()

    with open('ipo.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ 已成功儲存 IPO JSON 至 ipo.json")

except requests.exceptions.RequestException as e:
    print(f"❌ 發生請求錯誤：{e}")
except json.JSONDecodeError as e:
    print(f"❌ 回傳不是有效的 JSON：{e}")
