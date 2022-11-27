import hashlib

plaintext = "foobar"  #This time we have a string as input
theHash = hashlib.md5(plaintext.encode()).hexdigest()  #Note we need to encode the string
print(theHash)
