import builtins

builtins.print()

ranking = {
    'A': 100,
    'B': 60,
    'C': 75,
}

#ranking.get('A')

print(sorted(ranking, key=ranking.get, reverse=True))

