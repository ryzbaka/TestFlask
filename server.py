from flask import Flask

app= Flask(__name__)

@app.route("/")
def something():
	return "hello"

app.run()
