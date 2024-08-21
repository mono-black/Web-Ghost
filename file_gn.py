import os.path
from get_page import get

def callableGn():
    print("\nshould be like : (https://www.somethigs/smt)")
    url = input("Enter Url : ")
    filename = input("File Name : ")
    elements = get(url)
    i=0
    while True:
            
        if os.path.isfile(f"./WebGhost-{filename}-{i}.html"):
            i+=1
        else:
            f = open(f"WebGhost-{filename}-{i}.html", "wb")
            f.write(elements.encode("utf-8"))
            f.close()
            print("\nsir ! you have it now ...\n")
            break