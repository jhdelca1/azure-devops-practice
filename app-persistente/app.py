from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_FILE = "/data/storage.txt"

@app.route("/", methods=["GET"])
def read_data():
    try:
        with open(DATA_FILE, "r") as file:
            content = file.read()
        return jsonify({"message": "Contenido del archivo", "data": content})
    except FileNotFoundError:
        return jsonify({"message": "Archivo vacío", "data": ""})

@app.route("/", methods=["POST"])
def write_data():
    data = request.json.get("text", "")
    with open(DATA_FILE, "a") as file:
        file.write(data + "\n")
    return jsonify({"message": "Datos guardados correctamente!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

