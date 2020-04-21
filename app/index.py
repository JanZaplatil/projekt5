from flask import Flask, render_template, url_for, Markup
import csv



app = Flask(__name__)
 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/video')
def video():
    return render_template('video.html')


@app.route("/blog")
def blog():
  with open('static/vaja_noge_popravljena.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',') 
    first_line = True
    elements = []
    for row in data:
      if not first_line:
        elements.append({
          "hedaer": row[0],
          "img_source": row[1],
          "post": row[2]
        })
      else:
        first_line = False
  return render_template("blog.html", elements=elements)


@app.route('/workout')
def workout():
    return render_template('workout.html')

@app.route('/trainers')
def trainers():
    return render_template('trainers.html')








if __name__ == '__main___':
    app.run()