ten_thing = "Apple Orange Crows Telephone Light Sugar"

print("Wait there are not 10 thing in that list. Let's fix that.")

stuff = ten_thing.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "corn",
               "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()#出栈
    print("Adding: ",next_one)
    stuff.append(next_one)#追加
    print(f"There are {len(stuff)} items nows.")

print("There we go: ",stuff)

print("Let's do some things with stuff.")

print(stuff[1])#打印第一个
print(stuff[-1]) #whoa! fancy  打印 最后一个
print(stuff.pop())#出栈
print(' '.join(stuff)) #what? cool
print('#'.join(stuff[3:5])) #super stellar!
