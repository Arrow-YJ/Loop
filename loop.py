#1While loop
#Continue Loop
for int in "123456":
    if int == "4":
        continue
    print(int)

print("END")






#break Loop
for int in "123456":
    if int == "4":
        break
    print(int)

print("END")






#2For loop STAR Triangle

n =int(input("Enter numbers = \n"))
def triangle(n):

    k = n - 1

    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")

        k = k - 1

        for j in range(0, i + 1):

            print("* ", end="")
        print("\r")

triangle(n)
print("END")










