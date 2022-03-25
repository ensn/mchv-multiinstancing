import settings
try:
    if len(settings.delays)!=16:
        print("Warning: Delays should have 16 entrys")
    if len(settings.clicks)!=6:
        print("Warning: clicks should have 6 entrys")
    print("No errors")
    input()
    input()
except:
    print("There was an error")
    input()
    input()
    raise
