import linecache
import tkinter
import hashlib
import numpy as np
import os
import matplotlib.pylab as plt
def main():
        f=open("from.txt","r",encoding="utf-8")
        s1=f.read()
        f.close()
        s1=s1.replace('5','43')
        f=open("answer.txt","w",encoding="utf-8")
        f.write(s1)
        f.close()


    
    

if __name__ == '__main__':
	main()






