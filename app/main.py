class Animal:
    alive = []

    def __init__(
        self, name: str, health: str = 100, hidden: bool = False
    ) -> None:
        self.hidden = hidden
        self.health = health
        self.name = name
        self.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: "
            f"{self.health}, Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and animal.hidden is False:
            animal.health -= 50
        if animal.health <= 0:
            Animal.alive.remove(animal)
