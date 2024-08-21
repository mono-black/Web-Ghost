from get_page import find_element

def callableF():
     print("\nshould be like : (https://www.somethigs/smt)")
     url = input("Enter Url : ")
     print("\n1- id")
     print("2- class")
     print("3- name")
     print("4- method")
     print("5- action")
     print("6- type")
     selector = str(input("Enter : "))

        
     if selector == "1":
          attr = 1
     elif selector == "2":
          attr = 2
     elif selector == "3":
          attr = 3
     elif selector == "4":
          attr = 4
     elif selector == "5":
          attr = 5
     elif selector == "6":
          attr = 6
     else :
          print("huh???!")
     E_Name = input("Enter keyworld to find : ")
     try :
          value = find_element(attr=attr,url=url,value=E_Name)
          for i in value:
               print(i)
     except:
        print("\n--->> Something went wrong when opening the url or wrong url\n")
          
     
        
        
        