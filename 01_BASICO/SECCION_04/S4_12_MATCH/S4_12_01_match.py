serie = "N-010"

match serie:
    case "N-01":
        print ("Samsung")
    case "N-02":
        print ("Nokia")
    case "N-03":
        print ("Motorola")
    case _:
        print ("el producto no existe")
        
        
cliente = {"nombre": "federico", "edad":45,"ocupacion":"instructor"}
pelicula={"titulo": "matrix", "ficha_tecnica":{"protagonista":"keanu reeves","director":"lana y lilly wachowski"}}

elementos = [cliente,pelicula,"libro"]
for e in elementos:
    match e:
        case {"nombre": nombre,"edad":edad,"ocupacion":ocupacion}:
            print("es un cliente")
            print(nombre,edad,ocupacion)
        case {"titulo":titulo, "ficha_tecnica":{"protagonista": protagonista,"director":director}}:
            print("es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("es un libro")
            
