from flask import Flask, jsonify, request
from phone import track_number
from flask_cors import CORS

# Create a Flask app instance
app = Flask(__name__)
CORS(app)

@app.route('/', methods=["POST"])
def hello_world():
    # Verify if it's a POST request
    if request.method == 'POST':
        print("phasse-one")
        # Get data from query parameters
        data = request.get_json()
        print(data)
        number = data.get('number')
        country = data.get('country')
        print(country)
        # Check if the required parameters are present
        
        data = track_number(number , country)
        
      

        # Return a JSON response with the received data
        return jsonify({"message": "Data received", 'data' : data}), 200
    else:
        return jsonify({"error": "Invalid method"}), 405

# Main driver function
if __name__ == '__main__':
    # Run the app on the local development server
    app.run(debug=True, host='0.0.0.0', port=5000)
