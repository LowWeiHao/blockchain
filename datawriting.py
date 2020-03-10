# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 09:50:50 2020

@author: Low Wei Hao
"""
from datetime import datetime

file= open("User_Detail.txt","a+")
option=input("Do you want to start a new transition? Yes/No\n")
option=option.lower()

while option=="yes":
    From=str(input("Please input your user name: "))
    To=str(input("Please input your trade destination: "))
    Amount=str(input("Please input amount of this transition: "))
    Timestamp=str(datetime.now())
    print("Transition complete at",Timestamp)
    file.write("From: ")
    file.write(From)
    file.write("\n")
    file.write("To: ")
    file.write(To)
    file.write("\n")
    file.write("Amount: ")
    file.write(Amount)
    file.write("\n")
    file.write(Timestamp)
    file.write("\n\n")  
    file.close()
    exec(open('blockchain.py').read())
    file= open("User_Detail.txt","a+")
    option=input("Do you want to start a new transition? Yes/No\n")
    option=option.lower()
    if option=="no":
        file.close()
        break
