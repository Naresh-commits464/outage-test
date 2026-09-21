from flask import Flask, jsonify
from config import S3_BUCKET, SLACK_ALERT_WEBHOOK

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "bucket": S3_BUCKET})


@app.route("/notify")
def notify():
    # In a real deployment this would POST to SLACK_ALERT_WEBHOOK
    return jsonify({"notified": True})


if __name__ == "__main__":
    app.run(debug=True)
