'''
Program: Caesar Cipher.
Developer: Mayank Daga(github/coder-daga)
Python Version used: 2.7
　
'''
　
#This function encrypts the message for user.
def encrypt():
	
	#pt:PlainText. Accept string from user.
	
	pt=raw_input("Please enter the text you wan to convert to gibberish:\n").lower();
	
	#accept shift from user.
	
	shift=int(raw_input("Please enter the key value: "));
	
	answer=''						 #initialize a blank variable for later appending the character values.
	for char in pt:					 #iterating through the plaintext.
		char=(ord(char)+shift)		 #getting the ascii value of the character with shift added.
		if char - shift==32:		 #if the ascii of character is 32 i.e a space, leave it at 32.
			char = 32
			
		#if the value of ascii of char is more than ascii of z, substract 26. 
		#eg. a shift of 3 to char z(122) will return ascii 125. so 125-26=99 i.e ascii of 'c'
		
		elif char > ord('z'):			  
			char-=26
			
		#if the value of ascii of char is less than ascii of a, add 26. 
		
		elif char < ord('a'):
			
			char+=26
		char=chr(char)
		answer = answer + char
	print(answer)
	
　
def decrypt():	
	ck=raw_input("Please enter the gibberish to make sense out of it:\n").lower();
	shift=int(raw_input("Please enter the key value: "));
	answer='';
	for char in ck:
		char=(ord(char)-shift)
		if char + shift==32:
			char = 32
		elif char > ord('z'):
			char-=26
		elif char < ord('a'):
			
			char+=26
		char=chr(char)
		answer=answer+char
	print(answer)
		
　
　
choice=int(raw_input("Please press 1 for encryption or 2 for decryption: "));
if choice==1:
	encrypt();
elif choice==2:
	decrypt();
else:
	print("Wrong choice entered. Exiting now..");
	exit();
