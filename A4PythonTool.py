from flask import Flask, jsonify, url_for, redirect

app = Flask(__name__)

@app.route('/default', defaults = {'name' : 'Default Event'})
@app.route('/default/<name>')
def default(name):
    return jsonify(name = name,
    date='12-32-2023',
    time='2300')

@app.route('/urls')
def url():
    return redirect(url_for('default', name = 'College'))



app.run(host='0.0.0.0', port = 8080)