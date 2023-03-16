import random

team_a = [round(random.uniform(5, 10), 2) for a in range(20)]
team_b = [round(random.uniform(5, 10), 2) for b in range(20)]
team_win = [(team_a[i] if team_a[i] > team_b[i] else team_b[i]) for i in range(20)]

print(f'Первая команда: {team_a}'
      f'\nВторая команда: {team_b}'
      f'\nПобедители тура: {team_win}')