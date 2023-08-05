
def triangle_area(base:float,high:float):
  area = 0.5*base*high
  check_area(area)

def circle_area( radus:float):
   area = 3.14*radus*radus
   check_area(area)

def rectangle_area(length:float , high:float):
    area=length*high
    check_area(area)


def check_area(area):
    if area>=10 :
        print("area is bigger than 10")
    elif area <10 and area >0  :
            print("area less than 10")
    else :
         print("invalid area")


rectangle_area(10,5)
circle_area(5)
triangle_area(1,5)
