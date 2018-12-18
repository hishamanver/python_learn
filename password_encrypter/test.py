def generateEncryptionKey(key):
    encryptionKey = []
    for i in range(len(key)):
        encryptionKey = encryptionKey + [ord(key[i])]
    return encryptionKey

key = input("Input key: ")
encryptionKey = generateEncryptionKey(key)

fileIn = open("testdata.txt")
data = (fileIn.read())
fileIn.close()

dataOut = []
for j in range(len(data)):
    for k in range(len(encryptionKey)):
        dataOut = dataOut + [ord(data[j])+encryptionKey[k]]
AA
dataOut = ''.join(str(k) for k in dataOut)

fileOut =open("crypt.txt", "w")
fileOut.write(dataOut)
fileOut.close()

print(len(data))

