import webbrowser
from colorama import Fore as f, Back as b, Style as s, init
init(autoreset=True)
WIDTH=110
print(f.GREEN+'='*50,f.YELLOW+s.BRIGHT+b.RED+'MY  PERSONAL COMMAND CENTER',f.GREEN+'='*68)
print()
while True:
    print(f.GREEN+'='*147)
    print(f.RED+s.BRIGHT+"WHICH WEBSITE DO YOU WANT TO GO?")
    print(f.GREEN+'='*147)
    print(f.WHITE+s.BRIGHT+"1. GOOGLE")
    print(f.WHITE+s.BRIGHT+"2. GOOGLE MAPS")
    print(f.WHITE+s.BRIGHT+"3. YOUTUBE")
    print(f.CYAN+s.BRIGHT+"4. WHATSAPP WEB")
    print(f.CYAN+s.BRIGHT+"5. MICROSOFT EDGE")
    print(f.CYAN+s.BRIGHT+"6. CHAT GPT")
    print(f.CYAN+s.BRIGHT+"7. GOOGLE GEMINI")
    print(f.YELLOW+s.BRIGHT+"8. GGSIPU MAIN WEBSITE")
    print(f.YELLOW+s.BRIGHT+"9. GGSIPU REGISTRATION SITE")
    print(f.YELLOW+s.BRIGHT+"10. CBSE")
    print (f.GREEN+s.BRIGHT+"11. ---------EXIT---------")
    print(f.GREEN+'='*147)
    print()
    d=input(f.CYAN+s.BRIGHT+"Enter Your Choice Number: ")       
    if d=='1':
         print(f.WHITE+s.BRIGHT+"GOOGLE IS OPENING........")
         webbrowser.open('https://google.com')
         print(f.GREEN+'='*147)
         print()
    elif d=='3':
        print(f.WHITE+s.BRIGHT+" YOUTUBE IS OPENING........")
        webbrowser.open('https://www.youtube.com/')
        print(f.GREEN+'='*147)
        print()
    elif d=='4':
        print(f.CYAN+s.BRIGHT+' WHATSAPP WEB IS OPENING......')
        webbrowser.open('https://web.whatsapp.com/')
        print(f.GREEN+'='*147)
        print()
    elif d=='5':
        print(f.CYAN+s.BRIGHT+' MICROSOFT EDGE IS OPENING......')
        webbrowser.open('C:/Users/Public/Desktop/Microsoft Edge.lnk')
        print(f.GREEN+'='*147)
        print()
    elif d=='6':
        print(f.CYAN+s.BRIGHT+" CHAT GPT IS OPENING......")
        webbrowser.open('https://chatgpt.com')
        print(f.GREEN+'='*147)
        print()
    elif d=='2':
        print(f.WHITE+s.BRIGHT+' GOOGLE MAPS IS OPENING.....')
        webbrowser.open('https://maps.google.com')
        print(f.GREEN+'='*147)
        print()
    elif d=='7':
        print(' GOOGLE GEMINI IS OPENING.....')
        webbrowser.open('https://gemini.google.com/app?hl=en-IN')
        print(f.GREEN+'='*147)
        print()
    elif d=='8':
        print(f.YELLOW+s.BRIGHT+' GGSIPU MAIN WEBSITE IS OPENING......')
        webbrowser.open('https://ipu.ac.in')
        print(f.GREEN+'='*147)
        print()
    elif d=='9':
        print(f.YELLOW+s.BRIGHT+' GGSIPU REGISTRATION SITE IS OPENING.....')
        webbrowser.open('https://ipu.admissions.nic.in/')
        print(f.GREEN+'='*147)
        print()
    elif d=='10':
        print(f.YELLOW+s.BRIGHT+' CBSE IS OPENING......')
        webbrowser.open('https://cbse.gov.in')
        print(f.GREEN+'='*147)
        print()
    elif d=='11':
        print('='*147)
        print()
        print(f.GREEN+s.BRIGHT+" ---------EXIT--------- ")
        print()
        print(f.GREEN+'='*147)
        break
    else:
        print(f.RED+s.BRIGHT+"Not From Available Choices")
        print(f.GREEN+'='*147)
        print()

