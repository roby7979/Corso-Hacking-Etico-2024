mio_dizionario = {"nome": "Roberto", "Eta": 44, "Citta": "Barcellona"}

# print(type(mio_dizionario))
mio_dizionario["nome"] = "Marco"
print(mio_dizionario["nome"])
mio_dizionario["professione"] = "Programmatore"
del mio_dizionario["Eta"]
print(mio_dizionario)
if "Casa" in mio_dizionario:
    print("Questa chiave e' presente nel mio dizionario")
    
else:
    
    print("Questa chiave non e' presente nel dizionario")    
    
for  key, value  in mio_dizionario.items(): 
    print(f"Per la chiave {key} abbiamo il valore {value}")
    
# print(f"il numero di elementi dentro il mio dizionario e' {len(mio_dizionario)}")

# mio_dizionario.clear()
    
print(f"il numero di elementi dentro il mio dizionario e' {len(mio_dizionario)}")



quadrato = {x: x**2 for x in range(6)}
print(quadrato.keys())
print(quadrato.values())


mio_dizionario = {"nome": "Roberto", "Eta": 44, "Citta": "Barcellona"}
mio_dizionario2 = {"professione": "Programmatore", "Animali": "cane"}

mio_dizionario.update(mio_dizionario2)

print(mio_dizionario)

# print(mio_dizionario.get("nom", "non l ho trovata"))



my_dict = {
    "nome": "Roby",
    "hobbie": {"primo": "hacking", "secondo": "musica"},
    "eta": 44
}

# mio_dizionario = {"nome": "Roberto", "Eta": 44, "Citta": "Barcellona"}

# print(my_dict["hobbie"]["primo"])
for chiave, valore in my_dict.items():
    print(f"[{chiave}]: {valore}")





    