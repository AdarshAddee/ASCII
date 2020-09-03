import os
import pyfiglet
import termcolor
from termcolor import colored

os.system("clear")

print(colored("Press CTRL + Z to quit", "red"))


input("Press ENTER to continue ........")

os.system("clear")


print(colored("   :::'###:::::'######:::'######::'####:'####:", "red"))
print(colored("   ::'## ##:::'##... ##:'##... ##:. ##::. ##::", "red"))
print(colored("   :'##:. ##:: ##:::..:: ##:::..::: ##::: ##::", "red"))
print(colored("   '##:::. ##:. ######:: ##:::::::: ##::: ##::", "red"))
print(colored("    #########::..... ##: ##:::::::: ##::: ##::", "red"))
print(colored("    ##.... ##:'##::: ##: ##::: ##:: ##::: ##::", "red"))
print(colored("    ##:::: ##:. ######::. ######::'####:'####:", "red"))
print(colored("   ..:::::..:::......::::......:::....::....::", "red"))
print(colored("   ..:::::..:::......::::......:::....::....::", "red"))

print("\n")

print("<================================================>")

print(colored("   Youtube: https://youtube.com/mridealhat", "yellow"))

print(colored("   Github: https://github.com/adarshaddee", "yellow"))

print(colored("   Facebook: https://facebook.com/adarshaddee", "yellow"))

print(colored("   Instagram: https://instagram.com/adarshaddee", "yellow"))

print("<================================================>")



# user text 
txt = input(colored("\nEnter your text: \nAD4rSH_> ", "cyan"))

# user font

print(colored("\n>>> Choose your font style:", "red"))

print(colored("[01] Standard \t\t\t [02] Slant", "green"))

print(colored("[03] 3 - d \t\t\t [04] 3 x 5", "green"))

print(colored("[05] 5lineoblique \t\t [06] Alphabet", "green"))

print(colored("[07] Banner 3 - D \t\t [08] Doh", "green"))

print(colored("[09] Isometric1 \t\t [10] Letters", "green"))

print(colored("[11] Alligator \t\t\t [12] Dotmatrix", "green"))

print(colored("[13] Bubble \t\t\t [14] Bulbhead", "green"))

print(colored("[15] Digital \t\t\t [16] Stop", "green"))

print(colored("[99] Exit", "green"))



# user font
font = int(input(colored("\nEnter your font: \nADD33_> ", "cyan")))



if font == 1:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt)
	os.system("sleep 1")
	print(result)



elif font == 2:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "slant")
	os.system("sleep 1")
	print(result)	





elif font == 3:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "3-d")
	os.system("sleep 1")
	print(result)	



elif font == 4:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "3x5")
	os.system("sleep 1")
	print(result)	



elif font == 5:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "5lineoblique")
	os.system("sleep 1")
	print(result)	



elif font == 6:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "alphabet")
	os.system("sleep 1")
	print(result)	



elif font == 7:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "banner3-D")
	os.system("sleep 1")
	print(result)	



elif font == 8:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "doh")
	os.system("sleep 1")
	print(result)	




elif font == 9:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "isometric1")
	os.system("sleep 1")
	print(result)	




elif font == 10:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "letters")
	os.system("sleep 1")
	print(result)	




elif font == 11:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "alligator")
	os.system("sleep 1")
	print(result)	



elif font == 12:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "dotmatrix")
	os.system("sleep 1")
	print(result)	




elif font == 13:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "bubble")
	os.system("sleep 1")
	print(result)	



elif font == 14:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "bulbhead")
	os.system("sleep 1")
	print(result)	




elif font == 15:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "digital")
	os.system("sleep 1")
	print(result)	



	
elif font == 16:
	
	print(colored("\nWe are creating your ASCII text \n", "magenta"))
	
	os.system("sleep 0.5")
	
	print(colored("Please wait\n", "magenta"))
	
	# logic
	result = pyfiglet.figlet_format(txt, font = "stop")
	os.system("sleep 1")
	print(result)	




elif font == 99:
	print("\nThank you using our tool :-) ")
	print("See you again")



else:
		print("Not in options")
		print("Please try again")

