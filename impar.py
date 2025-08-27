def tipoNum(num):  
       
    if num % 2 == 0:                
        return 'numero é par'
    else:        
        return 'numero é impar'

valor = int(input("informe o numero ") )

print(tipoNum(valor))