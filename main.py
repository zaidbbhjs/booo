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
@app.get('/api2/{gmail}')
async def ga(gmail: str, request: Request):
	from requests import post
	email=gmail
	mj=0
	url='https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
	h={
 'X-Pigeon-Session-Id':'2b712457-ffad-4dba-9241-29ea2f472ac5',
 'X-Pigeon-Rawclienttime':'1707104597.347',
 'X-IG-Connection-Speed':'-1kbps',
 'X-IG-Bandwidth-Speed-KBPS':'-1.000',
 'X-IG-Bandwidth-TotalBytes-B':'0',
 'X-IG-Bandwidth-TotalTime-MS':'0',
 'X-IG-VP9-Capable':'false',
 'X-Bloks-Version-Id':'009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
 'X-IG-Connection-Type':'WIFI',
 'X-IG-Capabilities':'3brTvw==',
 'X-IG-App-ID':'567067343352427',
 'User-Agent':'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
 'Accept-Language':'ar-IQ, en-US',
 'Cookie':'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
 'Accept-Encoding':'gzip, deflate',
 'Host':'i.instagram.com',
 'X-FB-HTTP-Engine':'Liger',
 'Connection':'keep-alive',
 'Content-Length':'364',
 }
	da={
 'signed_body':'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"'f'{email}''"}',
 
 'ig_sig_key_version':'4',
 }
	s=post(url,headers=h,data=da).json()
 #print(s)
	if s["status"]=="ok":
		
		return         JSONResponse(content={"status":"Good"})
	else:
		return         JSONResponse(content=s)
