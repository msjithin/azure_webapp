from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # db intitialized here
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/task.db"
db.init_app(app)

# db.create_all()

from routes import *

if __name__ == "__main__":
    app.run(debug=True)