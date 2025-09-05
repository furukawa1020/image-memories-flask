from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# 名前と日付を保存するリスト
history_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # フォームから名前と日付を取得
        name = request.form.get('name')
        date = request.form.get('date')

        # 入力が空でないかを確認
        if name and date:
            # データを保存
            history_data.append({'name': name, 'date': date})
            return redirect(url_for('view_history'))

    return render_template('index.html')

@app.route('/history')
def view_history():
    # 同じ名前の人の入力回数をカウント
    name_count = {}
    for entry in history_data:
        name = entry['name']
        if name in name_count:
            name_count[name] += 1
        else:
            name_count[name] = 1

    # 今日の日付に入力されたデータを取得
    today = datetime.now().strftime('%Y-%m-%d')
    today_entries = [entry for entry in history_data if entry['date'] == today]

    return render_template('history.html', history=history_data, name_count=name_count, today_entries=today_entries)

if __name__ == '__main__':
    app.run(debug=True)

    