#uvicorn.run(app,host='0.0.0.0',port=8080)
@app.get('/tik/{email}')
async def tik():
		sis = str(uuid.uuid4()).replace('-', '')
		url =f'https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=19&iid=7372841843832473349&device_id=7194351170030650885&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=310503&version_name=31.5.3&device_platform=android&os=android&ab_version=31.5.3&ssmix=a&device_type=Infinix+X6816&device_brand=Infinix&language=ar&os_api=30&os_version=11&openudid=3293d1a6e9361cb7&manifest_version_code=2023105030&resolution=720*1568&dpi=303&update_version_code=2023105030&_rticket=1722418820230&is_pad=0&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi5g&uoo=0&op_region=IQ&timezone_offset=10800&build_number=31.5.3&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=ar%2C&ts=1722418819&cdid=556d8162-2721-4760-a509-a92b3cf27738&support_webview=1&cronet_version=2fdb62f9_2023-09-06&ttnet_version=4.2.152.11-tiktok&use_store_region_cookie=1'
		headers = {
    "Host": "api22-normal-c-alisg.tiktokv.com",
    "Content-Length": "95",
    "Cookie": (
        "passport_csrf_token=98153892f65b8d33f0fc4ffe571fe6ff; "
        "passport_csrf_token_default=98153892f65b8d33f0fc4ffe571fe6ff; "
        "d_ticket=9281ab6b344229e79a37b09d997ffd31c1a0f; "
        "multi_sids=7276401311359534085%3A14a2ae47be8dc51939df2969e4159dae%7C7320680702445503493%3A7a7e5835dfc5299e7ac584e090f6e8e2; "
        "cmpl_token=AgQQAPOGF-RPsLTEFtdG9108-bbhdjiI_4csYNYVRg; "
        "uid_tt=2507bbf000c73643b0480fdda21ecfd3015ddb85664c0a9ec8744a812eb35856; "
        "uid_tt_ss=2507bbf000c73643b0480fdda21ecfd3015ddb85664c0a9ec8744a812eb35856; "
        "sid_tt={sis}; "
        "sessionid={sis}; "
        "sessionid_ss={sis}; "
        "store-country-code=tr; "
        "store-country-code-src=uid; "
        "install_id=7372841843832473349; "
        "ttreq=1$95ba7cef3ab3446401e85f477fec283b1f0356ed; "
        "tt-target-idc-sign=znspePrEB2B5KD8K2lCDdggj4Lrw0uZD8o8bYY-w9vx1Z9klJbqvQgGeyl3E8sUGqwqHik_mH1KG6A5VVp__l3LlnWqVrDfjEzg9pcMtVEorYAHJ6Toep-EcMgXE-xS-3cOJwT1Qf5BUZiBoSeg0tnnZBVNK1JsWC-ntQlEGynwHnHW9i027cg1PQ3-umOPXjgbV1OEixU38LwPGQbJWkuX7v8RyMxVp3THNii4nXtbAvhBR7bm_o1VhlMlMn40SQuT9R8yWkQc6RL-HjDh_vLmUg4u1cbQddaqFaV9_m3xSMN96XIWp6MnyF052aO4xZHu9FKbDv_at-nQYCGW-cQKbnnyE69dDs0TE5kW9UT8reh6ZBsjJksItUaixkcAXkyMmkZkceMyRDkUvzTQm2PrsZP9QaKFGKnJJZx54L5wXWJfvRVQgvi0Ww3yzNbSo5h_k989r0nnMBlO8ukkfznwf5KrceuLTfncX1WQ9LVQkzQUhhmv9OOpgCdekXT5C; "
        "store-idc=alisg; "
        "tt-target-idc=alisg; "
        "odin_tt=4dfb813064a0a02517fb0dd3c1009e809bf0ce448947afa034d0e32c795874310203125b5dbae1bc50184a186676c5036593fa5d3ac1d8bff3c8fd7eec825de0b6faf9abdc1bdba28833e68fef89b1f1; "
        "sid_guard=14a2ae47be8dc51939df2969e4159dae%7C1722418253%7C15552000%7CMon%2C+27-Jan-2025+09%3A30%3A53+GMT; "
        "msToken=-7MZX1FGwui41BUSmMF7rmPZte5XSTuOPjeS9D4x3s_4H_ipjHFhhVAgIwDftSWW_3gcy5E2dlCVmid0AQKv9VxfDjtlODra8cMmfK67iolTKbCX_MU0YxgpWnM="
    ),
    "x-tt-multi-sids": "7276401311359534085%3A14a2ae47be8dc51939df2969e4159dae%7C7320680702445503493%3A7a7e5835dfc5299e7ac584e090f6e8e2",
    "sdk-version": "2",
    "x-bd-kmsv": "0",
    "x-tt-token": "0314a2ae47be8dc51939df2969e4159dae04ef342ee9f3bc17179723f2a65bf392603ac44a608f46b8107ebacfd96f2593ae1b301551fa2740d8ce6ca3ab08b9cd60ca9fbb4fddfb32f2ea68c016c71a8495cd41c7d712c40219d6948fe23f6866220-1.0.1",
    "x-ss-req-ticket": "1722418820234",
    "multi_login": "1",
    "x-tt-passport-csrf-token": "98153892f65b8d33f0fc4ffe571fe6ff",
    "passport-sdk-version": "19",
    "x-tt-dm-status": "login=1;ct=1;rt=1",
    "x-vc-bdturing-sdk-version": "2.3.3.i18n",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-ss-stub": "EF371AB22B36112B4E3777D59B57E7BF",
    "x-ss-dp": "1233",
    "x-tt-trace-id": "00-082976481063d778459717c605a804d1-082976481063d778-01",
    "User-Agent": "com.zhiliaoapp.musically/2023105030 (Linux; U; Android 11; ar_IQ; Infinix X6816; Build/RP1A.200720.011; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)",
    "Accept-Encoding": "gzip, deflate, br",
    "x-argus": "hYHSZacQ+SDgjlhp+GYTPATrp4KSxeMsHQySzlh5C4d7w07Cy/3kgo5M8Z2xffqwtvplj4D9mpyLjkrSxhYMrnMxuUo+zjWEC1vnuYSJ6SCnx3jNNrpAMGoJLptuSLDI32yTtCAF6I2CRxlfM3sDQFE++w5/cLMuNPH7oZMoC7hdF+oSimYO1yKIofoIa42nGjcHeES/wlmeYELVLE8jP7Zv9Y96TnziC3CLUL5rgwNisVnl+myJ7Om7f1ee/NEITKCB02v6dWxBdevWv6YU8xbar/XFgay1xjOqau6hAhBfl2zlGLI2GCcFuO0awp/76qFrUVspD5kJFIknREqMZuBZc7XwrGL1zBG2i2dLJ0L8xlf7nnXNJDcHaYJN/k2fgk20670sTHMwSU/2n3qjuoFnlmRvBtkbK9aZhXK6UsZBc7wfXFGtvo7mMEFNMx0bGBXeV0W3nMFUEBvQ8DSyz1sR8cX/TgcXki8fqv66hzqv7gKnoCpVg4DJLPX8BCoaCmbF8E8wY2I8LINdnUnCS171hAApx2OVCtdRChfZO2vm3aVH3FSpLZ7+3IiFmeFFqNnSiP3WFGPkZLjQzLcryRGN6okMTWYmzI8WEmD917+0rCVT1BGBeaz7y6376Hf0oaA=",

    "x-gorgon": "8404d0be100059d8c5deec6af320f9083a816ca0b153a10453d5",
    "x-khronos": "1722418817",
    "x-ladon": "AjUiHZeEpusLBby98MCwh8Po6zMm5xpdn8owe0nCNu1wuUYq"
}
		data = {
    "account_sdk_source": "app",
    "multi_login": "1",
    "email_source": "9",
    "email": email,
    "mix_mode": "1"
}
		res = requests.post(url,headers=headers,data=data).text
		if "قام المستخدم بربط رقم هاتف جوال بالفعل" in res:
			data={
			'dev':'@instagram',
			'status':'unavailable',
			'email':email,
			}
			    	return JSONResponse(content=data)
		elif "فشل في الربط، تم ربط صندوق البريد بالحساب الآخر"in res:
			data={
			'dev':'@instagram',
			'status':'available',
			'email':email,
			}
			    	return JSONResponse(content=data)
		else:
			return 'false'

#uvicorn.run(app,host='0.0.0.0',port=8080)
