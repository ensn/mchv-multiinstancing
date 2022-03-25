try:
    import settings
    if len(settings.delays)!=18:
        print("Warning: Delays should have 18 entrys")
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
