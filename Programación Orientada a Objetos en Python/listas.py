to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]
print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))
mix = ["uno",2,3.14, "true", [1,2,3]]
print(mix)
print(len(mix))
print("Primer elemto",mix[0])
print("segundo elemto",mix[1])
print("Ultimo elemto",mix[-1])
string = "Hola mundo"
print("Primer elemto",string[0])
print("segundo elemto",string[1])
print("Ultimo elemto",string[-1])
print(mix[2:-2])
print(mix)
mix.append("false")
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1,2,100.01,90.45,4,5]
print(numbers)
print("Mayor",max(numbers))
print("Mayor",max(numbers))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
print(numbers)




