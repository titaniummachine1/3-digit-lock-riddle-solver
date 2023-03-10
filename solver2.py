def matches_in_place(a, b):
    return sum([1 for i in range(len(a)) if a[i] == b[i]])

def num_digits_right(a, b):
    return len(set(a) & set(b))

def rule1(guess):
    return matches_in_place(guess, [6,8,2]) == 1 and num_digits_right(guess, [6,8,2]) == 1

def rule2(guess):
    return matches_in_place(guess, [6,1,4]) == 0 and num_digits_right(guess, [6,1,4]) == 1

def rule3(guess):
    return matches_in_place(guess, [2,0,6]) == 0 and num_digits_right(guess, [2,0,6]) == 2

def rule4(guess):
    return num_digits_right(guess, [7,3,8]) == 0

def rule5(guess):
    return matches_in_place(guess, [3,8,0]) == 0 and num_digits_right(guess, [3,8,0]) == 1

def is_valid(guess):
    return rule1(guess) and rule2(guess) and rule3(guess) and rule4(guess) and rule5(guess)

def get_combinations():
    combos = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                combos.append([i,j,k])
    return combos

combinations = get_combinations()
valid_guesses = [combo for combo in combinations if is_valid(combo)]

with open("solution.txt", "w") as f:
    for valid in valid_guesses:
        f.write("%d %d %d\n" % tuple(valid))
