from flask import Flask, Response
import json

app = Flask(__name__)

@app.route("/ipo")
def get_ipo():
    try:
        with open("ipo.json", encoding="utf-8") as f:
            data = json.load(f)
            # 使用 Response 搭配 indent 美化輸出
            return Response(
                json.dumps(data, indent=2, ensure_ascii=False),
                mimetype="application/json"
            )
    except Exception as e:
        return Response(
            json.dumps({"error": str(e)}, ensure_ascii=False, indent=2),
            mimetype="application/json"
        )

if __name__ == "__main__":
    app.run()
