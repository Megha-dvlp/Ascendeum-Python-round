def alpha_diamond(n):
    for i in range(1,n+1):
        
        alpha="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        for j in alpha:
            print(" "*(n-i), end ="")
            print(str(alpha[:(2*i-1)])+" ")
            break
            
    for i in range(n-1,0,-1):
        for j in alpha:
            print(" "*(n-i), end ="")
            print(str(alpha[:(2*i-1)]+" "))
            break
            
        
    
alpha_diamond(3)