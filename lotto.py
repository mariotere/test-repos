#lotto 7 out of 49
import random
numbers = []
b = 0
for number in range (1,50):
    numbers.append(number)
random.shuffle(numbers)#random mix

index_random = []
while b < 7:# in a loop while 7 index draws from a set of numbers from 1 to 49
    los_index = random.randint(1,49)
    if los_index in index_random:
        continue
    index_random.append(los_index)
    #print(b, los_index)
    b+=1
#print(losowe)
seven_random_numbers = []
for i in index_random:
    seven_random_numbers.append(numbers[i-1])
seven_random_numbers.sort()
print(f"The following 7 numbers were drawn out of 49 {seven_random_numbers}")
    
#print(numbers)
