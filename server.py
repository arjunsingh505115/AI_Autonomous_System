from flask import Flask, request, jsonify
import os

app = Flask(__name__)
INBOX_FILE = "inbox/commands.txt"

@app.route("/send-command", methods=["POST"])
def send_command():
    data = request.json
    command = data.get("command")
    if command:
        with open(INBOX_FILE, "a") as f:
            f.write(command + "\n")
        return jsonify({"message": "✅ Command Received!", "command": command})
    return jsonify({"error": "⚠️ No command provided"}), 400

@app.route("/get-commands", methods=["GET"])
def get_commands():
    if os.path.exists(INBOX_FILE):
        with open(INBOX_FILE, "r") as f:
            commands = f.readlines()
        return jsonify({"commands": [cmd.strip() for cmd in commands]})
    return jsonify({"commands": []})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
