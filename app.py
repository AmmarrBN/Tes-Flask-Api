import re
from urllib import response
from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from fake_useragent import UserAgent
import os

app=Flask(__name__)
api=Api(app)

CORS(app)

db = SQLAlchemy(app)

basedir=os.path.dirname(os.path.abspath(__file__))
database="sqlite:///" + os.path.join(basedir,"db.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = database

class ViewData(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nama=db.Column(db.String(100))
    umur=db.Column(db.Integer)
    token=db.Column(db.TEXT)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

db.create_all()

identitas={}

class TestingSource(Resource):
    def get(self):
        #response={"msg":"Success Build Rest Api"}
        useragent=UserAgent()
        ua=useragent.random
        query=ViewData.query.all()
        output=[
            ({
                "id":data.id,
                "nama":data.nama,
                "umur":data.umur,
                "token":data.token
            }) 
            for data in query
        ]
        response=({
            "code" : 200,
            "mssg" : "Query data success",
            "data" : output
        })
        return response, 200

    def post(self):
        dataNama=request.form["nama"]
        dataUmur=request.form["umur"]
        dataToken=request.form["token"]

        model=ViewData(nama=dataNama,umur=dataUmur,token=dataToken)
        model.save()

        response=({
            "msg" : "Success add data",
            "code": 200
        })
        return response, 200
    def delete(self):
        query=ViewData.query.all()
        for data in query:
            db.session.delete(data)
            db.session.commit()

        response={
            "mssg": "Success delete all data",
            "reponse code": 200
        }

        return response, 200


class UpdateSource(Resource):
    def put(self,id):
        query=ViewData.query.get(id)
        editNama = request.form["nama"]
        editUmur=request.form["umur"]
        editToken=request.form["token"]

        query.nama = editNama
        query.umur = editUmur
        query.token = editToken

        response={
            "mssg": "Success Edit Data",
            "code": 200
        }

        return response

    def delete(self,id):
        queryData=ViewData.query.get(id)

        db.session.delete(queryData)
        db.session.commit()

        response={
            "mssg": "Success delete data",
            "code": 200
        }

        return response

class RandomUa(Resource):
    def get(self):
        useragent=UserAgent()
        ua=useragent.random
        return ({
            "user-agent": ua,
            "response code": 200,
            "creator": "Ammar-Excuted"
        })

api.add_resource(TestingSource, "/first", methods=["GET", "POST", "DELETE"])
api.add_resource(UpdateSource, "/first/<id>", methods=["PUT","DELETE"])
api.add_resource(RandomUa, "/first/api/user-agent", methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)