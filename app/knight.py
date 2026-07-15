from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: dict,
                 weapon: dict,
                 potion: dict,
                 protection: int
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    @classmethod
    def create_knight(cls, knightsData: dict) -> Knight:
        return Knight(
            name=knightsData["name"],
            power=knightsData["power"],
            hp=knightsData["hp"],
            armour=knightsData["armour"],
            weapon=knightsData["weapon"],
            potion=knightsData["potion"],
            protection=0
        )

    def apply_knight_stats(self: Knight) -> None:
        # apply armour
        for a in self.armour:
            self.protection += a["protection"]

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def fight(self, opponent: Knight) -> None:
        opponent_damage = max(0, opponent.power - self.protection)
        self.hp -= opponent_damage

        self_damage = max(0, self.power - opponent.protection)
        opponent.hp -= self_damage

        # check if someone fell in battle
        self.hp = max(0, self.hp)
        opponent.hp = max(0, opponent.hp)
