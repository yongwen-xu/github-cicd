import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.ensure_ascii = False


def get_db_connection():
    conn = psycopg2.connect(
        os.environ.get(
            "DATABASE_URL", "postgresql://user:password@localhost:5432/sampledb"
        )
    )
    return conn


@app.route("/api/search", methods=["GET"])
def search_plans():
    prefecture_code = request.args.get("prefecture_code")
    if not prefecture_code:
        return jsonify({"error": "prefecture_code is required"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "SELECT plan_id, prefecture_code, hotel_name, plan_name, start_date, end_date, price "
            "FROM hotel_plan WHERE prefecture_code = %s;",
            (prefecture_code,),
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()

        plans = []
        for row in rows:
            plans.append(
                {
                    "plan_id": row[0],
                    "prefecture_code": row[1],
                    "hotel_name": row[2],
                    "plan_name": row[3],
                    "start_date": row[4].isoformat(),
                    "end_date": row[5].isoformat(),
                    "price": row[6] * 1.1,
                }
            )
        return jsonify(plans)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port)