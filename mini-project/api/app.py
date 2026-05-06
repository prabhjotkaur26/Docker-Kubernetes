from flask import Flask, request, jsonify
import psycopg2
import redis
import random
import string
import os

app = Flask(__name__)

db = psycopg2.connect(os.environ['DB_URL'])
r = redis.Redis.from_url(os.environ['REDIS_URL'])


def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


# ✅ Shorten URL
@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.json
    url = data['url']
    code = generate_code()

    cur = db.cursor()
    cur.execute(
        "INSERT INTO urls(code, original, clicks) VALUES(%s,%s,0)",
        (code, url)
    )
    db.commit()

    r.set(code, url)

    return jsonify({"short": code})


# ✅ Dashboard API
@app.route('/links', methods=['GET'])
def get_links():
    cur = db.cursor()
    cur.execute("SELECT code, original, clicks FROM urls;")
    rows = cur.fetchall()

    data = []
    for row in rows:
        data.append({
            "short": row[0],
            "original": row[1],
            "clicks": row[2]
        })

    return jsonify(data)


# ✅ IMPORTANT: Always last
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)