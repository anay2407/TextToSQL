import openai
from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3

# Load environment variables
load_dotenv()

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to interact with GPT-3 and get a response
def get_gemini_response(question, prompt):
    prompt_text = prompt[0] + f"\nQ: {question}\nA:"
    
    # Request from OpenAI's GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",  # Replace with your specific model if needed
        prompt=prompt_text,
        max_tokens=150,
        temperature=0.5
    )
    
    return response.choices[0].text.strip()  # Returning the generated response

# Function to retrieve SQL query results from a database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    
    for row in rows:
        print(row)
    
    return rows

# Define the prompt
prompt = [
    """
    You are an expert in converting English questions into SQL queries.
    The database has the name 'STUDENT' and the following columns: 'NAME', 'CLASS', and 'SECTION'.
    
    For example:
    - "How many entries of records are present?" -> SELECT COUNT(*) FROM STUDENT;
    - "Tell me all students studying in Data Science class?" -> SELECT * FROM STUDENT WHERE CLASS = 'Data Science';
    """
]

# Streamlit UI
st.set_page_config(page_title="I Can Retrieve Any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

# User Input
question = st.text_area("Input your question:", key="input")
submit = st.button("Ask the Question")

# When submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("The Generated SQL Query:")
    st.write(response)
    
    # Execute the SQL query and fetch data
    data = read_sql_query(response, 'student.db')
    
    st.subheader("The SQL Response:")
    for row in data:
        st.write(row)
