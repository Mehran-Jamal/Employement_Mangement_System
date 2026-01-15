from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from extensions import db
from models import Employee
from schemas import EmployeeSchema

employee_bp = Blueprint("employees", __name__)
schema = EmployeeSchema()


@employee_bp.route("/api/employees/", methods=["POST"])
@jwt_required()
def create_employee():
    data = request.json
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    if Employee.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already exists"}), 400

    emp = Employee(**data)
    db.session.add(emp)
    db.session.commit()

    return jsonify(schema.dump(emp)), 201



@employee_bp.route("/api/employees/", methods=["GET"])
@jwt_required()
def list_employees():
    page = request.args.get("page", 1, type=int)       
    department = request.args.get("department")        
    role = request.args.get("role")                   

    query = Employee.query
    if department:
        query = query.filter_by(department=department)
    if role:
        query = query.filter_by(role=role)

    pagination = query.paginate(page=page, per_page=10, error_out=False)
    
    return jsonify({
        "total": pagination.total,                     
        "page": page,                                  
        "employees": schema.dump(pagination.items, many=True)  
    })



@employee_bp.route("/api/employees/<int:id>/", methods=["GET"])
@jwt_required()
def get_employee(id):
    emp = Employee.query.get(id)

    if not emp:
        return jsonify({
            "message": f"Employee with id {id} not present"
        }), 404

    return jsonify(schema.dump(emp)), 200


@employee_bp.route("/api/employees/<int:id>/", methods=["PUT"])
@jwt_required()
def update_employee(id):
    emp = Employee.query.get_or_404(id)
    data = request.json

    if "email" in data and data["email"] != emp.email:
        if Employee.query.filter_by(email=data["email"]).first():
            return jsonify({"error": "Email already exists"}), 400

    for key, value in data.items():
        setattr(emp, key, value)

    db.session.commit()

    return jsonify(schema.dump(emp))

@employee_bp.route("/api/employees/<int:id>/", methods=["DELETE"])
@jwt_required()
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    return "", 204
