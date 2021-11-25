from coincurve.keys import PrivateKey
import requests
import json
from bit.crypto import ECPrivateKey
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from time import sleep
from bit.format import bytes_to_wif, public_key_to_address

#pip install -r requirements.txt


found = False
count = 0
def generate_private_key():
    private_key = ECPrivateKey()
    return private_key

def start():

    if __name__ == "__main__":
            global found
            global count
            privkey = generate_private_key()
            #print("Public Address: "+public_key_to_address(privkey.public_key.format()))
            #print("Private Key: "+bytes_to_wif(privkey.secret, compressed=True))
            #check if it has activity
            wif = bytes_to_wif(privkey.secret, compressed=True) #private.wif(compressed=False) 
            z = public_key_to_address(privkey.public_key.format()).encode("utf-8")

            url = requests.get("https://blockstream.info/api/address/"+str(z.decode('utf-8')))
            data = json.loads(url.text)
            
            count = count + 1

            print(count)
            #print(data)
            if data['chain_stats']['funded_txo_count']>0:
                print(data['chain_stats']['funded_txo_count'])
                print("Wow active address found!!")
                print("Adresse: " + z.decode('utf-8'))
                print("Private Key: " + wif)
                f = open("foundkey.txt", "a") # the found key and address saved to "foundkey.txt"
                f.write("Adresse: " + z.decode('utf-8'))
                f.write("\n")
                f.write("Private Key: " + wif)
                f.close()


print("Working...")
while found == False:
    start()
