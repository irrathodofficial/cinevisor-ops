from flask import Flask, render_template, request
from core.agent import CineVisorAgent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize our custom AI Agent Module
agent = CineVisorAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    agent_output = None
    error_msg = None
    user_query = ""

    if request.method == 'POST':
        user_query = request.form.get('query', '').strip()
        
        if not user_query:
            error_msg = "Please enter a valid infrastructure query."
        else:
            # Call the separated logic from core/agent.py
            output, error = agent.execute_infrastructure_query(user_query)
            if error:
                error_msg = error
            else:
                agent_output = output

    # Flask automatically looks inside the 'templates' folder for index.html
    return render_template('index.html', output=agent_output, error=error_msg, query=user_query)

if __name__ == '__main__':
    # Run the enterprise server
    app.run(host='0.0.0.0', port=5000, debug=True)