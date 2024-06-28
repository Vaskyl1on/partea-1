
#def login(nume,prenume,parola,parola2):
#    nume=(input("Numele"))
#    prenume=(input("Prenumele"))
#    parola=(input("Parola"))
#    parola2=(input("Repeta parola"))
#        if parola == parola2:
#            print("Contul dumneavoatra este inregistrat")
#        else :
#            print("a aparut o greseala la repetarea parolii")
f=open("test.txt","r")
for line in f:
    print(line,end="")
#print(f.read())
#print(f.readlines())
f.close()
