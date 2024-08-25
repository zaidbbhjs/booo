from fastapi import Response
import requests
import os
import random,uuid
import uvicorn
from fastapi import Request
from user_agent import generate_user_agent
from fastapi.responses import JSONResponse
from fastapi import FastAPI
import secrets
cok = secrets.token_hex(8) * 2
app = FastAPI()
a=int(0)
from fastapi import FastAPI, UploadFile

app = FastAPI()
@app.get('/tik/{email}')
async def tik(email):
		sis = str(uuid.uuid4()).replace('-', '')
		url =f'https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=19&iid=7372841843832473349&device_id=7194351170030650885&ac=WIFI&channel=googleplay&aid=1233&app_name=musical_ly&version_code=310503&version_name=31.5.3&device_platform=android&os=android&ab_version=31.5.3&ssmix=a&device_type=Infinix+X6816&device_brand=Infinix&language=ar&os_api=30&os_version=11&openudid=3293d1a6e9361cb7&manifest_version_code=2023105030&resolution=720*1568&dpi=303&update_version_code=2023105030&_rticket=1722418820230&is_pad=0&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi5g&uoo=0&op_region=IQ&timezone_offset=10800&build_number=31.5.3&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=ar%2C&ts=1722418819&cdid=556d8162-2721-4760-a509-a92b3cf27738&support_webview=1&cronet_version=2fdb62f9_2023-09-06&ttnet_version=4.2.152.11-tiktok&use_store_region_cookie=1'
		headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023105030 (Linux; U; Android 10; ar; JSN-L22; Build/HONORJSN-L22; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)",
  'x-tt-multi-sids': "7244263196788589573%3A2d2c64d5b9a84a83e99bcb51271fb05d",
  'sdk-version': "2",
  'x-bd-kmsv': "0",
  'x-tt-token': "032d2c64d5b9a84a83e99bcb51271fb05d018e06f3998ef8a2cebb5e435736eeaa137afdbf072731d98083650d11370e5d3143cadb7a8643febe4e3f3e212bc1d8031ef99ac847f59944de00c13e7b4ba1d784fd20ec289b1a82c538d53b85530142c-CkAxNWMyOWY1MjRiZWQ5NTVjMDFhNjcwZDBjZmJkNjdlMjhiYmFkNDU1MDlmZmI1ZTdiNDUzNjc3YmZhOGFhNTEx-2.0.0",
  'x-ss-req-ticket': "1724143814731",
  'multi_login': "1",
  'x-tt-passport-csrf-token': "ee8d571c5f8416fdf751859e04ac0ad9",
  'passport-sdk-version': "19",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-vc-bdturing-sdk-version': "2.3.3.i18n",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-ss-stub': "D262610E98D24EF465AA71E6A097CF5D",
  'x-ss-dp': "1233",
  'x-tt-trace-id': "00-6efac9ee1066a4dfacf15306062704d1-6efac9ee1066a4df-01",
  'x-argus': "bxXR7LRluRVi4V9JqQedEaYLIa3vWo2w1dLzN2YTVq0iRq1hykdgtDp+5Fl822k0wZs+Wc2CB3ZxCzZXcwBJV32hLfGBKmeAREs1GsB18eWQvBvtJix7ofOmchDpoiITcD5lOVFeVhYnIyGD566J6BxYgRt5AnffkxtdG+iHXeB+K9FmxpLi65UaQiMgo/SSvsT5jlHwAPI18Mzb29y/30i8xH5RQ2gGY2Dwb0husl77s53e80z9FdxqVkU3gOQ2fUZls6CcNa9Na+rmdjlxsYrtN3wK6IJwihHkPiKeVpp/qbxxo7hkKH2wQQMDpOsQ9voCyFXjZloYawTd3nLDAuv+4t4sTsD0uV4b8L9oxhp5sNfwEGQ9I4C9v2rT8dWjLTc9Ypmlq3BYXCo4Fv5/4vnzwlAjWhleIpVVkuJu4cVl4V7CdZz8610h7uz7f0c4m7QjehGO5Auek/saLoiyEyxz7ETVHQBhxZPAWp0roGBgKUNk++44TqFh1/O481W+bkaMuJwcbTP5DKo+JHIQZ+GyEMT6Avp+tp5FjZgd3SHyf42K6bTJkGRktYpo9PPJVL/jOmoCJaIGwpqvRPnVvpDqYZRYuTe89cbL1VS/YHPeeBSBMFHX2XoBLtbRD+Ys0FE=",
  'x-gorgon': "8404c0c2100001af2c41ffe6895b664c319707c5a8668a4f1214",
  'x-khronos': "1724230210",
  'x-ladon': "xwZIesnERjW/UuJrHJxbf8xohz9Ah16FyPN2MgAQXD78FU25",
  'Cookie': f"d_ticket=db235bee19a1476e2ef95518d7a2dee83ec0d; multi_sids=7244263196788589573%3A2d2c64d5b9a84a83e99bcb51271fb05d; cmpl_token=AgQQAPOnF-RPsLS2JFlgN908_MVGn17MP4QsYNXyiQ; uid_tt=c54c21eceaa2ebb88b3a456e7842cd5262f130c02abe4dd630c8470cb86bae6b; uid_tt_ss=c54c21eceaa2ebb88b3a456e7842cd5262f130c02abe4dd630c8470cb86bae6b; sid_tt={sis}; sessionid={sis}; sessionid_ss={sis}; store-idc=alisg; store-country-code=iq; store-country-code-src=uid; tt-target-idc=useast1a; passport_csrf_token=ee8d571c5f8416fdf751859e04ac0ad9; passport_csrf_token_default=ee8d571c5f8416fdf751859e04ac0ad9; install_id=7403493772548310790; ttreq=1$58be297161337571038dfa70fc0073b16be6df3b; sid_guard=2d2c64d5b9a84a83e99bcb51271fb05d%7C1724008592%7C15552000%7CFri%2C+14-Feb-2025+19%3A16%3A32+GMT; odin_tt=93f3b994509ee8d4a9a6719c29884e8058d3311aa04bffd5f8a8e36827f81fff9b80bf53f6f7604c325532e7dd0e75685e2bea61f0601f6bd5c22601cc0ff4fb2c637d19a6e60e7da3a46a1361658e31; msToken=I0STMc-_BNKhyh_k1FEFXAplbxMJM0OKZuwQZgtr-BVGH_zTOFKO3TJ2M6GhZax2K_fGTtPGCw3mspX8NZrIGQCS9eSQ1BUMYlILQA5m8bnvvv4scZTeDwwrhWL3"
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
			return data
		elif "فشل في الربط، تم ربط صندوق البريد بالحساب الآخر"in res:
			data={
			'dev':'@instagram',
			'status':'available',
			'email':email,
			}
			return data
		else:
			return res

#uvicorn.run(app,host='0.0.0.0',port=8080)
