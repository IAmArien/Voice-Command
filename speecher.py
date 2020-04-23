import time as time
import os as os
import json as object_notation
import speech_recognition as sr
import keyboard as kb
from command import Functions

class Recognition():
    def __init__(self, functions: dict, exception: str):
        super().__init__()
        self.transform = None        
        self.recognizer = sr.Recognizer()
        self.command = Command(functions=functions, exception=exception)

    def google_audio(self, audio: object) -> object:
        cmd_result = self.command.search_in_commands(text_recognizer=self.recognizer.recognize_google(audio_data=audio))
        self.transform.open_sapi().write_spvoice(message=cmd_result["message"]).start_sapi()
        time.sleep(5)
        if cmd_result["result"] == True:
            print(cmd_result)
            self.command.exec_command(func_index=cmd_result["index"],parametres_ext=dict(query=cmd_result["query"],texttotype=cmd_result['query'])) # add extra parameters and access it in the `exec_command` functions

    def listen(self, micro_source: object) -> object:
        audio = self.recognizer.listen(source=micro_source, timeout=3, phrase_time_limit=3)
        self.google_audio(audio=audio)

    def microphone(self, transform: object) -> object:     
        self.transform = transform   
        with sr.Microphone() as source:
            print("Listening.. Please Speak!")
            self.listen(micro_source=source)

class Command():
    def __init__(self, functions: dict, exception: str):
        super().__init__()
        self.functions = functions
        self.exception = exception
        self.cmd_func = Functions(commands=functions)       
        self.cmd_func.update_functions() 
    
    def search_in_commands(self, text_recognizer: str) -> dict:
        print(text_recognizer)
        for each_func in self.functions:
            if each_func.lower() in text_recognizer.lower():
                return dict(
                    message=self.functions[each_func]["message"], 
                    result=True, 
                    index=each_func,
                    query=text_recognizer)
        else:
            return dict(message=self.exception, result=False)
    
    def exec_command(self, func_index: object, parametres_ext: dict) -> bool:
        try:
            self.cmd_func.function_identifier(func_index=func_index,parametres_ext=dict(query=parametres_ext['query'],texttotype=parametres_ext['texttotype']))
        except Exception as ex:
            print(ex)        

class Transform():
    def __init__(self, sapi: str, content: list):
        super().__init__()
        self.sapi = sapi
        self.sapi_content = content
        self.spvoice_source = None

    def check_sapi(self) -> bool:
        return os.path.exists(self.sapi)

    def create_sapi(self) -> bool:
        open(file=self.sapi, mode="w+")
    
    def open_sapi(self) -> object:
        with open(file=self.sapi, mode="r", encoding="utf-8") as sp_source:
            self.spvoice_source = sp_source.read()
            sp_source.close()        
        return self
    
    def write_spvoice(self, message: str) -> object:
        try:
            index = len(self.spvoice_source.split("\n"))
            print(index, self.spvoice_source.split("\n"))
            self.sapi_content.insert(index-2, 'message_to_speak="{message}"'.format(message=message))
            with open(file=self.sapi, mode="w+", encoding="utf-8") as sp_source:
                for content in self.sapi_content:
                    if '()' in content:
                        arr_content = content.split("(")
                        arr_content.insert(1, '("sapi.spvoice"')
                        content = "".join(arr_content)  
                    if 'sapi_svoice.Speak' in content:
                        sp_source.write("%s"%content)
                    else:
                        sp_source.write("%s\n"%content)
                sp_source.close()                
        except Exception as e:
            print(e)
        return self
    
    def start_sapi(self) -> object:
        os.startfile(self.sapi)

with open(file="__config__.json", mode="r", encoding="utf-8") as config:
    config_file = object_notation.loads(config.read())
    config.close()

while True:
    if kb.is_pressed('n'):
        transform = Transform(sapi="sapi.vbs", content=config_file["Speecher"]["Content"])
        if not transform.check_sapi():
            transform.create_sapi()
        voice_recognition = Recognition(functions=config_file["Speecher"]["Functions"],exception=config_file["Speecher"]["Exception"])
        voice_recognition.microphone(transform=transform)


