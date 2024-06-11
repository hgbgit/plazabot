# Plaza Recruitment Chatbot

This project is a recruitment chatbot for Plaza, a VC-backed Brazilian Proptech/Fintech. The chatbot interacts with potential job applicants, collects necessary information, and stores it in a database.

## Features

- Converses with applicants about the open developer position.
- Collects information about the applicant's experience, preferred programming language, willingness to work on-site, willingness to use Ruby, and interview availability.
- Saves the collected information in an SQLite database.

## Prerequisites

- Python 3.6+
- OpenAI API key

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/plaza-recruitment-chatbot.git
   cd plaza-recruitment-chatbot
   ```

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**

   ```bash
   pip install flask openai
   ```

4. **Then run the script to create the database and the necessary table:**

   ```bash
   python database.py
   ```

5. **Run the Flask application**

   ```bash
   python app.py
   ```

6. **Access the application**
   
   Open a web browser and navigate to http://127.0.0.1:5000/.
   