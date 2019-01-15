temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c* 9/5 + 32
        return f
with open("file.txt", "w") as file:    
    for t in temperatures:
        converted = c_to_f(t)
        if type(converted) == float:
            file.write(str(c_to_f(t)))
            file.write("\n")
