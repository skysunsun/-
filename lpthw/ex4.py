cars=100#车辆数
space_in_a_car=4.0#停车位上的车辆数
drivers=30#司机数量
passengers=90#乘客数量
car_not_driven=cars-drivers#没被开得车数量
car_driven=drivers#被开车的数量
carpool_capacity=car_driven*space_in_a_car#停车场容量
average_passengers_per_car=passengers/car_driven#每辆车的平均乘客人数


print("there are",cars,"cars avaible.")#打印可以开的车
print("there are only", drivers,"drivers available.")#打印司机数量
print("there will be", car_not_driven,"empty cars today.")#打印没人开的车数量
print("we can transport", carpool_capacity,"people today.")#打印可以运输的人数量
print("we have", passengers,"to carpool today.")#打印停车场的人数
print("we need to put about", average_passengers_per_car,"in each car.")#打印每辆车的人数
