# save_model.py
from transformers import pipeline
import pickle

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Save the pipeline object with pickle
with open("summarizer.pkl", "wb") as f:
    pickle.dump(summarizer, f)

print("Model saved as summarizer.pkl")
