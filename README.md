### 🧠 Career Advisor Chatbot

This project is an AI-powered Career Advisor Chatbot built using Google Gemini API and Streamlit. It helps students explore career options after their 10th grade by providing clear and concise guidance based on their interests.

### 🚀 Features

💬 Interactive chatbot interface built with Streamlit

🎓 Provides career advice based on user interests (e.g., computers, commerce, arts)

⚡ Uses Gemini 2.5 Flash model for fast and accurate responses

🔐 Secure API key management using .env file

🧠 Context-aware conversation handling with session state

### 🧩 Tech Stack

Python 3.10+

Streamlit – Web interface

Google Gemini API – AI model for conversation

dotenv – Environment variable management

os – For API key setup

### 📂 Project Structure
```
Career-Advisor-Chatbot/
│
├── app.py                # Main Streamlit app file
├── .env                  # Stores your API key (not to be uploaded)
├── requirements.txt       # Required dependencies
├── README.md              # Project documentation
└── screenshots/           # UI images of chatbot (optional)
```
### ⚙️ Setup Instructions
1.Clone the repository
```
git clone https://github.com/yourusername/Career-Advisor-Chatbot.git
cd Career-Advisor-Chatbot
```
2.Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```
3.Install dependencies
```
pip install -r requirements.txt
```
4.Set up environment variables
* Create a .env file in the project root and add:
  ```
  gemini_key=YOUR_GEMINI_API_KEY
  ```
5.Run the chatbot
```
streamlit run app.py
```
6.Open the local URL shown in your terminal (usually http://localhost:8501) to interact with the chatbot.
### 🖼️ Chatbot Screenshots

**Example 1:** Initial Question  
![Career Advisor Chatbot Screenshot 1](./screenshots/Screenshot%20From%202026-02-18%2009-58-15.png)

**Example 2:** Follow-up Response  
![Career Advisor Chatbot Screenshot 2](./screenshots/Screenshot%20From%202026-02-18%2009-58-35.png)

## You Can Try here:
![chat bot](https://k9kcslvx9gytpqfamick53.streamlit.app/)
### 🧑‍💻 Author

#### Salam Shaik
Passionate about building impactful AI projects for students and learners.
