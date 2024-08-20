# author : @Syhrularv_
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

banner = """
\033[1;34m                                 .:^^:.                                
                       ..     .:^~~~~~~^:.     ..                      
                       !!~^.:~^^~7?!!?7~^^~:.^~!!                      
                      .~^!!!!~.~!7?~~?7!~.~!!!!^~.                     
                ^~^^:^~^~::~~!!!!?!~~!?!!!!~~::~^~^:^^~^               
        ....... ::.^!7~??~7J?!?!7::^^::7!?!?J7~??~7!^.:: .......       
        ^7~^!!^7~~^???7?^!77:^~7.^!??!^.7~^:77!^?7???^~~7^!!^~7^       
         ^~!^.~!~7JJ.^!!.!7^:~~7.!????!.7~~:^7!.!!^.JJ7~!~.^7~^        
         .~~~.~J?~!7::~^:^^::7?~!77!!77!~?7::^^:^~::7!~?J~.~~~.        
      .^:::!!7?!7^~~^^^^^^^^:::!?!~^~~!?!::^^^^^^^^^~~^7!?7!!:::^.     
      ::^?J7!7^~^~~~~777!77??^~!^:^?:^!~^??77!777~~~~^~^7!7J?^::      
      .~~7~?J~~^^~~~!7~^^^^^^~!!7~~J7^~7!!~^::^^^~7!~~~^^~~J?~7~~.     
      :!^:7J~~~:~~^:!^^^^:!7^!!^!??BB??!^!!^7!:^^:^!^^~~:~~~J7:^!:     
       .~!^??~^:~:.:~:~~^!!~~77..~7??7~..77^~!!^~~:~:.:~:^~??^!~.      
       :^^!7?~~..:~77!7!J&G!7?!!77!??!77!!?7!G&J!7!77~:..~~77!~~:      
       :^^!~7JYJ??~?7~7?JJ?7~^!!!~^!!^~!!!^~7?J??7~7?~??JYJ7~~^^:      
       :^^!^^~!?YGBGY!!!7!~~^^~!777!!777!~^^~~!7!!!YGBGY?!~^^!~^:      
       :~:!^:!7!~^!YBBP?^7?7^~7Y??JYYJ??Y7~^7?7^?PBBY!^~!7!:^!^~:      
        ~:!~:^~^~~!^^YGJP#&Y5PJ7PBG55GBP7JP5Y&#PJGY^^!~~^~^:~~^~       
        :^^!^^~~!::J^.?B&@YPB&GP&&@BB@&&PG&BPY@&G?.^J::!~~^^!^~:       
         ^^~!^^~!?~YJY#&B?~YY^.?PPPJJPPP7.^YY~?B&#YJY~?!~^^!~^^        
          ~^~!^^!!?P#&G?:.!YPY7^^ :!!: ^^7YPY!.:?G&#P?!!^^!~^^         
           ^^^!~~?5PP7~^^~^~~YBJ~..^^..~JBY~~^~^^~7PP5?~~~~^^          
            :^^~~^:^~~!!77~~!!~^~:....:~^~!!!~77!!~~^:^~~^^:           
             .^^^~~~^^~7?!!77!^~~:^..^:~~^!77!!?7~^^^~~^^^.            
               .^^^~~^~:~7!~~~^!~~^^^^~~!^~~~!7~:~^~~^^^.              
                 .:^^^~~!7!~~?!!~~~^^~~~!!?~~!7!~~^^^:.                
                    .::^^^~~:^~!7!~~~~!7!~^:~^^^^^:.                   
                        ..:~!7!!77~~~~77!!7!~::.                       
                            ...~!777777!~...                           
                                :^~~~~^:                               
                                   ..
                        {} S E C R E T  D I R A J A
""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}1{}]{} Encript      {}[{}2{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (sukses + "Done..")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

def enkrip():
   try:
       script = raw_input(ask + W + "Script " + G + "> " + W)
       output = raw_input(ask + W + "Output " + G + "> " + W)
       os.system("bash-obfuscate " + script + " -o " + output )
       print (sukses + "Done..")
   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")


takok = raw_input(W + "Choose" + G + " > ")

if takok == "1" or takok == "01":
   enkrip()
elif takok == "2" or takok == "02":
   dekrip()
else:
   print (eror + " Wrong input")
