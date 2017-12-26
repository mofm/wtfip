from flask import Flask
from flask import request
from flask import render_template
import pygeoip

app = Flask(__name__)
gi = pygeoip.GeoIP('data/GeoLiteCity.dat', pygeoip.MEMORY_CACHE)

@app.route('/')
@app.route('/home')
def home():
    geo_data = gi.record_by_addr(request.remote_addr)
    return render_template('home.html', geo_data=geo_data)


if __name__ == '__main__':
    app.run()