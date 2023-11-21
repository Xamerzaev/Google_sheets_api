from core import app, db
from flask_migrate import Migrate, upgrade

migrate = Migrate(app, db)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        upgrade()

    app.run(host="0.0.0.0", debug=True)
