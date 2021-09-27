
should_continue = True
while should_continue == True:
	letters1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
	            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
	            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
	            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	text_list = []
	direction = input("Type 'encode' to encrypt or 'decode' to decrypt\n").lower()
	text = input("Select your Phrase\n").lower()    
	shift = int(input("Select your Shift Key: "))
	for i in range(0, len(text)):
		text_list.append(text[i])
		
	def ceasar(direction, msg, shift):
		
		if shift >= 26:
			shift = round(shift / 26)
			
		if direction == "encode":
			letters2 = []
			new_text = []
			final = ""
			for i in range(0, 40):
				if i >= 27:
					i = 0
				letters2.append(letters1[i + shift])
			for i in range(0, len(msg)):
				for i2 in range(0, 26):
					if letters1[i2] == msg[i]:
						new_text.append(letters2[i2])
			for i in new_text:
				final += i
			print(final)
		
		
		elif direction == "decode":
			letters2 = []
			new_text = []
			final = ""
			for i in range(0, 52):
				if i <= 25:
					i = 51
				letters2.append(letters1[i - shift])
			for i in range(0, len(msg)):
				for i2 in range(0, 26):
					if letters1[i2] == msg[i]:
						new_text.append(letters2[i2])
			for i in new_text:
				final += i
			print(final)
		else:
			print(f"\n[+] invalid input {direction}, type 'encode' or 'decode'\n")
			ceasar(direction = direction, msg = text_list, shift = shift)
			
	ceasar(direction = direction, msg = text_list, shift = shift)
	end_app = input("Would you like to run the Cipher Tool again?\n")
	if end_app == "no":
		print("Goodbye")
		should_continue = False
