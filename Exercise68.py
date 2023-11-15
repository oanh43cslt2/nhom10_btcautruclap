while True :
    bit= input("Enter 8 bits (Enter to exit):")
    if bit=="" :
        break
    S=bit.count('1')+bit.count('0')
    if len(bit)==8 and S==8 :
        bit1=bit.count('1')
        if bit1 % 2 ==0 :
            print('Parity bit should be: 0')
        else :
            print('Parity bit should be: 1') 
             
    else :
        print("Error: Please enter exactly 8 bits.")
                  
            
         
         
         