from flask import Flask, render_template,request,jsonify
import pandas as pd

#Read cleaned data
df = pd.read_csv("cleaned_covid_data.csv", parse_dates=['date'])

#Create app.py with a root route ('/') that renders templates/index.html.
app=Flask(__name__)

#Pass a small summary (countries list, date range) from Flask to the template.
@app.route('/')
def index():

  country=request.args.get('country',df['country'].iloc[0]) #default use the 1st country
  metric = request.args.get('metric', 'new_cases') #default metric is new_cases

  valid_metrics = ['new_cases', 'new_vaccinations', 'new_deaths','vaccinations_per_hundred','cases_per_million','population']

  if metric not in valid_metrics:
    metric = 'new_cases'

  return render_template("index.html",
                         countries=df['country'].unique(),
                         start_date=df['date'].min(),
                         end_date=df['date'].max(),
                         selected_country=country, 
                         metric=metric)

#Add a route like /data?country=Canada&metric=new_cases that returns JSON (pandas →.to_dict()).
@app.route('/data')
def indexData():
  country=request.args.get('country',df['country'].iloc[0])
  metric = request.args.get('metric', 'new_cases')

  filtered_df = df[df['country'] == country].sort_values('date')

  return jsonify({
        "dates": filtered_df['date'].astype(str).tolist(),
        "values": filtered_df[metric].fillna(0).tolist()
  })

if __name__=="__main__":
  app.run(debug=True)