with open("hello.txt",'w+') as file:
    file.write("Hello, World!")

num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))