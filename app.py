from urllib import response
from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS

app=Flask(__name__)
api=Api(app)

CORS(app)

identitas={}

class TestingSource(Resource):
    def get(self):
        #response={"msg":"Success Build Rest Api"}
        return identitas

    def post(self):
        nama=request.form["nama"]
        umur=request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response={"msg":"Success add data"}
        return response

api.add_resource(TestingSource, "/first", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)