# from car import Car  # 导入模块car的Car类，若是多个则用逗号分割
from car import Car as Cr  # 用别名


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 133

        print(f"this car can go about {range} miles on a full charge")


# 创建子类时，父类必须包含在当前文件中，且位于子类前面
class ElectricCar(Cr):  # 继承
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # 属性是对象的实例

    def get_descriptive_name(self):  # 重写父类方法
        long_name = f"electricCar--{self.year} {self.make} {self.model}"
        return long_name.title()


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()
