n = int(input())
person = {}

for i in range(n):
    name, status = map(str, input().split())
    person[name] = status
sorted_person = dict(sorted(person.items(), reverse=True))

for key in sorted_person:
    if sorted_person[key] == 'enter':
        print(key)
        