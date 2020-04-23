Dim message_to_speak
Dim sapi_svoice
Set sapi_svoice = CreateObject("sapi.spvoice")
message_to_speak="Opening Google Chrome Browser To Search, Please Wait!"
sapi_svoice.Speak message_to_speak
