# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:53:58 2020

@author: Low Wei Hao
"""
from hashlib import sha256
from time import time
import random

file=open("Block_Chain.txt","a+")
timestamp=time()

def numZero(a):
    Zeros='0'
    result=0
    for char in a:
        if char in Zeros:
            result=result+1
    return result

def listToString(s):      
    str1 = ""  
    for ele in s:  
        str1 += ele   
    return str1

def tail(file, n=1, bs=1024):
    f = open(file)
    f.seek(0,2)
    l = 1-f.read(1).count('\n')
    B = f.tell()
    while n >= l and B > 0:
            block = min(bs, B)
            B -= block
            f.seek(B, 0)
            l += f.read(block).count('\n')
    f.seek(B, 0)
    l = min(l,n)
    lines = f.readlines()[-l:]
    f.close()
    return lines

with open("Block_Chain.txt") as f:
    f.seek(0)
    string=f.read(1)
    if not string:
        index=0
        nonce="0"
    else:
        check=tail("Block_Chain.txt")
        check=listToString(check)
        index=check[10]
        index=int(index)
        index=index+1
        nonce=str(random.randint(0,10000000000)+int(timestamp)*random.randint(0,9))
        Pre_HASH=check[22:86]
        
if index==0:
    data="first block"
    Hash=sha256('first block'.encode()).hexdigest()
    Pre_hash=None        
else:
    pre_hash=Hash
    Pre_hash=Hash
    data=tail("User_Detail.txt",5)
    data=listToString(data)
    combine=pre_hash+data+nonce
    Hash=sha256(combine.encode()).hexdigest()
    nonzero=len(Hash)-numZero(Hash)
    count=len(Hash)-nonzero
    time=0
    while count<14:
        nonce=str(random.randint(0,10000000000)+int(timestamp)*random.randint(0,9))
        Hash=sha256(combine.encode()).hexdigest()
        time=time+1
        pre_hash=Hash
        if time>50000:
            Hash=sha256(combine.encode()).hexdigest()
            pre_hash=Hash
            break

blockchain={
       'index':index,
       'hash':Hash,
       'prehash':Pre_hash,       
       'timestamp':timestamp,
       'data':data,
       'nonce':nonce,
       }

if index!=0:
    if Pre_hash!=Pre_HASH:
        print("ERROR")
        exit()

with open('Block_Chain.txt', 'a+') as f:
    print(blockchain, file=f)
    file.close()

    


if index==0:
    with open("User_Detail.txt") as d:
        d.seek(0)
        string=d.read(1)
        if string:
            index=1
            nonce=str(random.randint(0,10000000000)+int(timestamp)*random.randint(0,9))
            pre_hash=Hash
            Pre_hash=Hash
            data=tail("User_Detail.txt",5)
            data=listToString(data)
            combine=pre_hash+data+nonce
            Hash=sha256(combine.encode()).hexdigest()
            nonzero=len(Hash)-numZero(Hash)
            count=len(Hash)-nonzero
            time=0
            while count<14:
                nonce=str(random.randint(0,10000000000)+int(timestamp)*random.randint(0,9))
                Hash=sha256(combine.encode()).hexdigest()
                time=time+1
                pre_hash=Hash
                if time>50000:
                    Hash=sha256(combine.encode()).hexdigest()
                    pre_hash=Hash
                    break
            blockchain={
                    'index':index,
                    'hash':Hash, 
                    'prehash':Pre_hash,
                    'timestamp':timestamp,
                    'data':data,
                    'nonce':nonce,
                    }
            with open('Block_Chain.txt', 'a+') as f:
                print(blockchain, file=f)
                file.close()
            

