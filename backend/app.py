from flask import Flask, request, jsonify, send_file; from flask_cors import CORS; import os; import utils.utils as utils; app = Flask(__name__); CORS(app);
from flask_socketio import SocketIO, emit

# Initialize Flask-SocketIO
ws = SocketIO(app, cors_allowed_origins="*")

@app.route("/logs", methods=["POST"])
def post_logs():
  logs = request.get_json()['logs'] # string
  utils.wa(logs, 'logs.txt')
  ws.emit("logs", logs)
  return {"status": "ok", "logged": logs}, 200

@app.route("/logs", methods=["GET"])
def get_logs():
  logs = utils.rl('logs.txt')[::-1]
  return jsonify({"logs": logs}), 200

if __name__ == '__main__':
  app.run(debug=False)
