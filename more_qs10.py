"""def func():
    list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
    i = 0
    while i < len(list):
        a = len(list[i])
        j = 0
        while j < a:
            print (list[i][j])
            j= j+ 1
        i = i + 1
        print ('-----')
func()"""
    

def check_max_number():
    marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
    i=0
    while i<len(marks):
        j=0
        mx=0
        while j<len(marks[i]):
            if marks[i][j] > mx:
                mx=marks[i][j]
            j+=1
        i+=1
        print(mx)
check_max_number()
#more_qs10