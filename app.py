import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Cloud! This is a PaaS Deployment.'

if __name__ == '__main__':
    # Use PORT if Railway sets it; default 5000 for local dev
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
