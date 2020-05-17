import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

a=0.5       #learning Rate
w13=0.5     #weight
w14=0.9
w23=0.4
w24=1.0
w35=-1.2
w45=1.1
bias3=0.8   #bias = threshold level
bias4=-0.1
bias5=0.3


Loop = 0
while True:
    def forward():
        global y3,y4,y5,del5,e
    
        y3=sigmoid(x1*w13 + x2*w23 - bias3)
        y4=sigmoid(x1*w14 + x2*w24 - bias4)
        y5=sigmoid(y3*w35 + y4*w45 - bias5)
        
        e=yd5-y5                #e = error  ,  yd = desired output
        del5=y5*(1-y5)*e        #del = gradient of error
        return
    
    def backward():
        global w35,w45,w13,w14,w23,w24,bias3,bias4,bias5
    
        cw35=a*y3*del5          #cw = change of weight
        cw45=a*y4*del5
        cbias5=a*-1*del5        #cbias = change of threshold level
        
        del3=y3*(1-y3)*del5*w35
        del4=y4*(1-y4)*del5*w45
        
        cw13=a*x1*del3
        cw23=a*x2*del3
        cbias3=a*-1*del3
        cw14=a*x1*del4
        cw24=a*x2*del4
        cbias4=a*-1*del4
        
        w13=w13+cw13
        w14=w14+cw14
        w23=w23+cw23
        w24=w24+cw24
        w35=w35+cw35
        w45=w45+cw45
        bias3=bias3+cbias3
        bias4=bias4+cbias4
        bias5=bias5+cbias5
        
        return
    
    print('Loop: ',Loop)     
    x1=26           #XOR-gate
    x2=20
    yd5=0
    forward()
    backward()
    '''
    print('e1 =',e)
    print('w13 = ',w13)
    print('w14 = ',w14)
    print('w23 = ',w23)
    print('w24 = ',w24)
    print('w35 = ',w35)
    print('w45 = ',w45)
    print('bias3 = ',bias3)
    print('bias4 = ',bias4)
    print('bias5 = ',bias5)
    '''
    e1=e*e          #Square Error

    #print('y5-11 = ',y5)
    
    x1=22            #XOR-gate
    x2=25
    yd5=1
    forward()
    backward() 
    '''
    print('e2 =',e)
    print('w13 = ',w13)
    print('w14 = ',w14)
    print('w23 = ',w23)
    print('w24 = ',w24)
    print('w35 = ',w35)
    print('w45 = ',w45)
    print('bias3 = ',bias3)
    print('bias4 = ',bias4)
    print('bias5 = ',bias5)
    '''
    e2=e*e         #Square Error
    #print('y5-10 = ',y5)
    
    x1=19           #XOR-gate
    x2=18
    yd5=1
    forward()
    backward() 
    '''
    print('e3 =',e)
    print('w13 = ',w13)
    print('w14 = ',w14)
    print('w23 = ',w23)
    print('w24 = ',w24)
    print('w35 = ',w35)
    print('w45 = ',w45)
    print('bias3 = ',bias3)
    print('bias4 = ',bias4)
    print('bias5 = ',bias5)
    '''
    e3=e*e          #Square Error
    #print('y5-01 = ',y5)
    
    x1=14           #XOR-gate
    x2=20
    yd5=0
    forward()
    backward()  
    '''
    print('e4 =',e)
    print('w13 = ',w13)
    print('w14 = ',w14)
    print('w23 = ',w23)
    print('w24 = ',w24)
    print('w35 = ',w35)
    print('w45 = ',w45)
    print('bias3 = ',bias3)
    print('bias4 = ',bias4)
    print('bias5 = ',bias5)
    '''
    #print('y5-00 = ',y5)
    e4=e*e          #Square Error
    
    SSE=e1+e2+e3+e4     #Sum of Square Error
    
    print('SSE = ',SSE)
    print('----------------------------')
    
    Loop +=1
    
    if SSE <= 0.001:
        print('w13 = ',w13)
        print('w14 = ',w14)
        print('w23 = ',w23)
        print('w24 = ',w24)
        print('w35 = ',w35)
        print('w45 = ',w45)
        print('bias3 = ',bias3)
        print('bias4 = ',bias4)
        print('bias5 = ',bias5)
        break     