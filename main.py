
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/lesson/<int:lesson_id>')
def lesson(lesson_id):
    return render_template('lesson_content.html', lesson_id=lesson_id)

if __name__ == '__main__':
    app.run(debug=True)
