import os

os.system('clear')



banner = '''
8b           d8  88                 88888888ba   88888888888  
`8b         d8'  88                 88      "8b  88           
 `8b       d8'   88                 88      ,8P  88           
  `8b     d8'    88   ,d8           88aaaaaa8P'  88aaaaa      
   `8b   d8'     88 ,a8"  aaaaaaaa  88""""""8b,  88"""""      
    `8b d8'      8888[    """"""""  88      `8b  88           
     `888'       88`"Yba,           88      a8P  88           
      `8'        88   `Y8a          88888888P"   88           
                                                              
                                                              '''
print(banner)

text = '''
     
      [1]-VkBruteForce
        
      '''
print(text)

v = int(input("�������� �����:"))
def Vkpassgen():
	import os
	os.system("python3 passgen.py")

def VkBruteForceV1():
	import os
	os.system("python3 vk.py")

def VkBruteForce2():
	import os
	os.system('python vk2.py')

if v ==3:
	vkpassgen()
elif v ==1:
	VkBruteForce()
elif v ==22:
	VkBruteForce2()
