
def test(a,b,c=10,d=5,*args,**kwargs):
    print(a,b,c,d)
    print(type(args))
    for i in args:
        print(i)
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)

# test(1,2,5,6,7,8,name="mahesh",d=20,section="B",age=12,c=5)
y ={'i':1,'j':2,'k':3}
z=(4,5,6)
test(1,2,*z,**y)




# k=[(1,2,3),(2,3,4)]
# for a,b,c in k:
#     print(a,b,c)
