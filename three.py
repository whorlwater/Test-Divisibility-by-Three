three = 0

x = 1

three_list = [3,6,9]

def checkSumDigits(x):
    x = str(x)
    while len(x) >= 2:
        list_x = list(x)
        list_x = [int(each) for each in list_x]
        x = sum(list_x)
        x = str(x)
    x = int(x)
    return x

while three == 0:
    original_x = x
    divide_check = x/3.0
    if divide_check%1 == 0:
        x = checkSumDigits(x)
        if x in three_list:
            print "%s is divisible by three." % (original_x)  
            x = original_x + 1            
        else:
            three = original_x
            print "%s is divisible by three, but its digits' sum is not divisible by three." % (original_x)
    else:
        x = checkSumDigits(x)
        if x in three_list:
            three = original_x
            print "%s is not divisible by three, but its digits' sum is divisible by three." % (original_x)           
        else:
            print "%s is not divisible by three." % (original_x)  
            x = original_x + 1
