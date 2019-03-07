from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    # return jsonify({"yunTask" : task})
    return jsonify(tasks)


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    print(task.__str__())
    if len(task) == 0:
        abort(404)
    return jsonify({'task': tasks[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({'code': 404, 'error': 'Not find!', 'msg': str(error)}),
        404
    )


if __name__ == '__main__':
    app.run()

