import requests




def main():
    ur1='http://www.cntour.cn/'
    strhtml=requests.get(ur1)
    print(strhtml.text)
    pass

if __name__=="__main__":
    main()