def line(line):
    if line == []:
        print("The line is currently empty.")
    else:
        line_items = []
        i = 1
        for name in line:
            line_items.append(f'{str(i)}. {name}')
            i += 1
        print("The line is currently: " + " ".join(line_items))

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if katz_deli:
        print(f'Currently serving {katz_deli.pop(0)}.')
    else:
        print("There is nobody waiting to be served!")