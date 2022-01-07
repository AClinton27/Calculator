print('This is a simple calculator')
print('***'*20)
print('Mode')
print("To Add, select 1")
print("To Subtract, select 2")
print("To Multiply select 3")
print("To Divide, select 4")
print("To Get mean, select 5")
print("To solve a simultaneous equation, select 6")
print("To solve a quadratic equation, select 7")

print('***'*20)
def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for i in myList:
        result = result * i
    return result

mode = int(input('Enter mode: '))
if mode ==1:
    x = int(input('how many numbers do you want to add: '))
    y= []
    while x > len(y):
        a = int(input('enter number: '))
        y.append(a)
        print(y)
    print('answer =', sum(y))

elif mode ==2:
    z = int(input('how many numbers do you want to subtract: '))
    b = []
    while z > len(b):
        p = int(input('enter number: '))
        b.append(p)
        print(b)
        print(str(b[0]), '-', str(b[1:]))
    print('answer =', b[0]- sum(b[1:]))

elif mode ==3:
    m = int(input('how many numbers do you want to multiply: '))
    n= []
    while m > len(n):
        u = int(input('enter number: '))
        n.append(u)
        print(n)
    print('answer =', multiplyList(n))

elif mode==4:
    num= int(input('enter numerator: '))
    denominator = int(input('enter numerator: '))
    quotient = num/denominator
    print(str(num),'/', str(denominator),'=', quotient)

elif mode ==5:
    d = int(input('how many numbers do you want to get the mean for: '))
    e= []
    while d > len(e):
        digits = int(input('enter number: '))
        e.append(digits)
        print(e)
    print('The mean of', e, '=', sum(e)/len(e))

elif mode ==6:
    x1 = int(input('enter coefficient of x in equation 1: '))
    y1 = int(input('enter coefficient of y in equation 1: '))
    c1 = int(input('enter result in equation 1: '))
    x2 = int(input('enter coefficient of x in equation 2: '))
    y2 = int(input('enter coefficient of y in equation 2: '))
    c2 = int(input('enter result in equation 2: '))

    determinant = (x1*y2) - (y1*x2)
    det_x = (c1*y2) - (y1*c2)
    det_y = (x1*c2) - (c1*x2)
    X = det_x/determinant
    Y= det_y/determinant
    print ('The solution to the simultaneous equation is', X, 'and', Y)

elif mode ==7:
    a_ = int(input('enter a: '))
    b_ = int(input('enter b: '))
    c_ = int(input('enter c: '))
    discriminant = ((b_**2) - (4*a_*c_))**0.5
    ansx1 = (-1*b_ + discriminant)/(2*a_)
    ansx2 = (-1*b_ - discriminant) / (2*a_)
    print('The solution to the quadratic equation is',  ansx1, 'and',ansx2 )

else:
    print('Invalid selection')

