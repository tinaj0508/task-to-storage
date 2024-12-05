import os
from flask import Flask, request, jsonify
from google.cloud import storage

app = Flask(__name__)

# 環境變量中設置存儲桶名稱
BUCKET_NAME = os.getenv("BUCKET_NAME")

@app.route("/", methods=["POST"])
def handle_task():
    request_json = request.get_json()
    if not request_json or "message" not in request_json:
        return jsonify({"error": "Invalid request"}), 400

    message = request_json["message"]
    processed_message = message.upper()

    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob("processed_message.txt")
    blob.upload_from_string(processed_message)

    return jsonify({"message": f"Processed and stored: {processed_message}"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
