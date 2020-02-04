import linecache
def text_create(name, msg):    
	path = "file\\"  # 新创建的txt文件的存放路径    
	full_path = path+name + '.txt'      
	file = open(full_path, 'w')  
	file.write(msg)   
	file.close() 

def main():
	account=input("account>")
	passward=input("passward>")

	try:
		f=open("file\\mtxt4.txt","a",encoding="utf-8")
		include=account+" "+passward
		f.writelines(include+"\n") 
	except IOError:
		text_create('mtxt4', 'Hello world!')
	
	f.close()




if __name__ == '__main__':
	main()

