def generateEncryptionKey(key):
    encryptionKey = []
    for i in range(len(key)):
        encryptionKey = encryptionKey + [ord(key[i])*((-1)**i)]
    return encryptionKey

key = input("Input key: ")
encryptionKey = generateEncryptionKey(key)
# print(encryptionKey)

fileIn = open("testdata.txt")
data = (fileIn.read())
fileIn.close()

dataOut = []

for j in range(0,len(data),len(encryptionKey)):
    for k in range(len(encryptionKey)):
        try:
            dataOut = dataOut + [ord(data[j+k])+encryptionKey[k]+255] 
        except:
            continue

dataOut = ''.join(str(k) for k in dataOut)

fileOut =open("crypt.txt", "w")
fileOut.write(dataOut)
fileOut.close()

print(dataOut)
