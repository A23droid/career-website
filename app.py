from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1, 
    'title': 'Data Analyst',
    'location': 'Bangalore, India', 
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2, 
    'title': 'SDE',
    'location': 'Delhi, India', 
    'salary': 'Rs. 8,50,000'
  },
  {
    'id': 3, 
    'title': 'Data Scientist',
    'location': 'Mumbai, India', 
    'salary': 'Rs. 17,40,000'
  },
  {
    'id': 4, 
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 5, 
    'title': 'Backend Engineer',
    'location': 'San Francisco', 
    'salary': '$120,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host = '0.0.0.0', port = 3000, debug = True)