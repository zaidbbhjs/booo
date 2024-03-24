import os,sys
#os.system("pip install fastapi")
#os.system("pip install uvicorn")
from fastapi import Response
import requests
import os
import random,requests
import uvicorn,time
from fastapi import Request
import json
from user_agent import generate_user_agent
from fastapi.responses import JSONResponse
from fastapi import FastAPI
import secrets
app = FastAPI()
import requests
import requests , time,random
from json import dumps
r = requests.session()
a=int(0)
from fastapi import FastAPI, UploadFile
from secrets import token_hex
import uuid,secrets
cok = token_hex(8) * 2
uuid = str(uuid.uuid4())
app = FastAPI()
@app.get('/api/gmail/{gmail}')
async def ga(gmail):
    global cok,uuid
    email=gmail
    r = requests.post("https://mailcheck.co/api/checkMail", data={'email': email})
    r = r.json()['smtpExists']
    if True == r:
    
    		
    		data2={
    		"email":f"{gmail}",
    		"status":"Bad",
    		"Dev":"Marko_Bots",
    		}
    		return JSONResponse(content=data2)
    elif False==r:
    		dta={
    		"email":f"{gmail}",
    		"status":"Hit",
    		"Dev":"Marko_Bots",
    		}
    		return JSONResponse(content=dta)
    else:
    	dta={
    		"email":f"{gmail}",
    		"status":"Error",
    		"Dev":"Marko_Bots",
    		};return JSONResponse(content=dta)

#uvicorn.run(app,host='0.0.0.0',port=8080)
