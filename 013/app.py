from flask import Flask, render_template, request

from weather import get_local_time, query_api

app = Flask(__name__)


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    data = []
    if request.method == 'POST':
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        data.append(query_api(city1))
        data.append(query_api(city2))
    return render_template("weather.html",
                           data=data,
                           time=get_local_time)


if __name__ == "__main__":
    app.run()
