import hashlib

#LinkedIn
linkedInFile = open('SHA1.txt')
linkedInPasswords = open('linkedInPasswords.txt', 'w')
mostUsedPasswords = open('top10000passwords.txt')

pwFromFile = []
for line in linkedInFile:
	line = line.replace("\n", "")
	pwFromFile.append(line)

pwFromMUP = []
for word in mostUsedPasswords:
	word = word.replace("\n", "")
	pwFromMUP.append(word)

# Attemps to check random passwords
#sha1Hashed = hashlib.sha1(pwFromMUP[53].encode())
#print(sha1Hashed)
#sha1Hex = sha1Hashed.hexdigest()
#print(sha1Hex)
#print(pwFromFile[0])
#pwhash = hashlib.sha1(pwFromFile[0].encode())
#pwhex = pwhash.hexdigest()
#print(pwhex)

for pw in pwFromFile:
	fileHashed = hashlib.sha1(pw.encode())
	fileHex = fileHashed.hexdigest()
	for password in pwFromMUP:
		sha1Hashed = hashlib.sha1(password.encode())
		sha1Hex = sha1Hashed.hexdigest()
		if sha1Hex == fileHex:
			linkedInPasswords.write(sha1Hex + ", Password: " + password + "\n")

linkedInFile.close()
linkedInPasswords.close()
mostUsedPasswords.close()