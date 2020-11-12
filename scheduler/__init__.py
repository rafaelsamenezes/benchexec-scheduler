import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "scheduler.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    db_file = app.config.get('DATABASE', 'scheduler.sqlite2')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file}'    
    app.config['APPLICATION_ROOT'] = app.config.get('APPLICATION_ROOT', '/')
    

    import scheduler.models.machine
    import scheduler.models.job
    import scheduler.models.job_run
    from scheduler.models.db import db
    db.init_app(app)
    db.create_all(app=app)

    # apply the blueprints to the app
    from scheduler.controller import machine, job, job_run, web

    app.register_blueprint(machine.bp)
    app.register_blueprint(job.bp)
    app.register_blueprint(job_run.bp)
    app.register_blueprint(web.bp)

    app.add_url_rule("/", endpoint="index")

    return app
