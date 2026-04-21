import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


@app.route("/")
def home():
    return {"message": "Backend virker"}


@app.route("/api/status")
def status():
    return {"system": "online", "database": "postgres configured"}


@app.route("/api/readings", methods=["GET"])
def get_readings():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, temperature, humidity, motion, created_at
        FROM sensor_readings
        ORDER BY created_at DESC
        LIMIT 10;
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    data = [
        {
            "id": row[0],
            "temperature": row[1],
            "humidity": row[2],
            "motion": row[3],
            "created_at": str(row[4])
        }
        for row in rows
    ]

    return jsonify(data)


@app.route("/api/readings", methods=["POST"])
def add_reading():
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO sensor_readings (temperature, humidity, motion)
        VALUES (%s, %s, %s);
    """, (
        data.get("temperature"),
        data.get("humidity"),
        data.get("motion")
    ))

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Reading saved", "data": data}, 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
