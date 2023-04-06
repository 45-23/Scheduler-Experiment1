from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

events = []

@app.route('/')
def home():
    return 'home'
	
@app.route('/about')
def about():
    return 'about'
	
@app.route('/submit_event', methods=['POST', 'GET'])
def submit_event():
    event_name = request.form.get('event name')
    event_date = request.form.get('event date')
    event_time = request.form.get('event time')
	
    event_string = event_name+' on '+event_date+' at '+event_time
    events.append(event_string)
	#return event_name+' on '+event_date+' at '+event_time
    #return render_template("frontend.html", event = event_string)	
    return render_template("frontend.html", events = events)
    
if __name__ == "__main__":
    app.run(debug=True)