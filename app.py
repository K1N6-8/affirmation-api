
from flask import Flask, request, jsonify

app = Flask(__name__)

affirmations = {
    "confidence": [
        "You are enough just as you are.",
        "You are capable of amazing things."
    ],
    "calm": [
        "It’s okay to take a break.",
        "You deserve kindness and respect."
    ],
    "focus": [
        "Keep growing, one step at a time."
    ]
}

@app.route("/affirmations", methods=["GET"])
def get_affirmations():
    category = request.args.get("category")
    if category:
        return jsonify(affirmations.get(category, []))
    return jsonify(affirmations)

@app.route("/affirmations", methods=["POST"])
def add_affirmation():
    data = request.get_json()
    text = data.get("text")
    category = data.get("category")
    if not text or not category:
        return jsonify({"error": "Both 'text' and 'category' are required"}), 400
    affirmations.setdefault(category, []).append(text)
    return jsonify({"message": "Affirmation added successfully"}), 201

@app.route("/affirmations", methods=["DELETE"])
def delete_affirmation():
    data = request.get_json()
    text = data.get("text")
    category = data.get("category")
    if not text or not category:
        return jsonify({"error": "Affirmation text and category are required"}), 400
    if text in affirmations.get(category, []):
        affirmations[category].remove(text)
        return jsonify({"message": "Affirmation deleted successfully"})
    return jsonify({"error": "Affirmation not found"}), 404

@app.route("/affirmations", methods=["PATCH"])
def update_affirmation():
    data = request.get_json()
    old_text = data.get("old_text")
    new_text = data.get("new_text")
    category = data.get("category")
    if not old_text or not new_text or not category:
        return jsonify({"error": "Missing required fields"}), 400
    if category not in affirmations or old_text not in affirmations[category]:
        return jsonify({"error": "Affirmation not found"}), 404
    index = affirmations[category].index(old_text)
    affirmations[category][index] = new_text
    return jsonify({"message": "Affirmation updated successfully"})
