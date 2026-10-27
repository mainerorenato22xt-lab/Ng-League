import re,sys
S=sys.argv[1]
old=open(S+"/jugadores.html",encoding="utf-8").read()
data=re.search(r'<script id="data" type="application/json">(.*?)</script>',old,re.S).group(1)
cs=re.search(r'var COUNTRIES=(\{.*?\});\n',old,re.S).group(1)
t=open(S+"/template2.html",encoding="utf-8").read()
assert "__DATA__" in t and "__COUNTRIES__" in t
t=t.replace("__DATA__",data).replace("__COUNTRIES__",cs)
t=t.replace("__CRESTS__",open(S+"/crests.json").read())
open(S+"/jugadores2.html","w",encoding="utf-8").write(t)
print(round(len(t)/1e6,2),"MB")
