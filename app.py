import quandl
from flask import Flask,render_template,request,redirect
import pandas as pd
from bokeh.charts import Line
from bokeh.plotting import figure,output_file
from bokeh.embed import components
from bokeh.resources import CDN
import requests
app = Flask(__name__)



def plotit(x):
  quandl.ApiConfig.api_key = 'SH7sRjQUFq5Vnwg46PUj'
  quandl.ApiConfig.api_version = '2015-04-09'
  data = quandl.get("WIKI/%s" %x)
  plot=figure()
  x=data[0:30].ix[:,'Close']
  pl=Line(x,title='Closing stock for last month')
  script,div= components(pl)
  return script,div

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
 if request.method == 'GET':
    return render_template('index.html')
 else:
    s = request.form['ticker'].upper()
    script,div = plotit(s)
    return render_template('graph.html', script=script, div=div)



if __name__ == '__main__':
 app.run(port=33507)
