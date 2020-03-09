# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:53:58 2020

@author: Low Wei Hao
"""
from hashlib import sha256
from time import time
import uuid

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
        nonce=None
    else:
        index=index+1
        nonce=uuid.uuid4().hex

if index==0:
    data="first block"
    Hash=sha256('first block'.encode()).hexdigest()
    Pre_hash=None        
else:
    pre_hash=Hash
    Pre_hash=Hash
    data=tail("User_Detail.txt",5)
    change=listToString(data)
    combine=pre_hash+change+nonce
    Hash=sha256(combine.encode()).hexdigest()
    nonzero=len(Hash)-numZero(Hash)
    count=len(Hash)-nonzero
    time=0
    while count<14:
        nonce=uuid.uuid4().hex
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
       'timestamp':timestamp,
       'data':data,
       'nonce':nonce,
       'prehash':Pre_hash,
       }




with open('Block_Chain.txt', 'a') as f:
    print(blockchain, file=f)
file.close()

if index==0:
    with open("User_Detail.txt") as d:
        d.seek(0)
        string=d.read(1)
        if string:
            index=1
            nonce=uuid.uuid4().hex
            pre_hash=Hash
            Pre_hash=Hash
            data=tail("User_Detail.txt",5)
            change=listToString(data)
            combine=pre_hash+change+nonce
            Hash=sha256(combine.encode()).hexdigest()
            nonzero=len(Hash)-numZero(Hash)
            count=len(Hash)-nonzero
            time=0
            while count<14:
                nonce=uuid.uuid4().hex
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
                    'timestamp':timestamp,
                    'data':data,
                    'nonce':nonce,
                    'prehash':Pre_hash,
                    }
            with open('Block_Chain.txt', 'a+') as f:
                print(blockchain, file=f)
                file.close()

            

