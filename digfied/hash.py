import hashlib

def hash_code(url):
    enc = hashlib.md5(url.encode())
    hsh = enc.hexdigest()
    return str(hsh)

def hash_comp(hash1, hash2):
    if str(hash1)==str(hash2):
        return 'equals'
    return 'non-equals'

def hash_read_data(file_text):
    datafile = ''
    url = ''
    if file_text.find(".hash") == -1:
        datafile = file_text
    else:
        url = file_text
        f = open(file_text)
        datafile = f.readline()
        f.close()
    datafile_clean1 = datafile.replace('hash : ', '')
    datafile_clean = datafile_clean1.replace("'","")
    return url,datafile_clean

def hash_read():
    print("Texto o url", end=': ')
    read = input()
    url, hash_text = hash_read_data(read)
    print('hash ('+url+'): ' + hash_text)
