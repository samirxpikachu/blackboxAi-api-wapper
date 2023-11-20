from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
port = 3000

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/box", methods=["GET"])
def box_api():
    query = request.args.get("query", "")

    default_all_messages = [{"user": query}]
    all_messages = request.args.get("allMessages", default_all_messages)

    stream = request.args.get("stream", "")
    clicked_continue = request.args.get("clickedContinue", "false").lower() == "true"

    try:
        url = "https://useblackbox.io/chat-request-v4"
        payload = {
            "textInput": query,
            "allMessages": all_messages,
            "stream": stream,
            "clickedContinue": clicked_continue,
        }

        response = requests.post(url, json=payload)
        answer = response.json()["response"][0][0]

        return jsonify({"answer": answer}), 200
    except Exception as error:
        return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
