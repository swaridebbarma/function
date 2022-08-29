

def check_speed(speed):
    if speed <= 70:
        return 'Ok'
    elif speed >= 70:
        points = (speed - 70) // 2
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'
check_speed(80)



list=["abc","xyz","aba","1221"]
def fun(list):
    i=0
    c=0
    while i< len(list):
        if list[i]>1:
           list[0]==list[-1]
        c+=1
    print(c)
fun(list)


 
def match_words(wd):  
    c = 0    
    for w in wd:  
        if len(w) > 1 and w[0] == w[-1]:  
           c += 1  
        return c        
print(match_words(["abc","xyz","aba","1221"]))
     
