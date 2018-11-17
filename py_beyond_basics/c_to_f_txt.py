temperatures = [10, -20, -289, 100]

def c_to_f(t):
    if t < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = t * 9 / 5 + 32
        return str(f)


with open("temperatures.txt", "w") as file:
    for t in temperatures:
        file.write("\n%s" %c_to_f(t))
