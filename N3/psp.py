x = input("Введите скобки:\n")

open_count = 0
remove_count = 0

for bracket in x:
    if bracket == '(':
        open_count += 1
    elif bracket == ')':
        if open_count > 0:
            open_count -= 1
        else:
            remove_count += 1

remove_count += open_count

print("Число скобок без пары:", remove_count)