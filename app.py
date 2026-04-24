from flask import Flask, render_template, request
import requests

app = Flask(__name__)

secret_key = "your_secret_key"
app.secret_key = secret_key

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    data = response.json()

    temp = data["current_condition"][0]["temp_C"]
    weather = data["current_condition"][0]["weatherDesc"][0]["value"]

    return temp, weather

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None

    if request.method == "POST":
        city = request.form.get("city")
        temp, weather = get_weather(city)

        condition = None

        if int(temp) < 39 and  int(temp) > 0:
            condition = "Good you can go outside"
        else:
            condition = "Bad you should stay home"
            
            
        

        weather_data = {
            "city": city,
            "temp": temp,
            "weather": weather,
            "condition": condition
        }

      


    return render_template("index.html", data=weather_data)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
