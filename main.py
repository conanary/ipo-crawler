from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/ipo")
def get_ipo():
    try:
        with open("ipo.json", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
