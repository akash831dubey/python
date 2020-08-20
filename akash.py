import os

while True:
	print("Enter  your requirements : "  , end='')
	p = input()

if (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("chrome" in p) or("internet"in p) or ("browser" in p)):
	os.system("chrome")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("pdf editor" in p) or("pdf"in p)):
	os.system("PDFXEdit")

elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and ("anydesk" in p) :
	os.system("AnyDesk")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and ("gitbash" in p)  :
	os.system("git-bash")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and ("modem" in p) :
	os.system("USB Modem")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and ("modem" in p) :
	os.system("USB Modem")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("bluej" in p)  or ("java" in p)):
	os.system("blueJ") 
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("video player" in p) or ("video media" in p) ):
	os.system("vlc")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("github" in p) or ("github desktop" in p)) :
	os.system("GitHubDesktop")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("editor" in p) or ("vs code "in p) or ("visual code editor" in p )):
	os.system("Code")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("telegram" in p)  or ("social media " in p )) :
	os.system("Telegram")
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("video recoder" in p)  or ("record video " in p )) :
	os.system("bdcam") 
elif (("run" in p)  or ("open" in p) or ("launch" in p)  or ("execute" in p )) and (("video recoder" in p)  or ("record video " in p )) :
	os.system("bdcam")
elif  ("exit" in p)  or ("quit" in p) or ("stop" in p):
	break 
else:
  print("Select Proper Term To Open ")


