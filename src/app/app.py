from time import sleep

from flask import Flask
from flask_migrate import Migrate
from models.models import db
from routes.routes import blueprint

app = Flask(__name__)

DB_INFO = {
    "USER": "root",
    "PASSWORD": "root",
    "HOST": "db",
    "NAME": "userdb",
}

sleep(10)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"mysql+pymysql://{DB_INFO['USER']}:{DB_INFO['PASSWORD']}@{DB_INFO['HOST']}/{DB_INFO['NAME']}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()
app.register_blueprint(blueprint, url_prefix="/")
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
