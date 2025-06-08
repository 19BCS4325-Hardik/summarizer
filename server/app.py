import os
import gdown
import pickle
from transformers import pipeline
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MODEL_PATH = "summarizer.pkl"
GOOGLE_DRIVE_FILE_ID = "1pkdtwxdtH7_DZLcM_MF1nrRB2UIj3KIa"  # Replace this

def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model from Google Drive...")
        url = f"https://drive.google.com/uc?id={GOOGLE_DRIVE_FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)
        print("Download complete.")

print("Checking model...")
download_model()

print("Loading model...")
with open(MODEL_PATH, "rb") as f:
    summarizer = pickle.load(f)
print("Model loaded.")

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return jsonify({"summary": summary[0]['summary_text']})

if __name__ == '__main__':
    app.run(debug=True, port=5007)
