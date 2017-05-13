from flask import Flask, render_template, request
import datetime
import getDBdate
import pygal

name = {0,0}
date1 = 0
units = 'Celsius'

def makeGraph():
    global date1
    global units
    try:
		graph = pygal.Line()
		graph.x_labels = getDBdate.getTime()
		graph.add('Humidity',  getDBdate.getHumid())
                if units == 'Celsius':
                    graph.add('tempC',    getDBdate.getTemp(0))
		else:
                    graph.add('tempF',     getDBdate.getTemp(1))
		graph_data = graph.render_data_uri()
		return graph_data
    except Exception, e:
		return(str(e))

app = Flask(__name__)
@app.route("/")
def hello():
 now = datetime.datetime.now()
 timeString = now.strftime("%Y-%m-%d %H:%M")
 getDBdate.getData("05/07/17")
 c, h = getDBdate.getCurrent()
 templateData = {
  'title' : 'Box 1',
  'time': timeString,
  'temp': c,
  'hum': h
  }
 return render_template('main.html', **templateData)

@app.route("/history.html")
def history():
        return render_template('history.html')
@app.route("/history.html", methods=["POST"])
def history_request():
    global date1
    global units
    tempType = 0
    date1 = request.form['mon1']
    date1 += '/'
    date1 += request.form['day1']
    date1 += '/'
    date1 += request.form['year1']
    units = request.form['Units']
    if units == 'Celsius':
        tempType = 0
    if units == 'Fahrenheit':
        tempType = 1
    getDBdate.getData(date1)
    times = getDBdate.getTime()
    temps = getDBdate.getTemp(tempType)
    humids = getDBdate.getHumid()
    graph_data = makeGraph()
    templateData = {
        'firstbound': date1,
        'Units': units,
        'graph_data': graph_data
        }
    return render_template('history_displayed.html', **templateData)
@app.route("/getInfo/<val>")
def info(val):
 now = datetime.datetime.now()
 if (val=="time"):
  timeString = now.strftime("%H:%M")
  templateData = { 'title' : 'Time on this Pi',
   'name':'The Time is',
   'datetime': timeString}
 if (val=='date'):
  timeString = now.strftime("%Y-%m-%d")
  templateData = { 'title' : 'Date on this Pi',
   'name':'The Date is',
   'datetime': timeString}
  return render_template('date_time.html', **templateData)
if __name__ == "__main__":
 app.run(host='0.0.0.0', port=481, debug=True)

