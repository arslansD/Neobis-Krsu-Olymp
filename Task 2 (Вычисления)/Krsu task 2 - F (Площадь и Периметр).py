user_input=input("").split()
user_input=list(map(float, user_input))
matrix1=user_input[0]-user_input[4]
matrix2=user_input[2]-user_input[4]
matrixy1=user_input[1]-user_input[5]
matrixy2=user_input[3]-user_input[5]
Square=((matrix1*matrixy2)-(matrix2*matrixy1))*0.5

side_a= ((user_input[2]-user_input[0])**2) + ((user_input[3]-user_input[1])**2)
side_b= ((user_input[4]-user_input[2])**2) + ((user_input[5]-user_input[3])**2)
side_c= ((user_input[4]-user_input[0])**2) + ((user_input[5]-user_input[1])**2)

Perimeter=(side_a**0.5)+(side_b**0.5)+(side_c**0.5)

print(abs(round(Perimeter, 5)), abs(Square))
