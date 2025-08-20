# calculator_backend.py
# You need to install Flask and Flask-Cors:
# pip install Flask Flask-Cors

from flask import Flask, request, jsonify
from flask_cors import CORS
import re

# Initialize the Flask application
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) to allow the frontend
# to communicate with this backend.
CORS(app)

# --- Security Note ---
# Using eval() is extremely dangerous because it can execute arbitrary code.
# For this calculator, we will create a safe evaluation function that only
# allows mathematical operations.

def safe_calculate(expression):
    """
    Safely evaluates a mathematical expression.
    It only allows numbers, and the operators +, -, *, /
    """
    try:
        # 1. Validate the expression to ensure it only contains allowed characters.
        # Allowed: digits 0-9, operators +-*/, and decimal point .
        if not re.match(r"^[0-9+\-*/.\s]+$", expression):
            return "Error: Invalid characters in expression"

        # 2. To prevent other security issues (like very long numbers),
        # we can add more checks, but for a simple calculator, this is a good start.

        # 3. Perform the calculation safely. Python's `eval` is used here
        # but only AFTER the string has been validated. For a production app,
        # you would parse the expression manually or use a dedicated library.
        result = eval(expression)
        return result

    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        # Catch any other potential errors during calculation
        print(f"Calculation error: {e}")
        return "Error: Invalid expression"


@app.route('/calculate', methods=['POST'])
def calculate_endpoint():
    """
    This is the API endpoint that the frontend will call.
    It receives a JSON object with an 'expression' key.
    """
    # Get the JSON data from the incoming request
    data = request.get_json()

    # Check if the 'expression' key exists in the data
    if not data or 'expression' not in data:
        return jsonify({'error': 'Invalid request format'}), 400

    expression = data['expression']
    
    # Use our safe function to calculate the result
    result = safe_calculate(expression)

    # If the result is a string, it's an error message
    if isinstance(result, str) and "Error" in result:
        return jsonify({'error': result}), 400

    # Otherwise, return the successful result
    return jsonify({'result': result})

# This block allows you to run the server directly from the command line
if __name__ == '__main__':
    # Runs the Flask app on http://127.0.0.1:5000
    # The debug=True flag provides helpful error messages during development.
    app.run(debug=True, port=5000)
