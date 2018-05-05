info = {
    'name': 'Kara', 
    'age': 22, 
    'hobbies': ['Netflix', 'Chill', 'Sleep'], 
    'wakeup': {'Mon': 6, 'Tues': 7, 'Wed': 8}
    }

print(info['name'])
print(len(info['hobbies']))
print(info['wakeup']['Tues'])

for hobby in info['hobbies']:
    print(hobby)

for time in info["wakeup"].values():
    print(time)

