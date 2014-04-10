#!/usr/bin/python
import cgi
import cgitb
import re
import urllib
#cgi.test()
#cgitb.enable()
form=cgi.FieldStorage()
#choice=form.getvalue('choice')
print "Content-Type:text/html\n"

print '<link rel="stylesheet" href="../surveyStyle.css">\n'
print form
#print "one"
#print str(form)\
#print len(form)
i=1


#print form[('choice%d',%i].value
#print form["choice"+str(1)].value
#for i in range (1, len(form)):
  #print i
for i in range (1, len(form)):
 
  a= "choice"+str(i)
  #print a
  #print form[a].value
  ##print "mash"
  #print form.getlist("choice"+i)
  #print form["choice"+i].getlist("choice"+i)
  #print form["choice"+i].getvalue("choice"+i)
  print (form["choice"+str(i)].value)
print "one"
string=form.values
print string
print "one"

f = open("survey.ssv", "rw+")
info = f.readlines()
f.close()

f = open("results.ssv", "a")
results = re.findall(r'\d+', form.value)
for i in range(0, len(results)):
  f.write("%d " %(results[i]),)
f.close()

choice = "choice"

print "<head>"
print '<link rel="shortcut icon" href="http://i68.photobucket.com/albums/i7/newphew92/bagel_zps29e40f4c.jpg">'
print "<h1>\n%s - Results</h1>" %(info[0])
print "</head>"

for i in range(1, len(info)):
		print	"<p>"
		print	"%s" %(info[i])
		print	"Strongly agreed: %d, Agreed: %d, Disagreed: %d, Strongly disagreed: %d, Average %d" %()
		print	"</p>\n"

print '<a href="http://cs.mcgill.ca/~ctrinh2/welcome.html">Return to homepage</a><br>'
print "</BODY>\n"

#url='survey.html
#response=requests.post(url,data=form_data)
