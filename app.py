from flask import Flask

from helper.database import db, migrate
from helper.api import api, blueprint
from helper.cors import cors

app = Flask(__name__) 

api.init_app(app)
cors.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:post@localhost:5432/todos"
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)