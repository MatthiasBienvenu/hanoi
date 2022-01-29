Lstrats = [["AC"]]

#inverser CB puis AC puis inverser AB 

for n in range(int(input("nombre de palets:"))-1):
    
    Ls = Lstrats[n] + ["AC"] + Lstrats[n]
    
    #inversement CB
    for chaineIndice in range(0, 2**(n+1)-1):
        L = list(Ls[chaineIndice])
        for carIndice in range(2):
            if Ls[chaineIndice][carIndice] == "C":
                L[carIndice] = "B"
            elif Ls[chaineIndice][carIndice] == "B":
                L[carIndice] = "C"
        Ls[chaineIndice] = L[0] + L[1]
    
    #inversement AB
    for chaineIndice in range(2**(n+1), 2**(n+2)-1):
        L = list(Ls[chaineIndice])
        for carIndice in range(0, 2):
            if Ls[chaineIndice][carIndice] == "A":
                L[carIndice] = "B"
            elif Ls[chaineIndice][carIndice] == "B":
                L[carIndice] = "A"
        Ls[chaineIndice] = L[0] + L[1]
        
    Lstrats.append(Ls)
    print(Ls)
print(Lstrats)