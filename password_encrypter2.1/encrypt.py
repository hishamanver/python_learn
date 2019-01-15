def generateEncryptionKey(key):
    encryptionKey = []
    for i in range(len(key)):
        encryptionKey = encryptionKey + [ord(key[i])*((-1)**i)]
    return encryptionKey

def generateEncryptionKeyOffset(key,start):
    encryptionKeyOffset = start
    for i in range(len(key)):
        if encryptionKeyOffset<510:
            encryptionKeyOffset += ord(key[i])
    if encryptionKeyOffset < 255:
        encryptionKeyOffset = generateEncryptionKeyOffset(key,encryptionKeyOffset)
    return encryptionKeyOffset

key = input("Input key: ")
encryptionKey = generateEncryptionKey(key)
encryptionKeyOffset = generateEncryptionKeyOffset(key, 0)
# print(encryptionKey)
# print(encryptionKeyOffset)

fileIn = open("testdata.txt")
data = (fileIn.read())
fileIn.close()

dataOut = []

for j in range(0,len(data),len(encryptionKey)):
    for k in range(len(encryptionKey)):
        try:
            dataOut = dataOut + [ord(data[j+k])+encryptionKey[k]+encryptionKeyOffset] 
        except:
            continue

dataOut = ''.join(str(k) for k in dataOut)

fileOut =open("crypt.txt", "w")
fileOut.write(dataOut)
fileOut.close()

print(dataOut)
