from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "[Layer 7] Hello from Application Layer!"

if __name__ == "__main__":
    print("[Layer 7] Starting Flask server...")
    app.run(host="127.0.0.1", port=5000)
