def listdata():
    list1 = ['hello','world']
    list2 = ['2','3','1']
    print('list1:{}'.format(list1))
    print('list2:{}'.format(list2))

    for i,l in enumerate(list1):
        print('[{}] is {}'.format(i,l))

    for l in list2:
        print("list2: {}".format(l))

    print("sorted: {}".format(sorted(list2)))
    list2.sort(reverse=True)
    print("sort: {}".format(list2))

def tupledata():
    t1 = (1,2,3,4,5)
    t2 = ('abc','ddd')
    for i in range(len(t1)):
        print('[{}] is {}'.format(i,t1[i]))

def dicdata():
    d1 = {'aaa':123,'bbb':456}
    for k in d1.keys():
        print ("key:"+k)
    
    for v in d1.values():
        print ("value: {}".format(v))

    for k,v in d1.items():
        print ("key:{},v:{}".format(k,v))
   
def main():
    listdata()
    tupledata()
    dicdata()

if __name__ == '__main__':
    main()