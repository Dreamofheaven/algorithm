import re

while True:
    password = input()

    if password == 'end':
        break

    con1 = re.findall(r"a|e|i|o|u", password)
    con2 = re.findall(r"([a|e|i|o|u]{3})|([^a|e|i|o|u]{3})", password)
    con3 = re.findall(r"([a-df-np-z])\1", password)

    if len(con1) != 0 and len(con2) == 0 and len(con3) == 0:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
