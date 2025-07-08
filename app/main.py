from flask import Flask
import redis
import time

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    try:
        r.ping()
        return 'Redis доступен!'
    except redis.exceptions.ConnectionError:
        return 'Redis не отвечает!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
