import webbrowser as browser
import os as os
import subprocess

class Functions():
    def __init__(self, commands: dict):
        super().__init__()
        self.commands = commands
        self.func_index = None
        self.query = None        
        self.delimeter = None
        self.texttotype = None

    def update_functions(self) -> object:
        self.commands['open google search'].update(dict(commands=lambda: self.open_google_search())) # open google search
        self.commands['youtube search'].update(dict(commands=lambda: self.open_youtube_search())) # open youtube search
        self.commands['search in google'].update(dict(commands=lambda: self.search_in_google())) # search in google
        self.commands['search in youtube'].update(dict(commands=lambda: self.search_in_youtube())) # search in youtube
        self.commands['open notepad'].update(dict(commands=lambda: self.open_notepad())) # open notepad
        self.commands['please type'].update(dict(commands=lambda: self.type_in_text())) # please type

    def function_identifier(self, func_index: str, parametres_ext: dict) -> object:
        # these are just extra variables used by other functions, you can create your own in `__init__`
        self.func_index = func_index
        self.delimeter = self.func_index 
        self.query = parametres_ext['query'] 
        self.texttotype = parametres_ext['texttotype']
        self.commands[func_index]["commands"]()

    '''
    Below are the functions used to perform specific operations
    You can add your own functions below and initialize it in `update_functions()` functions
    '''

    def open_google_search(self) -> object:
        try:
            browser.get(r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s").open("https://www.google.com/")
        except Exception as e:
            print(e)

    def open_youtube_search(self) -> object:
        try:
            browser.get(r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s").open("https://www.youtube.com/")
        except Exception as e:
            print(e)

    def search_in_google(self) -> object:
        try:
            self.query = "+".join(self.query.split("%s "%self.delimeter)[1].split(" "))
            browser.get(r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s").open("https://www.google.com/search?q=%s"%self.query)
        except Exception as e:
            print(e)

    def search_in_youtube(self) -> object:
        try:
            self.query = "+".join(self.query.split("%s "%self.delimeter)[1].split(" "))
            browser.get(r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s").open("https://www.youtube.com/results?search_query=%s"%self.query)
        except Exception as e:
            print(e)

    def open_notepad(self) -> object:
        subprocess.Popen("notepad.exe", shell=True)

    def type_in_text(self) -> object:
        try:
            if not os.path.exists("texttotype.txt"):
                open("texttotype.txt", "w+")
            text = "".join(self.texttotype.split(self.delimeter)[1])
            with open(file="texttotype.txt", mode="w+", encoding="utf-8") as txt:
                txt.write(text)
                txt.close()
            os.startfile("auto.vbs")
        except Exception as e:
            print(e)

