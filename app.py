from flask import Flask, render_template, request, jsonify
from itinerary import generate_itinerary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/plan", methods=["POST"])
def plan():
    data = request.get_json()

    destination = data["destination"]
    days = int(data["days"])
    budget = int(data["budget"])
    interests = data["interests"]

    itinerary = generate_itinerary(destination, days, budget, interests)

    return jsonify({
        "destination": destination,
        "days": days,
        "budget": budget,
        "budget_breakdown": {
            "travel": int(budget * 0.25),
            "food": int(budget * 0.35),
            "stay": int(budget * 0.40)
        },
        "itinerary": itinerary,
        "map": f"https://www.google.com/maps/search/{destination}"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
