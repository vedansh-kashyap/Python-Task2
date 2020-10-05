import pyttsx3
import webbrowser as wb
print("    so wht's up guys    ")
print("========================")

engine = pyttsx3.init()
engine.say("welcom to the world of knoledge")
engine.runAndWait()

print("yes sir what do you want lit me know??")

engine = pyttsx3.init()
engine.say("  Let me know what do you want..")
engine.runAndWait()

ch = input()
if ("date" in ch):
    wb.open("http://13.126.230.164/cgi-bin/menu.py?cmd=date")
elif ("date" in ch):
    wb.open("http://13.126.230.164/cgi-bin/menu.py?cmd=date")
elif("calender" in ch) or ("cal" in ch):
    wb.open("http://13.126.230.164/cgi-bin/menu.py?cmd=cal")
elif("ip" in ch) or ("add" in ch):
    wb.open("http://13.126.230.164/cgi-bin/menu.py?cmd=ifconfig")
elif("list" in ch) or ("files" in ch):
    wb.open("http://13.126.230.164/cgi-bin/menu.py?cmd=ls")
elif("play song " in ch) or ("play tora for me" in ch):
    wb.open("https://www.youtube.com/watch?v=k6i8SnE_iZ8")
elif("new game play " in ch) or ("play gta v for me" in ch):
    wb.open("https://www.youtube.com/watch?v=Do2d-K-Fh-Y")
elif("i am boar" in ch) or ("i am sad " in ch):
    wb.open("https://www.youtube.com/watch?v=al295jJT0es")
elif("bhai roke music" in ch) or (" play roke music" in ch):
    wb.open("https://www.youtube.com/watch?v=eIpLAwON_R4")
else:
    print("not understand")