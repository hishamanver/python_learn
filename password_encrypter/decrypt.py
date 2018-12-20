def generateEncryptionKey(key):
    encryptionKey = []
    for i in range(len(key)):
        encryptionKey = encryptionKey + [ord(key[i])*((-1)**i)]
    return encryptionKey

key = input("Input key: ")
encryptionKey = generateEncryptionKey(key)
# print(encryptionKey)

fileIn = open("crypt.txt")
data = (fileIn.read())
fileIn.close()

dataOut = []

for j in range(0,len(data),3*len(encryptionKey)):
    for k in range(len(encryptionKey)):
        try:
            dataOut = dataOut + [chr(int(data[j+k*3]+data[j+1+k*3]+data[j+2+k*3])-encryptionKey[k]-255)]   
        except:
            continue

dataOut = ''.join(str(k) for k in dataOut)


fileOut =open("decrypt.txt", "w")
try:
    fileOut.write(dataOut)
except: print("Incorrect key!")
fileOut.close()

print(dataOut)

