

def Primos_hasta(num=250):
    Primos = []
    No_Primo = []
    for i in range(num+1):
        Es_Primo = True
        if i == 1:
            Es_Primo = False
        elif i == 0:
            Es_Primo = False
        elif i >2:
            for primo in Primos:
                if i%primo == 0:
                    Es_Primo = False
        if Es_Primo == True:
            Primos.append(i)
        else:
            No_Primo.append(i)
    return(Primos)
    
Lista_Primos = Primos_hasta(int(input('Dime un numero y te diré todos los primos que hay hasta él: ')))
print(Lista_Primos)
