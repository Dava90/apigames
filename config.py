from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS

# Initialize app and database connection
app = Flask(__name__)
CORS(app, resources={"/api/*": {"origins": "*"}}, supports_credentials=True)

# Konfigurasi MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://DBgames_slowmostly:f0eaf020bcaa5267fb628881abc90dca806326c8@xzvzg.h.filess.io:3305/DBgames_slowmostly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'test123'
db = SQLAlchemy(app)

app.app_context().push()