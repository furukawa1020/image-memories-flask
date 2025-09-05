from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

static_image_dir = os.path.join('static', 'images')
# 名前・日付・画像ファイル名を保存するリスト
history_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    # static/images/配下の画像一覧を取得
    images = [f for f in os.listdir(static_image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        image = request.form.get('image')
        if name and date and image:
            history_data.append({'name': name, 'date': date, 'image': image})
            return redirect(url_for('view_history'))

    return render_template('index.html', images=images)

@app.route('/history')
def view_history():
    name_count = {}
    for entry in history_data:
        name = entry['name']
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

    today = datetime.now().strftime('%Y-%m-%d')
    today_entries = [entry for entry in history_data if entry['date'] == today]

    return render_template('history.html', history=history_data, name_count=name_count, today_entries=today_entries)

if __name__ == '__main__':
    app.run(debug=True)

    
