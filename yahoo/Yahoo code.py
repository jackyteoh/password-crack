import re

#Yahoo
yahooFile = open('password.file', 'r')
yahooRead = yahooFile.read()
yahooArray = re.findall(r'\d+:.+:.+\s', yahooRead)

yahooPasswords = open('yahooPasswords.txt', 'w')
for i in range(1, 100):
	line = yahooArray[i]
	line = line.replace("\n", "")
	number, email, password = line.split(':')
	decodedPassword = line + ", Password: " + password + "\n"
	if int(number) > 0 and int(number) < 100:
		yahooPasswords.write(decodedPassword)

yahooFile.close()
yahooPasswords.close()