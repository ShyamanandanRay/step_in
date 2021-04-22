fruits = {"apple": 2, "orange" : 3, "tangerine": 5}
dry_fruits = {"cashew": 3, "almond": 4, "pistachio": 6}

dictionary = {**dry_fruits, **fruits}
print(dictionary)