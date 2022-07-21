from flask import Flask
from flask_restful import Api ,Resource 

class test_code(Resource):
    def get(self):
        return {"test_method":"get_request"}

    def post(self):
        return "added"
    def delete(self,id):
        return 204 

    def put(self,id):
        return 201
