from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/student', methods=['GET'])
def student():
    name = request.args.get('name', 'Guest')
    return jsonify(message=f"Hello, {name}! Welcome to the Flask application.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
