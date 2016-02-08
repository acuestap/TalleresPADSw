def fibonacci(n):  
 a, b = 0, 1
 var = "1"

 while(n>1):
 	c = a + b 	
 	a = b;
 	b = c
 	var = var +"," + str(c)
 	n = n-1
 return var;
n = int(input("\nIngrese el numero de iteraciones: "))  
if(n>0):  
 a=fibonacci(n)  
 print ("\nResultado: "+a)
else:
 print ("\nResultado: 0")
