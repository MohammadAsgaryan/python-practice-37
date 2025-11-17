import random

class Human:
    def __init__(self, name):
        self.name = name
        
        
class Footballer(Human):
    def __init__(self, name):
        super().__init__(name)
        
        
names = [
    "حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد",
    "مصطفی", "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد",
    "سهیل", "بهروز", "شهروز", "سامان", "محسن"
]

players = [Footballer(name) for name in names]
random.shuffle(players)

team_A = players[:11]
team_B = players[:11]

print("تیم A:")
for p in team_A:
    print(f"{p.name}")

print("\nتیم B:")
for p in team_B:
    print(f"{p.name}")