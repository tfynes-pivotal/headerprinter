
import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

port = int(os.getenv('PORT','3000'))

@app.route('/')
def index():
    print(json.dumps(dict(request.headers)))
    return json.dumps(dict(request.headers))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
