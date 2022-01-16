import os
from department_app import app, db
from department_app.models import Department, Employee


# print(dir(models))
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Department': Department, 'Employee': Employee}


if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000

    app.run('localhost', debug=True)
