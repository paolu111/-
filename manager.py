from apps import crete_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps.models import db

app = crete_app('apps.config_file.DevConfig')
manager = Manager(app=app)
migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    print(app.url_map)
    manager.run()