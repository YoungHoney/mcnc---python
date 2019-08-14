def average(*args):
    result = 0
    for i in args:
        result+=i
    return result/len(args)

print(average(2,3))
        
    
