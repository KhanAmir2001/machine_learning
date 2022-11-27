import time
import hashlib

def simpleCrack(wordlist, target):
    """
    Code to crack an md5 hash using a dictionary

    @param wordlist:  List of dictionary Words
    @param target:    The Hash we want to crack
    """
    pass  #Your code goes here.
    #def pcrack(target):

    fd = open("passwords.txt", "r")
    startTime = time.time()

    match = None
    #Loop through all items in the password List
    for item in fd:
        item = item.strip() #Remove New Lines
        #print ("Chekking {0}".format(item))
        #Create a hash for the item
        theHash = hashlib.md5(item.encode()).hexdigest()
        #Compare to our target
        if theHash == target:
            print ("Password Match found {0}".format(item))
            match = item[:-4]


    endTime = time.time()
    print ("Match is {0}".format(match))
    print ("Total of {0} Seconds".format(endTime - startTime))

target = "dd8fcb2c31ee2c6ebbc63f8cf22e7c16"  #Unknown Hash

if __name__ == "__main__":

    #Our word list
    wordlist = open("passwords.txt", "r")
    #Our Target Hash
    target = "dd8fcb2c31ee2c6ebbc63f8cf22e7c16"  #Unknown Hash


    startTime = time.time()
    simpleCrack(wordlist, target)
    endTime = time.time()
    print ("Total of {0} Seconds".format(endTime - startTime))