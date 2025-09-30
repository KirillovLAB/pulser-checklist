from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/section1')
def section1():
    return render_template('section.html', title="Раздел 1", section_id=1)

@app.route('/section2')
def section2():
    return render_template('section.html', title="Раздел 2", section_id=2)

@app.route('/section3')
def section3():
    return render_template('section.html', title="Раздел 3", section_id=3)

@app.route('/section4')
def section4():
    return render_template('section.html', title="Раздел 4", section_id=4)

if __name__ == '__main__':
    app.run(debug=True)
