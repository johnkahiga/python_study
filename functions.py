def hello(name):
    print(f'Hello {name}')

hello('Alex')
def triangle_area(base,height):
    t_area=0.5*base*height
    print(t_area)

triangle_area(10,20)

def area_circle(radius):
    tt=3.164
    area=radius*tt
    print(area)

area_circle(123)

def area_rectangle(length,width):
    area=length*width
    print(area)

area_rectangle(56,47)
area_rectangle(45,123)

def largest_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        large=num1
    elif num2>num3 and num2>num3:
        large=num2
    else:
        large=num3
    return large



2,4,7,10,12 use functions