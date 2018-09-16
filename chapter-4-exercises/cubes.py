cubes = []
for i in range(1, 11):
    cube = i**3
    cubes.append(cube)
print(cubes)

cubes = [value**3 for value in range(1, 11)]
for i in cubes:
    print(i)