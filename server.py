from flask import Flask, request, jsonify
import os

app = Flask(__name__)

minecraft_chat = []
roblox_chat = []

ROBLOX_ADMINS = os.getenv("ROBLOX_ADMINS", "").split(",")

@app.route("/minecraft/chat", methods=["POST"])
def minecraft_chat_in():
    data = request.json
    minecraft_chat.append(data)
    if len(minecraft_chat) > 50:
        minecraft_chat.pop(0)
    return jsonify(ok=True)

@app.route("/roblox/chat", methods=["POST"])
def roblox_chat_in():
    data = request.json
    roblox_chat.append(data)
    if len(roblox_chat) > 50:
        roblox_chat.pop(0)
    return jsonify(ok=True)

@app.route("/minecraft/poll")
def minecraft_poll():
    return jsonify(roblox_chat)

@app.route("/roblox/poll")
def roblox_poll():
    return jsonify(minecraft_chat)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
