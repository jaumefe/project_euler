# Problema 22
Alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
nom = '/home/jaume/ProjectEuler/p022_names.txt'
res = 0

# Obrim el fitxer i extraiem el contingut
fichero = open(nom)
contingut = fichero.read()
fichero.close()

# Acondicionem el contingut per a poder llegir-lo com si fora una matriu
contingut = contingut.replace('"', '')
noms = contingut.split(',')

# Ordenem alfabèticament
noms.sort()

for i in range(len(noms)):
    sumNom = 0  # Variable en la que guardem la suma de la posició d'una lletra en l'alfabet
    for j in range(len(noms[i])):
        for k in range(len(Alfabet)):
            if noms[i][j] == Alfabet[k]:
                sumNom += k + 1
                break
    res += sumNom * (i+1)
print(res)
