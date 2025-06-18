
from flask import Flask, request, jsonify

app = Flask(__name__)

affirmations = {
    "confidence": [
        "You are enough just as you are.",
        "Your voice matters.",
        "You are capable of amazing things.",
        "You are creative and full of ideas.",
        "You’re doing better than you think.",
        "You are worthy of good things.",
        "Believe in your own magic.",
        "You have the power to change your story.",
        "You are brave and resilient.",
        "You are proud of yourself.",
        "You have a unique purpose.",
        "You are a positive force in the world.",
        "You are deserving of happiness.",
        "You can overcome challenges with grace.",
        "You are in charge of your own happiness.",
        "You inspire others without even trying.",
        "Your dreams are worth chasing.",
        "You are becoming the best version of yourself.",
        "You radiate strength and confidence.",
        "You trust yourself to make the right decisions."
    ],
    "calm": [
        "It’s okay to take a break.",
        "Your feelings are valid.",
        "You deserve kindness and respect.",
        "Mistakes are part of learning.",
        "You are surrounded by love.",
        "You bring light to those around you.",
        "You are patient with yourself.",
        "You are kind to yourself and others.",
        "Let go of what you can’t control.",
        "Peace begins with a deep breath.",
        "You are safe in this moment.",
        "Calmness washes over you like a wave.",
        "Breathe in peace, breathe out tension.",
        "You release what no longer serves you.",
        "Your calm heart is your strength.",
        "Silence is a source of great strength.",
        "Every breath brings you peace.",
        "Relaxation is your natural state.",
        "Stillness restores your spirit.",
        "You are a peaceful presence in the world."
    ],
    "focus": [
        "Keep growing, one step at a time.",
        "Every day is a new opportunity.",
        "You are making progress even if it’s small.",
        "Stay present and take it one task at a time.",
        "Your goals are within reach when you stay consistent.",
        "Distractions are temporary — your vision is long-term.",
        "You have the power to direct your attention.",
        "Focus on what you can control.",
        "You are clear, focused, and determined.",
        "One step at a time gets you to the finish line.",
        "You concentrate on what matters most.",
        "Each task you complete moves you forward.",
        "You manage your time with purpose.",
        "You turn your thoughts into focused action.",
        "You are centered and grounded in the now.",
        "Your attention fuels your goals.",
        "You work efficiently and effectively.",
        "You block out distractions and focus deeply.",
        "You approach each task with clarity and calm.",
        "You follow through with determination."
    ]
}

@app.route('/affirmations', methods=['GET'])
def get_affirmations():
    return jsonify(affirmations)

@app.route('/affirmations', methods=['POST'])
def add_affirmation():
    data = request.get_json()
    text = data.get("text")
    category = data.get("category")
    if not text or not category:
        return jsonify({"error": "Both 'text' and 'category' are required"}), 400
    if category not in affirmations:
        affirmations[category] = []
    affirmations[category].append(text)
    return jsonify({"message": "Affirmation added successfully"})

@app.route('/affirmations', methods=['DELETE'])
def delete_affirmation():
    data = request.get_json()
    text = data.get("text")
    category = data.get("category")
    if not text or not category:
        return jsonify({"error": "Both 'text' and 'category' are required"}), 400
    if category in affirmations and text in affirmations[category]:
        affirmations[category].remove(text)
        return jsonify({"message": "Affirmation deleted successfully"})
    return jsonify({"error": "Affirmation not found"}), 404

@app.route('/affirmations', methods=['PATCH'])
def update_affirmation():
    data = request.get_json()
    old_text = data.get("old_text")
    new_text = data.get("new_text")
    category = data.get("category")
    if not old_text or not new_text or not category:
        return jsonify({"error": "Fields 'old_text', 'new_text', and 'category' are required"}), 400
    if category in affirmations and old_text in affirmations[category]:
        index = affirmations[category].index(old_text)
        affirmations[category][index] = new_text
        return jsonify({"message": "Affirmation updated successfully"})
    return jsonify({"error": "Affirmation not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
