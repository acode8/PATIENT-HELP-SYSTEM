from flask import Flask, render_template, request
from utils.voice import speak
from utils.alerts import send_email, send_sms
from db.database import log_help_request, get_logs

app = Flask(__name__)

messages = {
    "Nurse": "🔔 Need a help of nurse.",
    "Emergency": "🚨 Emergency team !",
    "Water": "🚰 Need of water.",
    "Washroom": "Need assistance .",
    "Meal": "🍽️ Need of meals."
}

@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    if request.method == 'POST':
        help_type = request.form['help']
        response = messages.get(help_type, "Invalid request.")
        
        # Trigger all actions
        speak(response)
        send_email("Patient Help Request", response)
        send_sms(response)
        log_help_request(help_type)
    
    return render_template('index.html', response=response)

@app.route('/admin')
def admin():
    logs = get_logs()
    return render_template('admin.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
from utils.alerts import send_email, send_sms, make_call  # <-- add this

# Inside the POST block
make_call(f"{help_type} help requested")
