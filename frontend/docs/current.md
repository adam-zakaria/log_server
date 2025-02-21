The thing about json is that it doesn't preserve format so I need to parse each string as a new line, not a big deal but maybe extra work?

Create a web app which is a log server. the server should receive post requests with a log text and append it to 'log.txt'. The client should GET the log.txt on load and open a websocket to get updates to log.txt. The log lines should be displayed in reverse.

the logs are line separated.txt, and are sent to client as json. {'logs': logs}
The json is a reversed list of lines.
Client should parse the list and display the lines.
i.e.
.json()).then((json)=>
  json.forEach((el) => prepend(el))

Create a "/logs" POST endpoint which accepts a string called logs which are the logs and appends the string to log.txt and publishes the string on a websocket channel called logs.

Fix my example.

import flask-socketio
ws = flask-socketio()
@app.route("/logs", method=["POST"])
def post_logs():
  logs = request.get_json()['logs'] # string
  utils.a(logs, 'log.txt')
  ws.emit("logs", logs, broadcast=True)
  return {"status": "ok", "logged": logs}, 200

Okay this seems to be working..

So...now we want to test the logging with twitch...
