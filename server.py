import os
import sqlite3
from flask import Flask, request, jsonify, render_template
from llama_sql import generate_sql_query  # Ensure this function is correct

app = Flask(__name__, template_folder="templates")

DATABASE = "company.db"  # Ensure this is the correct database file

def connect_db():
    """Connect to the SQLite database."""
    db_path = os.path.abspath(DATABASE)
    print(f"📌 Using database at: {db_path}")  # Debugging: Print the database path
    return sqlite3.connect(DATABASE)

@app.route("/")
def home():
    """Serve the UI."""
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def get_sql_query():
    """Generate an SQL query from a natural language query."""
    data = request.get_json()
    
    if not data or "query" not in data:
        return jsonify({"error": "Invalid request. Please provide a 'query' field."}), 400
    
    sql_query = generate_sql_query(data["query"])  # Convert user query to SQL
    print(f"✅ Generated SQL: {sql_query}")  # Debugging log
    return jsonify({"sql": sql_query})

@app.route("/execute", methods=["POST"])
def execute_sql():
    """Execute the generated SQL query and return results."""
    data = request.get_json()
    sql_query = data.get("sql", "").strip()

    if not sql_query:
        return jsonify({"error": "No SQL query provided"}), 400

    print(f"🔍 Executing SQL: {sql_query}")  # Debugging log

    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Ensure only SELECT queries are executed (prevent database modifications)
        if not sql_query.lower().startswith("select"):
            return jsonify({"error": "Only SELECT queries are allowed"}), 400

        cursor.execute(sql_query)
        rows = cursor.fetchall()

        # If cursor.description exists, extract column names
        column_names = [desc[0] for desc in cursor.description] if cursor.description else []

        conn.close()

        # Format results as JSON
        results = [dict(zip(column_names, row)) for row in rows]
        print(f"✅ Query Results: {results}")  # Debugging log
        return jsonify({"results": results})

    except Exception as e:
        print(f"❌ Error: {str(e)}")  # Debugging log
        return jsonify({"error": str(e)}), 500

@app.route("/structure", methods=["GET"])
def get_db_structure():
    """Return the database schema (table names and columns)."""
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        db_structure = []

        for table in tables:
            table_name = table[0]
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

            column_info = [{"name": col[1], "type": col[2]} for col in columns]
            db_structure.append({"name": table_name, "columns": column_info})

        conn.close()

        return jsonify({"tables": db_structure})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print(f"🚀 Server running on http://127.0.0.1:5000/")
    app.run(debug=True, host="0.0.0.0", port=5000)
