#! /usr/bin/env python

import hashlib
import os
import re
import time

ptc_types = ['CHR', 'COL', 'GRP', 'MEM', 'PRG', 'SCR']
validchars = re.compile(b'[0-9A-Z_]+(?=\x00*$)')

print('PetitRepo Assistant v1.0')

if not os.path.isdir('ptc'):
    os.mkdir('ptc')

if not os.path.isdir('raw'):
    os.mkdir('raw')

for filename in os.listdir('ptc'):
    with open('ptc/' + filename, 'rb') as file:
        if not file.read(4) == b'PX01':
            print('File "' + filename + '" is not a valid PTC file. Skipping...')
            continue
        
        file.seek(12)
        ptc_name = file.read(8)
        ptc_name = validchars.match(ptc_name)
        if ptc_name is None:
            print ('Internal file name of PTC file "' + filename + '" is invalid. Skipping...')
            continue
        ptc_name = ptc_name.group().decode("ascii")
        
        md5_hash = hashlib.md5()
        file.seek(20)
        ptc_hash = file.read(16)
        ptc_data = file.read()
        ptc_pieced = b'PETITCOM' + ptc_data
        md5_hash.update(ptc_pieced)
        if not ptc_hash == md5_hash.digest():
            print('Internal MD5 hash does not match actual hash of contents of PTC file "' + filename + '". Skipping...')
            continue
        
        file.seek(45)
        ptc_type = file.read(3)
        ptc_type = ptc_type.decode("ascii")
        if not ptc_type in ptc_types:
            print('Invalid internal file type for PTC file "' + filename + '". Skipping...')
            continue
    
    if not os.path.isdir('raw/' + ptc_type):
        os.mkdir('raw/' + ptc_type)
    
    with open('raw' + '/' + ptc_type + '/' + ptc_name, 'wb') as file:
        file.write(ptc_data)
        
        print('Successfully processed "' + filename + '"!')

time.sleep(5)
