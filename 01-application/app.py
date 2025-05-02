from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv('AUTHOR', 'Unknown Author')

    return f"""
    <html>
        <head><title>Echo Server</title></head>
        <body>
            <h1>Echo Server Info</h1>
            <p><strong>Hostname:</strong> {hostname}</p>
            <p><strong>IP Address:</strong> {ip_address}</p>
            <p><strong>Author:</strong> {author}</p>
        </body>
    </html>
    """

@app.route('/healthz')
def health():
    # Здесь можно добавить проверку состояния приложения или базы данных
    return 'OK', 200

@app.route('/readiness')
def readiness():
    # Здесь можно добавить более сложную логику для проверки готовности
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
