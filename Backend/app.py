from flask import Flask, jsonify
from flask_migrate import Migrate
from setting import db
from model import Company_list
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bragadeesh:bragadeesh%4016@localhost/companylist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

default_data = [
    {"Company_name": "Google", "Status": "active", "Clicks": 100, "Cost": 1200, "Impressions": 300},
    {"Company_name": "Facebook", "Status": "paused", "Clicks": 150, "Cost": 2150, "Impressions": 350},
    {"Company_name": "Twitter", "Status": "active", "Clicks": 200, "Cost": 3400, "Impressions": 400},
    {"Company_name": "LinkedIn", "Status": "paused", "Clicks": 250, "Cost": 3650, "Impressions": 450},
    {"Company_name": "Instagram", "Status": "active", "Clicks": 300, "Cost": 6400, "Impressions": 500},
    {"Company_name": "Snapchat", "Status": "paused", "Clicks": 350, "Cost": 4750, "Impressions": 550},
    {"Company_name": "Pinterest", "Status": "active", "Clicks": 400, "Cost": 5900, "Impressions": 600},
    {"Company_name": "Reddit", "Status": "paused", "Clicks": 450, "Cost": 5050, "Impressions": 650},
    {"Company_name": "YouTube", "Status": "active", "Clicks": 500, "Cost": 6500, "Impressions": 700},
    {"Company_name": "TikTok", "Status": "paused", "Clicks": 550, "Cost": 6570, "Impressions": 750}
]

@app.before_request
def seed_data():
    db.create_all()
    if Company_list.query.count() == 0:
        for entry in default_data:
            db.session.add(Company_list(**entry))
        db.session.commit()
        print("Initial data inserted.")
    else:
        print("Data already exists.")

@app.route("/dashboard")
def dashboard():
    companies = Company_list.query.all()
    return jsonify([
        {
            "Company_name": c.Company_name,
            "Status": c.Status,
            "Clicks": c.Clicks,
            "Cost": c.Cost,
            "Impressions": c.Impressions
        } for c in companies
    ])

if __name__ == "__main__":
    app.run(debug=True)
