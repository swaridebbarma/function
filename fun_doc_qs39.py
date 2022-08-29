#doc.q39
maxi=[4,6,2000,1,9,63,-134,566]
mini=[-52, 56, 30,-120, 29, -54, 0, -110]
def check(maxi,mini):
    i=0
    max=0
    min=0
    while i<len(maxi):
        if (maxi[i])>max:
            max=maxi[i]
        elif mini[i]<min:
             min=mini[i]
        i+=1
    print(max)
    print(min)
check(maxi,mini)
    
# maxi=[5]
# mini=[42, 54, 65, 87, 0]
# check([4,6,2,1,9,63,-134,566])
# check([-52, 56, 30, 29, -54, 0, -110])
