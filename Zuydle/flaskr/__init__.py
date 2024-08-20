import os

from flask import Flask, jsonify, request, session, make_response


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/api/data')
    def get_data():
        data = {'message': 'Hello from the backend!'}
        return jsonify(data)

    @app.route('/api/users', methods=['GET', 'POST'])
    def users():
        if request.method == 'GET':
            # Implement logic to fetch users from the database
         pass
        elif request.method == 'POST':
         # Implement logic to create a new user in the database
         pass

    return app
    
    