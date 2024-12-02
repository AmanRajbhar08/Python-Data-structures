#initalise empty dictonary
squares={}

#input for the number till where we want to genrate sqaure 
n=int(input("Enter the number of to generate sqaure till "))

#loop for genrating sqaures
for i in range(1,n+1):
    squares[i]=i*i
 
#printing the sqaure dictionary    
for key,value in squares.items():
    print(f"{key}:{value}")    

