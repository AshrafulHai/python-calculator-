def add (a,b):
    result=a+b
    print ('a+b is' , result )
def sub (a,b):
    result=a-b
    print ('a-b is' , result )
def mul (a,b):
    result=a*b
    print ('a*b is' , result )  
def div (a,b):
    result=a/b
    print ('a/b is' , result )

x=int (input ('Enter ur first number:' ))
y=int (input ('Enter ur secound number:' ))
z= input ('Enter ur operation type:' )

if z=="+":
    add (x,y)
elif z=="-":
    sub (x,y)
elif z=="*":
    mul (x,y)
elif z=="/":
    div (x,y)
else :
    print ("No operation found")
