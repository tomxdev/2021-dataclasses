class Person:
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age


def main():
    person1 = Person("Tom", "Neves", 23)
    person2 = Person("Mariano", "John", 18)
    person3 = Person("Mariano", "John", 18)

    print(id(person2))
    print(id(person3))
    print(person1)
    print(person3 == person2)


if __name__ == '__main__':
    main()