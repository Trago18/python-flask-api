from flask import Flask, jsonify, request
from json import loads
app = Flask(__name__)

todos = [
    { "label": "Sample", "done": True }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)
    
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    data = loads(request_body)
    # print(data)
    todos.append(data)
    # print(todos)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position-1)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)