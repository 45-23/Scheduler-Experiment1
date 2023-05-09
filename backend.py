from flask import Flask, request, render_template, redirect, url_for, make_response, jsonify

import sqlite3

app = Flask(__name__, template_folder='templates')

connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE IF NOT EXISTS events (id INT, name VARCHAR, date DATE, time TIME)')
cursor = connect.cursor()
cursor.execute('SELECT id, name, date, time FROM events')
events = cursor.fetchall()
#events = []

@app.route('/home')
def index():
	return render_template("test.html")

@app.route('/api/eventData', methods=['post', 'get'])
def json_data():
	
	req = request.get_json()

	print(req)

	res = make_response(jsonify({"message": "JSON received"}), 200)

	return res

@app.route('/')
def home():
	
	#cursor = connect.cursor()
	cursor.execute('SELECT id, name, date, time FROM events')
	events = cursor.fetchall()
	
	return render_template("frontend.html", events = events)
	
@app.route('/about')
def about():
    return 'about'
	
@app.route('/add_event', methods=['post', 'get'])
def add_event():
    #event_name = request.form.get('event name')
    #event_date = request.form.get('event date')
    #event_time = request.form.get('event time')
	event_name = request.form['event name']
	event_date = request.form['event date']
	event_time = request.form['event time']
	
	#event_string = event_name+' on '+event_date+' at '+event_time
	#events.append(event_string)
	
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute("select count(*) from events")
	count = cursor.fetchone()[0] + 1
	cursor.execute("INSERT INTO events (id,name,date,time) VALUES (?,?,?,?)",(count, event_name, event_date, event_time))
	db.commit()
	
	cursor.execute('SELECT id, name, date, time FROM events')
	events = cursor.fetchall()
	
	return render_template("frontend.html", events = events)

@app.route('/edit_event/<int:value>')
def change(value):
    return render_template("edit.html", value = value)
	
@app.route('/change_event/<int:value>', methods=['post'])
def change_event(value):
    
    #new_name = request.form.get('change name')
    #new_date = request.form.get('change date')
    #new_time = request.form.get('change time')
	new_name = request.form['change name']
	new_date = request.form['change date']
	new_time = request.form['change date']
    
    #new_string = new_name+' on '+new_date+' at '+new_time
    #events.pop(value-1)
    #events.insert(value-1, new_string)
	
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute("UPDATE EVENTS SET name=?, date=?, time=? WHERE id=?",(new_name, new_date, new_time, value))
	db.commit()
    
	cursor.execute('SELECT id, name, date, time FROM events')
	events = cursor.fetchall()
	
	return render_template("frontend.html", events = events)

@app.route('/delete_event/<int:value>')
def delete(value):
	
	#events.pop(value-1)
	
	db = sqlite3.connect("database.db")
	cursor = db.cursor()
	cursor.execute("DELETE FROM events WHERE id=?",[value])
	db.commit()
	
	cursor.execute('SELECT id, name, date, time FROM events')
	events = cursor.fetchall()
	
	return render_template("frontend.html", events = events)
	
	return redirect(url_for("frontend.html"))
		
if __name__ == "__main__":
    app.run(debug=True)
