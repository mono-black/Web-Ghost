from get_page import find_element

def callableU():
    print("\nshould be like : (https://www.somethigs/smt)")
    url = input("Enter Url : ")
    try:
        elements = find_element(attr="href",url=url,value="")
        print("\n")
        for i in elements:
            print("Title : " + i.text)
            print("URL : " + i["href"])
        print("\n")
    except:
        print("\n--->> Something went wrong when opening the url or wrong url\n")