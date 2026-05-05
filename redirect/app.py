from flask import Flask, redirect
import psycopg2
import redis
import os

app = Flask(__name__)

db = psycopg2.connect(os.environ['DB_URL'])
r = redis.Redis.from_url(os.environ['REDIS_URL'])


@app.route('/<code>')
def go(code):
    # 🔥 Try Redis first (fast)
    url = r.get(code)

    if url:
        url = url.decode()
    else:
        # fallback to DB
        cur = db.cursor()
        cur.execute("SELECT original FROM urls WHERE code=%s", (code,))
        row = cur.fetchone()

        if not row:
            return "Not found", 404

        url = row[0]
        r.set(code, url)

    # ✅ increment clicks
    cur = db.cursor()
    cur.execute("UPDATE urls SET clicks = clicks + 1 WHERE code=%s", (code,))
    db.commit()

    return redirect(url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)