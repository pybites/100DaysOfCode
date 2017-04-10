from pprint import pprint as pp

from flask import Flask, render_template, request

from weather import get_local_time, query_api

app = Flask(__name__)


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    data = []
    error = None
    if request.method == 'POST':
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        for c in (city1, city2):
            resp = query_api(c)
            pp(resp)
            if resp:
                data.append(resp)
        if len(data) != 2:
            error = 'Did not get complete response from Weather API'
    return render_template("weather.html",
                           data=data,
                           error=error,
                           time=get_local_time)


if __name__ == "__main__":
    app.run()
