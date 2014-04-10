#!/usr/bin/python
import cgi
import cgitb
#cgi.test()
#cgitb.enable()
form=cgi.FieldStorage()
choice=form.getvalue('choice')
print "Content-Type:text/html\n"

print '<link rel="stylesheet" href="../surveyStyle.css">\n'

f = open("survey.ssv", "rw+")
info = f.readlines()
f.close()

choice = "choice"

print "<head>"
print '<link rel="shortcut icon" href="http://i68.photobucket.com/albums/i7/newphew92/bagel_zps29e40f4c.jpg">'
print "<h1>\n%s</h1>" %(info[0])
print "</head>"

for i in range(1, len(info)):
		print	"<p>"
		print	"%s" %(info[i])
		print	"</p>"
		print	'<form action="http://cs.mcgill.ca/~ctrinh2/cgi-bin/results.py" method="post">'
		
		print	"<input type=\"radio\" name=\"%s%d\" value=\"1\"> Strongly Agree<br>" % (choice, i)
		print	"<input type=\"radio\" name=\"%s%d\" value=\"2\"> Agree<br>" % (choice, i)
		print	"<input type=\"radio\" name=\"%s%d\" value=\"3\"> Disagree<br>" % (choice, i)
		print	"<input type=\"radio\" name=\"%s%d\" value=\"4\"> Strongly Disgree<br>\n" % (choice, i)

print '<input type="submit" name="finish" value="Submit" style="font-size:20px">'
print "</form>"
print '<a href="http://cs.mcgill.ca/~ctrinh2/welcome.html">Return to homepage</a><br>'
print '<a href="http://cs.mcgill.ca/~ctrinh2/cgi-bin/results.py">Skip survey and go to results</a>'
print "</BODY>\n"

#url='survey.html
#response=requests.post(url,data=form_data)
