import hashlib

string = "qwerty"
encoded = string.encode()
result = hashlib.sha256(encoded)

print (result.hexdigest())

#input the key in walletfiles. 
#https://www.bitaddress.org

#then check the adresse in block explorer

