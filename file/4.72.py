from datetime import datetime

with open("4.72\\file1.txt") as file1:
    data = file1.read()
    with open("4.72\\file2.txt") as file2:
        data = data + "\n" + file2.read()
        with open("4.72\\file3.txt") as file3:
            data = data + "\n" + file3.read()
            with open(datetime.now().strftime("4.72\\%Y-%m-%d-%H-%M-%S-%f.txt"), "w") as fileOut:
                fileOut.write(data)

#Try glob2.glob("*.txt")