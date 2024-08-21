from file_gn import callableGn
from show_pg import callablePg
from finder import callableF
from u_finder import callableU
print("""
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·      ▄▄ •  ▄ .▄      .▄▄ · ▄▄▄▄▄
██· █▌▐█▀▄.▀·▐█ ▀█▪    ▐█ ▀ ▪██▪▐█▪     ▐█ ▀. •██  
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄    ▄█ ▀█▄██▀▐█ ▄█▀▄ ▄▀▀▀█▄ ▐█.▪
▐█▌██▐█▌▐█▄▄▌██▄▪▐█    ▐█▄▪▐███▌▐▀▐█▌.▐▌▐█▄▪▐█ ▐█▌·
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀     ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀▀▀▀  ▀▀▀   
by mono-black
----------------------------------------------------
""")



while True :
    print("1- get webpage elements as file")
    print("2- show webpage elements")
    print("3- find in page")
    print("4- link finder")
    print("5- quit")
    x = str(input("\nEnter :"))

    if(x == '1'):
        callableGn()
    elif(x == '2'):
        callablePg()
    elif(x == '3'):
        callableF()
    elif(x == '4'):
        callableU()
    elif(x == '5'):
        break
    else:
        pass