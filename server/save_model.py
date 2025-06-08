from transformers import pipeline
import pickle

def save_model():
    print("Loading model (PyTorch only)...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")
    print("Model loaded. Saving to summarizer.pkl ...")

    with open("summarizer.pkl", "wb") as f:
        pickle.dump(summarizer, f)

    print("Model saved successfully.")

if __name__ == "__main__":
    save_model()
