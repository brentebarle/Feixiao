from flask import Flask

# Flask HTTP server for status monitoring
app = Flask(__name__)

@app.route('/')
def status():
    return "Feixiao is running"

def start_http_server():
    app.run(host='0.0.0.0', port=5002)
