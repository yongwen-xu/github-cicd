import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route("/api/travel/plans", methods=["GET"])
def get_travel_plans():
    prefecture_code = request.args.get("prefecture_code")
    if not prefecture_code:
        return jsonify({"error": "prefecture_code is required"}), 400

    try:
        booking_api_url = os.environ.get("BOOKING_API_URL")
        response = requests.get(
            f"{booking_api_url}/api/search", params={"prefecture_code": prefecture_code}
        )
        response.raise_for_status()
        plans = response.json()
        return jsonify(
            {
                "source": "booking-api",
                "prefecture_code": prefecture_code,
                "plans": plans,
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT"))
    app.run(host="0.0.0.0", port=port)