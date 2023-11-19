class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        return f"{self.coordinates}, " \
               f"{self.speed}, " \
               f"{self.brand}, " \
               f"{self.year}, " \
               f"{self.number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        x = self.coordinates[0]
        y = self.coordinates[1]
        if (pos_x <= x <= pos_x + width) and (pos_y <= y <= pos_y + length):
            return True
        return False

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                self.__coordinates = value
                return
        raise Exception("Неверные значения")

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__speed = value
                return
        raise Exception("Неверные значения")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self.__brand = value
            return
        raise Exception("Неверные значения")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if isinstance(value, int):
            if value <= 2023:
                self.__year = value
                return
        raise Exception("Неверные значения")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if isinstance(value, str):
            self.__number = value
            return
        raise Exception("Неверные значения")


class Passenger:
    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__passengers_capacity = value
                return
        raise Exception("Неверные значения")

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__number_of_passengers = value
                return
        raise Exception("Неверные значения")


class Cargo:
    def __init__(self, carrying):
        self.carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__carrying = value
                return
        raise Exception("Неверные значения")


class Plane(Transport):
    def __init__(self, height, *args, **kwargs):
        self.height = height
        Transport.__init__(self, *args, **kwargs)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
                return
        raise Exception("Неверные значения")


class Auto(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Ship(Transport):
    def __init__(self, port, *args, **kwargs):
        self.port = port
        Transport.__init__(self, *args, **kwargs)

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        if isinstance(value, str):
            self.__port = value
            return
        raise Exception("Неверные значения")


class Car(Auto):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, passengers_capacity, number_of_passengers):
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Auto.__init__(self, coordinates, speed, brand, year, number)


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, carrying):
        Auto.__init__(self, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)


class Boat(Ship):
    def __init__(self, coordinates, speed, brand, year, number, port):
        super().__init__(port, coordinates, speed, brand, year, number)


class PassengerShip(Ship, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, port, passengers_capacity, number_of_passengers):
        Ship.__init__(self,port, coordinates, speed, brand, year, number, )
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class CargoShip(Ship, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, port, carrying):
        Ship.__init__(self, port, coordinates, speed, brand, year, number)
        Cargo.__init__(self, carrying)


class MyPlane(Plane, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, height, passengers_capacity, number_of_passengers):
        Plane.__init__(self, height, coordinates, speed, brand, year, number)
        Passenger.__init__(self, passengers_capacity, number_of_passengers)


class SeaPlane(Plane, Ship):
    def __init__(self, height, coordinates, speed, brand, year, number, port):
        Ship.__init__(self, port, coordinates, speed, brand, year, number)
        Plane.__init__(self, height, coordinates, speed, brand, year, number)


