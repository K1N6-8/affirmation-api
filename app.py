
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
    ],
    "self-esteem": [
        "Your worth isn’t measured by productivity.",
        "You are enough without needing to prove anything.",
        "You deserve kindness from yourself and others.",
        "You trust yourself to grow and learn.",
        "You are worthy of love, exactly as you are.",
        "You are proud of how far you’ve come.",
        "You believe in your own voice and truth.",
        "You honor your emotions and your journey.",
        "You have the right to take up space.",
        "You are not your mistakes — you are your growth.",
        "You embrace who you are becoming.",
        "You speak to yourself with compassion.",
        "You are deserving of respect and care.",
        "You are grounded in your own value.",
        "You recognize your own unique brilliance.",
        "You release self-doubt and invite self-love.",
        "You are allowed to shine.",
        "You are enough, just by being you.",
        "You matter in this world.",
        "You celebrate yourself without guilt."
    ],
    "safety": [
        "You are grounded and protected in this moment.",
        "You are allowed to feel safe in your body.",
        "You are surrounded by peace and security.",
        "Your boundaries are strong and respected.",
        "You release fear and return to calm.",
        "You are supported, even when things feel uncertain.",
        "You create safety within yourself.",
        "You trust the world is safe enough for you to rest.",
        "You are safe to express your truth.",
        "You are held by your breath and your body.",
        "Stillness is a safe place for you.",
        "You feel anchored and stable within.",
        "You are rooted in peace and strength.",
        "Calm and safety are your birthrights.",
        "You trust the process of healing and protection.",
        "You feel secure in who you are.",
        "Each breath reminds you that you are safe.",
        "You are wrapped in comfort and care.",
        "You deserve to feel protected and valued.",
        "You are shielded by your own strength and wisdom."
    ],
    "gratitude": [
        "You are thankful for the little things that bring joy.",
        "Gratitude grounds you in the present moment.",
        "You recognize beauty in everyday moments.",
        "You are grateful for how far you’ve come.",
        "Every breath is a gift you honor.",
        "You express thanks for all you are and all you have.",
        "You notice the good and let it grow.",
        "Your heart is open to abundance and grace.",
        "You give thanks for your resilience.",
        "Gratitude shifts your focus to the positive.",
        "You appreciate your body, your breath, your being.",
        "You welcome joy through a thankful spirit.",
        "You honor life with presence and appreciation.",
        "Gratitude brings peace to your spirit.",
        "You are thankful for the lessons that shaped you.",
        "You recognize blessings in simple things.",
        "Each day gives you something to be thankful for.",
        "You give thanks for who you are becoming.",
        "You speak gratitude and receive joy.",
        "You radiate appreciation for the world around you."
    ],
    "success": [
        "You are creating the success story you’ve always dreamed of.",
        "You are equipped with everything you need to succeed.",
        "You attract opportunities that align with your vision.",
        "You are proud of your accomplishments and efforts.",
        "You move forward with courage and clarity.",
        "You take inspired action toward your goals.",
        "You believe in your ability to achieve great things.",
        "You rise above fear and self-doubt to reach your goals.",
        "You take bold steps to create the life you want.",
        "Your focus and determination guide you forward.",
        "You welcome success into your life with confidence.",
        "You celebrate your strengths and talents.",
        "You learn from every experience and improve.",
        "You are persistent and never give up.",
        "You are capable of overcoming any obstacle.",
        "You are motivated by your passion and purpose.",
        "You celebrate every step of progress you make.",
        "You trust yourself to navigate obstacles with ease.",
        "You believe success is not only possible—it’s inevitable.",
        "You are grateful for your journey and progress."
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
