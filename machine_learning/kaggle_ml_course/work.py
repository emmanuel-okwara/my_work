
def func(number):
    num ={0:'###\n# #\n# #\n# #\n###', 1:'#\n#\n#\n#\n#',2:'###\n  #\n###\n#\n###',3:'###\n  #\n###\n  #\n###',4:'# #\n# #\n###\n  #\n  #',5:'###\n#\n###\n  #\n###',6:'###\n#\n###\n# #\n###',7:'###\n  #\n  #\n  #\n  #',8:'###\# #\n###\n# #\n###',9:'###\n# #\n###\n  #\n###'}
    l = []
    sting_number = str(number)
    
    
    for i in sting_number:
        print(num[int(i)]+'\n\n\n123
              ',end='')  
    
    
            
        
print(func(int(input('Enter any number to print:    '))))

