#隐式继承
# class Parent():
#     #def implicit(self):
#         #print("Parent implicit()")
#
# class Child(Parent):
#     #pass
# dad = Parent()
# son = Child()
# dad.implicit()
# son.implicit()
#
#显示覆盖
# class Parent():
#
#     def override(self):
#         print("Parent override()")
#
# class Child(Parent):
#
#     def override(self):
#         print("Child override()")
#
# dad = Parent()
# son = Child()
#
# dad.override()
# son.override()


# class Parent():
#     def altered(self):
#         print("Parent altered()")
#
# class Child(Parent):
#
#     def altered(self):
#         print("Child, before Parent altered()")
#         super(Child,self).altered()
#         print("Child, after Parent altered()")
#
# dad = Parent()
# son = Child()
#
# dad.altered()
# son.altered()

# class Parent():
#     def override(self):
#         print("Parent override()")
#
#     def implicit(self):
#         print("Parent implicit()")
#
#     def altered(self):
#         print("Parent altered")
#
# class Child(Parent):
#
#     def override(self):
#         print("Child override()")
#     def altered(self):
#          print("Child, before Parent altered()")
#          super(Child,self).altered()
#          print("Child, after Parent altered()")
#
# dad = Parent()
# son = Child()
#
# dad.implicit()
# son.implicit()
#
# dad.override()
# son.override()
#
# dad.altered()
# son.altered()

class Other():
    def override(self):
        print("other override()")

    def implicit(self):
        print("other implicit()")

    def altered(self):
        print("other altered()")

class Child():
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("Child override()")

    def altered(self):
        print("Child before other altered()")
        self.other.altered()
        print("Child after other altered")

son = Child()

son.implicit()
son.override()
son.altered()
