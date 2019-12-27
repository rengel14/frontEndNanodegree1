stop = 0
html = ""
while(True):
	headNum = input("Header Num: ")
	if(headNum == "end"):
		break
	headTitle = input("Header Title: ")
	text = ""
	while(True):
		temp = input("body: ")
		if((temp != "end") and (temp != "")):
			text = text + "<p>&emsp;" + temp + "</p>\n"
		else:
			if(temp == "end"):
				break
	html = html + "\n<h" + str(int(headNum)+1) + ">" + headTitle + "</h" + str(int(headNum)+1) + ">\n"
	html = html + text
		
	
html = html.encode('ascii', 'ignore')
fp = open("htmlOut.txt", 'wb')
fp.write(html)