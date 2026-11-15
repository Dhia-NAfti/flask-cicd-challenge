# app.py
import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello from my CI/CD pipeline!"}

@app.route("/health")
def health():
    return {"status": "healthy"}

@app.route("/version")
def version():
    return {
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "application": "Flask CI/CD Challenge"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
