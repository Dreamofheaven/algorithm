# 나머지

mod_stack = set()

for _ in range(10):
    n = int(input())
    mod_stack.add(n % 42)

print(len(mod_stack)) 