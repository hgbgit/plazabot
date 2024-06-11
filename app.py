from flask import Flask, request, jsonify, render_template, session
import openai
import sqlite3
from database import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'

openai.api_key = 'sk-proj-EzZEOQuI8rpaj3gh6YDhT3BlbkFJKVHEhh63xCYzq0dnzDAB'

init_db()

SYSTEM_MESSAGE = """You are a helpful assistant and a recruiter for Plaza. 
You should only talk about the open developer position and its requirements. 
Do not discuss anything else. Always be polite and concise."""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    if 'applicant_data' not in session:
        session['applicant_data'] = {
            'years_of_experience': None,
            'favorite_programming_language': None,
            'willing_to_work_onsite': None,
            'willing_to_use_ruby': None,
            'interview_date': None
        }

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify({"response": response.choices[0].message['content'].strip()})

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    session['applicant_data'].update(data)
    
    # Check if all data is collected
    if all(value is not None for value in session['applicant_data'].values()):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO applicants (years_of_experience, favorite_programming_language, willing_to_work_onsite, willing_to_use_ruby, interview_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (session['applicant_data']['years_of_experience'], session['applicant_data']['favorite_programming_language'], session['applicant_data']['willing_to_work_onsite'], session['applicant_data']['willing_to_use_ruby'], session['applicant_data']['interview_date']))
        conn.commit()
        conn.close()
        session.pop('applicant_data')
        return jsonify({"status": "success"})
    return jsonify({"status": "incomplete"})

if __name__ == '__main__':
    app.run(debug=True)
