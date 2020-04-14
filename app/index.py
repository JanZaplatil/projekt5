from flask import Flask, render_template, url_for
import csv



app = Flask(__name__)
 

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/blog')
def blog():
    with open('static/clanek_noge_noge.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        paragraphs = []
        for row in data:
            if not first_line:
                paragraphs.append({
                    "para":row[0]
                })
            else:
                first_line = False
        return render_template("blog.html", paragraphs=paragraphs)

@app.route('/workout')
def workout():
    return render_template('workout.html')

@app.route('/video')
def video():
    return render_template('video.html')







if __name__ == '__main___':
    app.run()