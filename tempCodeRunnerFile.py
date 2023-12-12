speaker = win32com.client.Dispatch("SAPI.SpVoice")
while 1:
      print("Enter th word you wnt to speak it out by computer 56")
      s = input()
      speaker.Speak(s)
