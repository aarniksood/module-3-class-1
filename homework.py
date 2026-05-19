def circumference(P):
    return 2*3.14*P
def area_of_circle(P):
    return 3.14 * P**2.0
print("What you want to find")
print("a. circumference of a circle")
print("b. area of circle")
choice = input("enter your choice")
radius = float(input("enter radius"))
if choice == ('a'):
 print("circumference of circle =", circumference(radius))
elif choice == ('b'):
 print("area of circle =", area_of_circle(radius))