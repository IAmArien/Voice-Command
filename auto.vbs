WScript.Sleep 1000
Set WshShell = WScript.CreateObject("WScript.Shell")
Dim Row
Dim LineLength
Set fso = CreateObject("Scripting.FileSystemObject")
Set dict = CreateObject("Scripting.Dictionary")
Set file = fso.OpenTextFile("texttotype.txt", 1)
Row = 0
Do Until file.AtEndOfStream
  line = file.Readline
  dict.Add Row, line
  Row = Row + 1
Loop
file.Close
For Each line in dict.Items
    LineLength = Len(line)
    For index = 0 To LineLength-1
        WshShell.SendKeys Mid(line,index+1,1)
        WScript.Sleep 1
    Next
Next