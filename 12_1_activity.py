def main():
        for i in range(4):
                name='v'+str(i)
                locals()['v'+str(i)]=i
        print (locals()['v1'],locals()['v2'],locals()['v3'])


    
    

if __name__ == '__main__':
	main()






