data = ["?", "?", "?", "?", "?", "?"]

for i in range(6):
    data[i] = "_"
    print(f'''
    {data[0]}x + {data[1]}y = {data[2]}
    {data[3]}x + {data[4]}y = {data[5]}''')
    data[i] = input("Insert number: ")

W = (float(data[0]) * float(data[4])) - (float(data[3]) * float(data[1]))
Wx = (float(data[2]) * float(data[4])) - (float(data[5]) * float(data[1]))
Wy = (float(data[0]) * float(data[5])) - (float(data[3]) * float(data[2]))

if(W==0):
    print("Sprzeczne")
else:
    x = Wx / W
    y = Wy / W
    print(f"x: {x} \ny: {y}")