from flask import Flask
from flask_script import Manager
import logging

app = Flask(__name__)
manager = Manager(app)


def configure_app():
    from config import key
    app.secret_key = key.secret_key
    from config.config import config_dict
    app.config.update(config_dict)
    if not app.debug:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)


def configured_app():
    configure_app()
    return app

@manager.command
def server():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    '''+``TEMPLATES_AUTO_RELOAD``         
    Flask checks if template was modified each
 +  time it is requested and reloads it if
 +  necessary. But disk I/O is costly and it may
 +  be viable to disable this feature by setting
 +  this key to ``False``. This option does not
 +  affect debug mode.'''
    app.jinja_env.auto_reload = True
    config = dict(
            debug=True,
            host='0.0.0.0',
            port=8001,
    )
    app.run(**config)


if __name__ == '__main__':
    configure_app()
    manager.run()
