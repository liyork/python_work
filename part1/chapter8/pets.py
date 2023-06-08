def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


def describe_pet_with_default(pet_name, animal_type='dog'):  # 默认值，先列出没有默认值的形参，再列出有默认值的实参
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")


if __name__ == '__main__':
    describe_pet("hamster", 'harry')
    describe_pet("dog", 'willie')  # 位置实参
    describe_pet(animal_type='hamster', pet_name='harry')  # 关键字实参
    describe_pet_with_default('aaa')
