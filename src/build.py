import re,sys
S=sys.argv[1]
old=open(S+"/jugadores.html",encoding="utf-8").read()
data=re.search(r'<script id="data" type="application/json">(.*?)</script>',old,re.S).group(1)
cs=re.search(r'var COUNTRIES=(\{.*?\});\n',old,re.S).group(1)
t=open(S+"/template2.html",encoding="utf-8").read()
t=t.replace("__DATA__",data).replace("__COUNTRIES__",cs).replace("__CRESTS__",open(S+"/crests.json").read())
V="10.14.1"
head=('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
 '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%276%27 fill=%27%23a9bbd3%27/%3E%3Ctext x=%2716%27 y=%2722%27 font-size=%2716%27 font-family=%27Arial%27 font-weight=%27bold%27 text-anchor=%27middle%27 fill=%27%230b121b%27%3ENG%3C/text%3E%3C/svg%3E">\n')
t=t.replace('<title>NG League</title>',head+'<title>NG League</title>',1)
t=t.replace('<style>','<style>\n[hidden]{display:none!important}body{margin:0}',1)
libs=''.join('<script src="https://www.gstatic.com/firebasejs/%s/firebase-%s-compat.js"></script>\n'%(V,n) for n in ("app","auth","firestore"))
t=t.replace('<script id="data"',libs+'<script id="data"',1)
t=t.rstrip()+"\n</body>\n</html>\n"
t=t.replace('</style>\n\n<header','</style>\n</head>\n<body>\n<header',1)
assert '<body>' in t
open(S+"/index.html","w",encoding="utf-8").write(t)
print(round(len(t)/1e6,2),"MB")
