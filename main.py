# data = ["?", "?", "?", "?", "?", "?"]
#
# for i in range(6):
#     data[i] = "_"
#     print(f'''
#     {data[0]}x + {data[1]}y = {data[2]}
#     {data[3]}x + {data[4]}y = {data[5]}''')
#     data[i] = input("Insert number: ")
#
# W = (float(data[0]) * float(data[4])) - (float(data[3]) * float(data[1]))
# Wx = (float(data[2]) * float(data[4])) - (float(data[5]) * float(data[1]))
# Wy = (float(data[0]) * float(data[5])) - (float(data[3]) * float(data[2]))
#
# if(W==0):
#     print("Sprzeczne")
# else:
#     x = Wx / W
#     y = Wy / W
#     print(f"x: {x} \ny: {y}")

class Uklad:
    def __init__(self, d1, d2, d3, d4, d5, d6):
        self.data = [d1, d2, d3, d4, d5, d6]

    def licz(self):
        W = (float(self.data[0]) * float(self.data[4])) - (float(self.data[3]) * float(self.data[1]))
        Wx = (float(self.data[2]) * float(self.data[4])) - (float(self.data[5]) * float(self.data[1]))
        Wy = (float(self.data[0]) * float(self.data[5])) - (float(self.data[3]) * float(self.data[2]))

        if(W==0):
            if(Wx == 0)and(Wy == 0):
                print("Nieskończenie wiele")
            else:
                print("Sprzeczne")
        else:
            x = Wx / W
            y = Wy / W
            print(f"x: {x} \ny: {y}")

uklad1 = Uklad(7, 2, 1, 3, 4, 2) # x=0 i y=1/2
uklad2 = Uklad(1, 2, 3, 1, 2, 3)
uklad3 = Uklad(1, 2, 3, 1, 2, 2)

uklad1.licz()
uklad2.licz()
uklad3.licz()