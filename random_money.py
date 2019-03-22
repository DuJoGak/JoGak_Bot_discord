import random as rd
import discord

def money_ready():
    global f
    f=open("Users.txt",'a+')

def db_read():
    global ulist
    #ulist=f.
def signup(uname):
    print(uname)
    money_ready()
    f.write(str(uname)+" "+"0")
    return 0
    
def get_money():
    money=rd.randint(500,50000)
    
