#print("How old are you?", end=' ')
#age = input()
#print("How tall are you?", end=' ')
#height = input()
#print("How much do you weigh?", end=' ')
#print("How much do you weigh?", end=' ' 没有括号
#weight = input()

#print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#print(f"So, you're {age} old, {height} tall and {weight} heavy.")height没有定义
#from sys import argv
#script, filename = argv#没有导包

#txt = open(filename)
#txt = open(filenme)变量名错误

#print("Here's your file {filename}:")
#print(txt.read())
#print(tx.read())tx没有定义

#print("Type the filename again:")
#file_again = input("> ")

#txt_again = open(file_again)

#print(txt_again.read())
#print(txt_again_read())没有这个函数


#print("Let's practice everything.")
#print('Let's practice everything.')单引号里面还有单引号
#print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
#print('You\'d need to know \'bout escapes
      #with \\ that do \n newlines and \t tabs.')with是关键字 不能分割

#poem = """
#\tThe lovely world
#with logic so firmly planted
#cannot discern \n the needs of love
#nor comprehend passion from intuition
#and requires an explanation
#\n\t\twhere there is none.
#"""

#print("--------------")
#print("--------------)没有后引号
#print(poem)
#print("--------------")
#print(--------------")没有前引号


#five = 10 - 2 + 3 - 6
#print(f"This should be five: {five}")

#def secret_formula(started):
    #jars = jelly_beans / 1000
    #crates = jars / 100
    #return jelly_beans, jars, crates


#start_point = 10000
#beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
#print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
#print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

#start_point = start_point / 10

#print("We can also do that this way:")
#formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
#print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
cates = 30
dogs = 15


if people < cates:
    print ("Too many cats! The world is doomed!")

if people > cates:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
