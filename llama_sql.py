from llama_cpp import Llama

# Path to LLaMA model
model_path = r"C:\Users\91630\.cache\lm-studio\models\hugging-quants\Llama-3.2-1B-Instruct-Q8_0-GGUF\llama-3.2-1b-instruct-q8_0.gguf"

# Load model
print("Loading LLaMA model...")
llm = Llama(model_path=model_path, n_ctx=2048)
print("✅ Model loaded successfully!")

# Function to generate SQL
def generate_sql_query(user_input):
    """Generate an SQL query from natural language input."""
    
    prompt = f"""
    You are an expert in SQL. Convert the following user question into a valid SQL query.

    Database Schema:
    - Employees (ID, Name, Department, Salary, Hire_Date)
    - Departments (ID, Name, Manager)

    ### Examples:
    User: "List employees who have the highest salary"
    SQL: SELECT * FROM Employees WHERE Salary = (SELECT MAX(Salary) FROM Employees);

    User: "List employees hired after 30-05-2023"
    SQL: SELECT * FROM Employees WHERE Hire_Date > '2023-05-30';

    User: "What is the total salary expense for the Engineering department?"
    SQL: SELECT SUM(Salary) FROM Employees WHERE Department = 'Engineering';

    User: "Show employee names with their department managers"
    SQL: SELECT Employees.Name, Departments.Manager FROM Employees 
         JOIN Departments ON Employees.Department = Departments.Name;

    User: "{user_input}"
    SQL:
    """

    response = llm(prompt, max_tokens=200, stop=["User:", "\n\n"], temperature=0.1)
    sql_query = response["choices"][0]["text"].strip()
    
    return sql_query
