path = "./test/test1.txt"
def openfile():
    with open(path,'a+') as f:
        str = "This  a  test!"
        f.write(str+"\n")
def readfile():
    with open(path,'r') as f:
        """ lines = f.readlines()
        for l in lines:
            print("read lines: {}".format(l)) """
        
        for l in f:
            print("read data: {}".format(l))
   


def main():
    #openfile()
    readfile()

if __name__ == '__main__':
    main()

