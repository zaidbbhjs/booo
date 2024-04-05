from fastapi import Response
import requests
import os
import random
import uvicorn
from fastapi import Request
import json,faker
from user_agent import generate_user_agent
from fastapi.responses import JSONResponse
from fastapi import FastAPI
import secrets
cok = secrets.token_hex(8) * 2
app = FastAPI()
a=int(0)
from fastapi import FastAPI, UploadFile

app = FastAPI()

from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
from faker import Faker
yy='azertyuiopmlkjhgfdsqwxcvbn'
@app.get('/api/{email}')
async def ga(email):
    	num="5678"
    	rng = int("".join(random.choice(num) for i in range(1)))
    	wqq = 'qwertyuiopasdfghjklzxcvbnm'
    	name = "".join(random.choice(wqq) for i in range(rng))
    	nn1 = Faker().simple_profile()
    	rr1 = nn1['username'].split(' ')[0]
    	r=rr1,name
    	r = "".join(random.choice(r) for i in range(1))
    	#r=random.choice(name,rr1)
    	r=f"{r}@hotmail.com"
        r={"email":f"{r}"}
    	return         JSONResponse(content=r)
#uvicorn.run(app,host='0.0.0.0',port=8080)
