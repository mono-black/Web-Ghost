from get_page import get

def callablePg():
        print("\nshould be like : (https://www.somethigs/smt)")
        url = input("Enter Url : ")
        try:
                elements = get(url)
                print(elements)
        except: 
                print("\n--->> Something went wrong when opening the url or wrong url\n")
        