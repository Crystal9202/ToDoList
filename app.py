from flask import Flask
from flask_restful import Api,Resource

app=Flask(__name__)
api=Api(app)

class Helloworld(Resource):
    def get(self):
        return {'data':'Hello,world'}

class Helloname(Resource):
    def get(self,name):
        return {'data':f'Hello,{name}'}

api.add_resource(Helloworld, '/helloworld')
api.add_resource(Helloname, '/helloname/<string:name>')



