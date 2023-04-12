class Panda:
    def __int__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self) -> int:
        return self.__age

    def set_name(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __str__(self):
        return f"Name {self.__name} '\n' Age: {self.__age}"





