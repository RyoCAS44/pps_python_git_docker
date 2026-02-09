from flask import Flask, jsonify, request
from bayeta import frotar, añadir_frases

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hola, mundo"

@app.route("/frotar/<int:n_frases>", methods=["GET"])
def frotar_endpoint(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases), 200

@app.route("/frotar/add", methods=["POST"])
def add_frases():
    data = request.get_json()

    if not data or "frases" not in data:
        return jsonify({"error": "Formato JSON inválido. Se espera una clave 'frases'."}), 400

    if not isinstance(data["frases"], list):
        return jsonify({"error": "'frases' debe ser una lista"}), 400

    añadir_frases(data["frases"])
    return jsonify({"status": "Frases añadidas correctamente"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
