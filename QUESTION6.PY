def function():
    if speed < 70:
        print("ok")
    elif speed > 70 and speed < 90:
        print("point:2")
    else:
        print("License suspended")
speed=int(input("enter no"))
function()