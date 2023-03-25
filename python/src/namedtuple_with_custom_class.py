import collections


class Stats:
    def __init__(self) -> None:
        self.men: int = 0
        self.women: int = 0

    def __repr__(self) -> str:
        return f"men: {self.men}, women: {self.women}"


stats: dict = collections.defaultdict(lambda: Stats())

print("Accessing an object first time:")
print(f"{stats['Russia']}\n")

print("Add count of men in Russia:")
stats["Russia"].men = 100
print(f"{stats['Russia']}\n")

print("Add count of women in England:")
stats["England"].women = 100
print(f"{stats['England']}\n")

print("Whole dict:")
for key, value in stats.items():
    print(f"{key}: {value}")
