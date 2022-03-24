def replace(str, search, replace):
    while search in str:
        str=str[0:str.index(search)]+replace+str[str.index(search)+len(search):len(str)]
    return str

def readfile(name, length, datatype):
    l=[]
    file=open(name)
    for line in file:
        linedata=replace(line.rstrip(), "  ", " ").split(" ")[0:length]
        if linedata!=[""]:
            for i in range(len(linedata)):
                if datatype=="i":
                    linedata[i]=int(linedata[i])
                else:
                    linedata[i]=float(linedata[i])
            l.append(linedata)
    return l
 
if __name__=="__main__":
    try:
        open("clicks.txt")
        open("delays.txt")
        try:
            clicks=readfile("clicks.txt", 2, "i")
            delays=readfile("delays.txt", 1, "f")
            print(clicks)
            print(delays)
            if len(clicks)!=4:
                print("Warning: There should be 4 lines of content in the clicks.txt file")
            if len(delays)!=11:
                print("Warning: There should be 11 lines of content in the clicks.txt file")
        except:
            print("There is a mistake one of the text files (space before first variable, no space in between variables (tab doesnt count))")
    except:
        print("File(s) not found or named incorrectly")
    
    input()
    input()

