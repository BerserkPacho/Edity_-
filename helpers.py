import hashlib 
def hash(string):
    hash =  hashlib.md5(string.encode())
    hash = hash.hexdigest() 
    return hash
