import sys
import os

def intro():
    with open("usernames.txt", "a") as file:
        file.write(f"{name}\n")
    print(f"Welcome, {name}!\n")
    print("Since this seems to be your first time here, here are some things to note:")
    print("-FileFinder operates by being given a path to the folder(s) you'd like searched, before being given the name of the file.")
    print("-It will NOT look inside subfolders, unless you include them as separate paths!")
    print("-If you're ever confused about something regarding FileFinder, go back to main with '!m' and then navigate to the help menu with '!h'!")
    print("-You can exit anytime with '!e'!")
    print("-There's a changelog you can check out with your next input that can help check what changes. Use '!c' from main to look through it!")
    print("-Since FileFinder's search gives you the path to the file if it exists, you can directly input that path to find the file, or give the path to any other software that takes paths!")
    main()
def main():
    print(f"Welcome to the main menu, {name}!\n")
    print("-Type '!s' to enter constrained file search.")
    print("-Type '!h' to enter the help menu.")
    print("-Type '!c' to view changelog.")
    print("-Type '!e' to end program.")
    request = input()
    if request == "!s":
        constrainedSearch()
    elif request == "!h":
        helpMenu()
    elif request == "!c":
        changelog()
    elif request == "!e":
        print("Goodbye!")
        sys.exit(0)
def constrainedSearch():
    print("You are now in constrained search.")
    print("-Enter the path(s) to the folder(s) you would like searched (ex: C:\\coolstuff\\planes).")
    print("-Type '!d' to indicate you have submitted all folders, '!e' to exit, or '!m' to return to main.")
    print("-You can give multiple folders for the search, but search time may be adversely affected by this.\n")
    folders.clear()
    files = 0
    while True:
        request = input("")
        if request == "!e":
            print("Goodbye!")
            sys.exit(0)
        elif request == "!m":
            main()
            break
        elif request == "!d":
            if files >= 6:
                warning()
                break
            else:
                enterFile()
                break
        else:
            folders.append(request)
            files = files + 1

def warning():
    print("NOTE: You are attempting to search 6+ folders at once! Search times could be MUCH higher than expected.\n")
    print("Enter '!y' to proceed, '!m' to return to main, or '!e' to exit program.\n")
    request = input()
    if request == "!y":
        enterFile()
    elif request == "!m":
        main()
    elif request == "!e":
        print("Goodbye!")
        sys.exit(0)

def enterFile():
    print("Now, please input the name of the file you would like searched for (ex: 'cat.png') Type '!e' to exit or '!m' to return to main.\n")
    target = input()
    if target == '!e':
        print("Goodbye!")
        sys.exit(0)
    elif target == '!m':
        main()
        return
    result = 0
    for folder in folders:
        files = [i for i in os.listdir(folder) if os.path.isfile(os.path.join(folder, i))]
        for file in files:
            if file == target:
                result = folder + "\\" + file
                break
        if result != 0:
            print(f"\nFile Path Found: {result}\n")
            print("Enter '!e' to exit, or '!m' to return to main.\n")
            request = input()
            if request == "!e":
                print("Goodbye!")
                sys.exit(0)
            elif request == "!m":
                main()
                break
    if result == 0:
        print(f"\n\nFile was not found in folders. It may not be in the folder entirely or in a subfolder. If neither of these are the case, please contact support.\n")
        print("Enter '!e' to exit, or '!m' to return to main.\n")
        request = input()
        if request == "!e":
            print("Goodbye!")
            sys.exit(0)
        elif request == "!m":
            main()

def helpMenu():
    print(f"Welcome to the help menu, {name}!\n")
    print("-Type '!f' to read frequently asked questions and answers.")
    print("-Type '!t' to read a list of notable tips to improve your experience.")
    print("-Type '!s' to see support contact info.")
    print("-Type '!m' to return to main.")
    print("-Type '!e' to exit program.\n")
    request = input()
    if request == "!f":
        faq()
    elif request == "!t":
        tips()
    elif request == "!s":
        support()
    elif request == "!e":
        print("Goodbye!")
        sys.exit(0)
    elif request == "!m":
        main()

def faq():
    print("Q: Can I use this for grabbing files for other software?")
    print("A: Absolutely! FileFinder can be used to grab the path to a file for anything you want to use, just make sure it's a file that'll work for your program!\n")
    print("Q: Why won't it automatically look through subfolders?")
    print("A: Could get added as a future option, but it would slow down the runtime quite the bit. You can still manually select folders that are in other folders, though!\n")
    print("Q: Will there be other search functions in the future?")
    print("A: Potentially, yes. It depends on a couple of factors, but there are some we're looking at implanting later on!\n")
    print("Enter '!e' to exit, or '!m' to return to main.\n")
    request = input()
    if request == "!e":
        print("Goodbye!")
        sys.exit(0)
    elif request == "!m":
        main()

def tips():
    print("-You can type '!e' anytime you're asked for input to exit, or '!m' to return to main from any section AFTER main.")
    print("-You can include folders to search that are in other folders, INCLUDING folders in other folders you're already searching.")
    print("-You can reach out to support not just for technical help, but to ask questions related to FileFinder or give suggestions for changes/additions you think would make the app better!\n")
    print("Enter '!e' to exit, or '!m' to return to main.\n")
    request = input()
    if request == "!e":
        print("Goodbye!")
        sys.exit(0)
    elif request == "!m":
        main()

def support():
    print("-Email for suggestions, questions, and concerns: neuensce@oregonstate.edu\n")
    print("Enter '!e' to exit, or '!m' to return to main.\n")
    request = input()
    if request == "!e":
        print("Goodbye!")
        sys.exit(0)
    elif request == "!m":
        main()

def changelog():
    print("Version 1.0.0: Release!")
    print("Version 0.8.0: Beta, added changelog and multi-folder searching!\n")
    print("Enter '!e' to exit, or '!m' to return to main.\n")
    request = input()
    if request == "!e":
        print("Goodbye!")
        sys.exit(0)
    elif request == "!m":
        main()

prompt = "Welcome to FileFinder, please input your preferred username! If you're new, you can make one here!\n"
name = input(prompt)
folders = []
usernames = open("usernames.txt", "r")
knownName = False
for line in usernames:
    text = line.strip()
    if text == name:
        knownName = True
        usernames.close()
        main()
        break
if not knownName:
    usernames.close()
    intro()


