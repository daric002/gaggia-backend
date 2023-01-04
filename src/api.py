from flask import Flask
import redis

app = Flask(__name__)
red = redis.Redis()
red.mset({"temperature_goal":95})


@app.route("/")
def hello_world():
    return "Hello World", 200

@app.route('/temperature')
def get_current_temperature():
    return red.get("temperature"), 200

@app.route('/temperature-goal')
def get_temperature_goal():
    return red.get("temperature_goal"), 200

@app.route('/temperature-goal/<new_temp>', methods=["POST"])
def set_temperature(new_temp):
    temperature_goal = int(new_temp)
    red.set("temperature_goal", temperature_goal)
    return "New temperature set", 200


if __name__ == '__main__':
   app.run(debug = True)