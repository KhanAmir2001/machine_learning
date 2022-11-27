import hashlib

def simpleSalt(plaintext):
    return "{0}SALT".format(plaintext)


plaintext = "jimjar"
salted=simpleSalt(plaintext)
print(salted)
# Salted is now "foobarSALT"
# doHashing(salted)