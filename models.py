from datetime import datetime
from extensions import db

class Employee(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))           
    address = db.Column(db.String(255))        
    # post = db.Column(db.String(50))            
    salary = db.Column(db.Float)               
    department = db.Column(db.String(50))      
    role = db.Column(db.String(50))            
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)
