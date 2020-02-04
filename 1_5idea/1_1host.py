import linecache
import tkinter
import hashlib
import os
class account:
    permission=0
    def __init__(self,ID=000000,passward=000000,belong=0):
        self.ID=ID
        self.passward=passward
        self.belong=belong
    def add(self):
        p3="teacher\\t.txt"
        p = "product\\p" + self.ID + ".txt"
        p2 = "allow\\a" + self.ID + ".txt"
        try:
            solution = "log\\" + self.ID + ".txt"
            f = open(solution, "r", encoding="utf-8")
            print("account existed:")
            return 0
        except IOError:
            pass
        if len(self.ID)>=10 or len(self.ID)<=7:
            print("please use your ID number to register!")
            return 0
        for x in self.ID:
            if x<'0' or x>'9':
                print("please use your ID number to register!")
                return 0
        m=hashlib.sha1()
        byte='1'.join(format(ord(x),'b')for x in self.passward)
        m.update(byte.encode())
        str=m.hexdigest()+'\n'+self.belong
        text_create(self.ID,str)
        f = open(p3, "a", encoding="utf-8")
        file = open(p, 'w')
        file = open(p2, 'w')
        f.writelines(self.ID+"\n")
        f.close()
        print('register successfully')
        self.permission=1
        return 1
    def check(self):
        try:
            m = hashlib.sha1()
            solution="log\\"+self.ID+".txt"
            f = open(solution, "r", encoding="utf-8")
            str1=linecache.getline(solution,1)
            byte = '1'.join(format(ord(x), 'b') for x in self.passward)
            m.update(byte.encode())
            str = m.hexdigest()+'\n'
            if str==str1:
                self.permission=1
                print("you've logged in!")
                return 1
            else:
                print("wrong passward!")
            conclude=f.read()
        except IOError:
            print("wrong account!")
            return 0
    def add_product(self,name=0,amount1=0,net_add=0,price=0,others=0,belong=0):
        p = "product\\p" + self.ID + ".txt"
        p2="allow\\a"+self.ID+".txt"
        try:
            if(os.path.exists(p)==False):
                text_create2(p, '')
            if (os.path.exists(p2) == False):
                text_create2(p2, '')
            f = open(p, "r", encoding="utf-8")
            data = f.read()
            count=data.count('\n')
            print(count)
            f = open(p, "a", encoding="utf-8")
            amount=str(count+1)
            f.writelines(amount+'\t'+name+'\t'+amount1+'\t'+net_add+'\t'+price+'\t'+belong+'\t'+others+'\n')
            f.close()
            f = open(p2, "a", encoding="utf-8")
            f.writelines('0'+'\t'+amount+'\n')
        except IOError:
            text_create2(p, '0')
    def look_for_stu(self):
        p = "product\\p" + self.ID + ".txt"
        p2="allow\\a"+self.ID+".txt"
        f = open(p, "r", encoding="utf-8")
        f2= open(p2, "r", encoding="utf-8")
        data = f.read()
        count=data.count('\n')
        f = open(p, "r", encoding="utf-8")
        b=f.readlines()
        a=f2.readlines()
        for x in range(count):
            if a[x][0]=='0':
                 print(b[x])
        f.close()
    def look_for_tea(self,belong=0):
        p3="teacher\\t.txt"
        f3=open(p3, "r", encoding="utf-8")
        rl3=f3.readlines()
        count3=0
        for x in range(len(rl3)-1):
            str3=rl3[x].replace('\n','')
            p = "product\\p" + str3 + ".txt"
            p2 = "allow\\a" + str3 + ".txt"
            f = open(p, "r", encoding="utf-8")
            f2=open(p2,"r",encoding="utf-8")
            b2=f2.readlines()
            b=f.readlines()
            for y in range(len(b)-1):
                if b2[y][0]=='0':
                    if b[y][b[y].rfind('\t')-1]==str(belong):
                        count3+=1
                        f22= open(p2, "w", encoding="utf-8")
                        by=b[y].replace('\n','')
                        print(str3,count3,by)
                        allow=input("1 or 0 ? >")
                        if allow=='1':
                            b2[y]=b2[y].replace('0','1')
                        f22.write("".join(b2))
        pass
def text_create(name, msg):
	path = "log\\"  # 新创建的txt文件的存放路径
	full_path = path+name + '.txt'
	file = open(full_path, 'w')
	file.write(msg)
	file.close()
def text_create2(name, msg):
	full_path = name
	file = open(full_path, 'w')
	file.write(msg)
	file.close()
def main():
    a1= account('18402218','1008611','0')
    a1.add()
    a1.check()
    ''''
    name=input("name>")
    net_add=input("net>")
    price=input("price>")
    others=input("others>")
    belong=input("belong 0 or 1>")
    amount=input('amount>')
    a1.add_product(name,amount,net_add,price,others,belong)
    '''
    a1.look_for_tea()
    '''
    try:
        f=open("file\\mtxt4.txt","a",encoding="utf-8")
        include=account+" "+passward
        f.writelines(include+"\n")
    except IOError:
        text_create('mtxt4', 'Hello world!')
    f.close()
    '''


if __name__ == '__main__':
	main()



