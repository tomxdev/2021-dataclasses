from dataclasses import dataclass, field


@dataclass(order=True, frozen=False)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)

    def __str__(self):
        return f'{self.name} {self.job} ({self.age})'


def main():
    person1 = Person("Tom", "Neves", 35, 99)
    person2 = Person("Mariano", "John", 30)
    person3 = Person("Mariano", "John", 30)

    print(person1)
    print(id(person2))
    print(id(person3))
    print(person3 == person2)
    print(person1 > person2)


if __name__ == '__main__':
    main()
