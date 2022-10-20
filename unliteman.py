import sys, requests
ses=requests.Session()
id = []
token = "token kamu"
cok = "cookie kamu"
cookie = {"cookie":cok}

idt = input("masukan id : ")
try:
	for idz in ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
		try:
			for i in ses.get(f"https://graph.facebook.com/{idz['id']}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie).json()["friends"]["data"]:
				if i["id"]+"<=>"+i["name"] in id:
					pass
				else:
					id.append(i["id"]+"<=>"+i["name"])
				sys.stdout.write(f"\r [*] sedang mengumpulkan {len(id)} id...");sys.stdout.flush()
		except:continue
except Exception as e:
	print(e)