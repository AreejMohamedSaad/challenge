from flask import Flask
from flask_restful import Api ,Resource
from apis import rest_api 


app = Flask(__name__)
api = Api(app)
api.add_resource(rest_api.test_code,"/test/method")

