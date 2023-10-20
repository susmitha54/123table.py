#the following example uses 1 to 5.
'''
     1  2  3  4  5        0
  ********************    1 
1 |  1  2  3  4  5        2
2 |  2  4  6  8 10        3 
3 |  3  6  9 12 15        4    
4 |  4  8 12 16 20        5
5 |  5 10 15 20 25        6

0 1  2  3  4  5  6

'''
for row in range(7):
    for column in range(7) :
      if((column==0 and row==0)or(column==1 and row==0) or(column==0 and row==1)):
        print(' ',end=' ')
      elif(row==0):
        print(repr(column-1).rjust(2),end='  ')
      elif(row==1 ):
        print('****',end='')  
      elif(column==0):
        print(repr(row-1).rjust(2),end=' ')  
      elif ( column==1):
        print('|',end=' ')
      elif(column==2) :
        print(row-1,end='  ') 
      elif(row==2):
        print(repr((column*1)-1).rjust(2),end='  ')  
      elif(row==3):
        print(repr((column*2)-2).rjust(2),end='  ')  
      elif(row==4):
        print(repr((column*3)-3).rjust(2),end='  ') 
      elif(row==5):
        print(repr((column*4)-4).rjust(2),end='  ')  
      elif(row==6):
        print(repr((column*5)-5).rjust(2),end='  ')         
      
    print()