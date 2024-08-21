from flask import Flask, jsonify, request 
from app import app, db 
from app.models import Item

@app.route('/api/users', methods=['GET', 'POST'])
def users():
        if request.method == 'GET':
            # Implement logic to fetch users from the database
         pass
        elif request.method == 'POST':
         # Implement logic to create a new user in the database
         pass
