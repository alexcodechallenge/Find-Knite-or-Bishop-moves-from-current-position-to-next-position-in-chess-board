a = ['a','b','c','d','e','f','g','h']
b = [1,2,3,4,5,6,7,8]
for x in range(len(b), -1, -1):
    for i in a:
        if x==0:
            break
        print('{0}{1}'.format(i,x),end=' ')
        
    print('')    
        
