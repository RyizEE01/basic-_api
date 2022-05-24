from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import users_models
from db import create_table_students
import students_models


app = Flask(__name__)
CORS(app)

@app.route('/students', methods=['GET'])
def get_students():
    try:
        result = students_models.get_students()
        data = {
            
            'status': 200,
            'data': result
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/students/<id>', methods=['GET'])
def get_students_by_id(id):
    try:
        result = students_models.get_students_by_id(id)
        data = {
            
            'status': 200,
            'data': result
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
        
    
@app.route('/students', methods=['POST'])
def insert_students():
    students_details = request.json
    nim = students_details['nim']
    nama = students_details['nama']
    jurusan = students_details['jurusan']
    alamat = students_details['alamat']
    try:
        result = students_models.insert_students(nim, nama, jurusan, alamat)
        data = {
            
            'status': 201,
            'message': 'Success!'
            
        }
        resp = jsonify(data)
        resp.status_code = 201
        
        return resp
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
    
    
@app.route('/students/<id>', methods=['PUT'])
def update_students(id):
    students_details = request.json
    id = students_details['id']
    nim = students_details['nim']
    nama = students_details['nama']
    jurusan = students_details['jurusan']
    alamat = students_details['alamat']
    try:
        result = students_models.update_students(id, nim, nama, jurusan, alamat)
        data = {
            
            'status': 200,
            'message': 'Success!'
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/students/<id>', methods=['DELETE'])
def delete_students(id):
    try:
        result = students_models.delete_students(id)
        data = {
            
            'status': 200,
            'message': 'Success!'
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/students/all', methods=["GET"])
def get_students_all_join():
    try:
        result = students_models.get_students_all_join()
        data = {
            
            'status': 200,
            'data': result
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
    
@app.route('/students/all/<students_id>', methods=["GET"])
def get_students_by_id_join(students_id):
    try:
        result = students_models.get_students_by_id_join(students_id)
        data = {
            
            'status': 200,
            'data': result
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/users', methods=["GET"])
def get_users():
    try:
        result = users_models.get_users()
        data = {
            
            'status': 200,
            'data': result
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/users/<id>', methods=["GET"])
def get_users_by_id(id):
    try:
        result = users_models.get_users_by_id(id)
        data = {
            
            'status': 200,
            'data': result
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
    
@app.route('/users', methods=["POST"])
def insert_users():
    users_details = request.json
    username = users_details['username']
    password = users_details['password']
    students_id = users_details['students_id']
    try:
        result = users_models.insert_users(username, password, students_id)
        data = {
            
            'status': 201,
            'message': 'Success!'
            
        }
        resp = jsonify(data)
        resp.status_code = 201
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/users/<id>', methods=["PUT"])
def update_users(id):
    users_details = request.json
    id = users_details['id']
    username = users_details['username']
    password = users_details['password']
    students_id = users_details['students_id']
    try:
        result = users_models.update_users(id, username, password, students_id)
        data = {
            
            'status': 200,
            'message': 'Success!'
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/users/<int:id>', methods=["DELETE"])
def delete_users(id):
    try:
        result = users_models.delete_users(id)
        data = {
            
            'status': 200,
            'message': 'Success!'
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        return resp
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/users/all', methods=["GET"])
def get_users_all_join():
    try:
        result = users_models.get_users_all_join()
        data = {
            
            'status': 200,
            'data': result
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/users/all/<students_id>', methods=["GET"])
def get_users_by_id_join(students_id):
    try:
        result = users_models.get_users_by_id_join(students_id)
        data = {
            
            'status': 200,
            'data': result
            
        }
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
            
            'status': 404,
            'message': "Data Not Found"
            
        }
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        
            'status': 404,
            'message': 'Not Found: ' + request.url
            
        }
    
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp

if __name__ == '__main__':
    app.run(debug=True)