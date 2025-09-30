from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Нужно для flash сообщений

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/section1', methods=['GET', 'POST'])
def section1():
    if request.method == 'POST':
        device_number = request.form.get('device_number')
        # Здесь можно сохранить данные в базу данных
        flash(f'Чек-лист ТО-1 для прибора {device_number} сохранен!', 'success')
    return render_template('section.html', title="ТО-1", section_id=1)

@app.route('/section2', methods=['GET', 'POST'])
def section2():
    if request.method == 'POST':
        device_number = request.form.get('device_number')
        flash(f'Чек-лист ТО-2 для прибора {device_number} сохранен!', 'success')
    return render_template('section.html', title="ТО-2", section_id=2)

@app.route('/section3', methods=['GET', 'POST'])
def section3():
    if request.method == 'POST':
        device_number = request.form.get('device_number')
        flash(f'Чек-лист ТО-3 для прибора {device_number} сохранен!', 'success')
    return render_template('section.html', title="ТО-3", section_id=3)

@app.route('/section4', methods=['GET', 'POST'])
def section4():
    if request.method == 'POST':
        device_number = request.form.get('device_number')
        flash(f'Чек-лист ТО-0 для прибора {device_number} сохранен!', 'success')
    return render_template('section.html', title="ТО-0", section_id=4)

if __name__ == '__main__':
    app.run(debug=True)
