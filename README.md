# SQLite Chatbot with Llama 3

This is a **Flask-based chatbot** that generates **SQL queries** from natural language input using **Llama 3** and executes them on an SQLite database.

## 📌 Features
- Converts user queries into **SQL commands** using **Llama 3**.
- Executes queries on an **SQLite database**.
- Displays query results in a **Flask-based UI**.

## 🛠️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/shanmukha2003/sqlite_chatbot.git
cd sqlite_chatbot


2️⃣ Create a virtual environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install dependencies

pip install -r requirements.txt


4️⃣ Set up the SQLite database

python database_setup.py  # Creates tables in company.db

5️⃣ Run the server

python server.py

🚀 Usage
Open http://127.0.0.1:5000 in your browser.
Enter your natural language query (e.g., "List all employees in the Sales department").
View the generated SQL query and its results.
