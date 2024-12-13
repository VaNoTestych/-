from task_1 import Car, SocialMedia, Tree

if __name__ == "__main__":
    car = Car(120, "Opel")
    facebook = SocialMedia("Facebook", 200000)
    oak = Tree("Oak", 6.0, 58)

    try:
        car.accelerate(5.5)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        facebook.add_users(5.5)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        oak.grow(9.7)
    except TypeError:
        print('Ошибка: неправильные данные')
