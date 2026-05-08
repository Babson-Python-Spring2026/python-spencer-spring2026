# plus_minus.py — Plus/Minus Target Sum
# given a list of numbers and a target, assign + or - to each number
# to make the expression equal the target

# state: the current sign combination being tested (list of 0s and 1s)
# transition: move to next combination by incrementing a counter
# invariant: every number used exactly once per combination,
#            all 2**n combos checked before reporting no solution


def get_numbers():
    # read list of numbers from user, split by spaces, convert to ints
    raw = input("Enter numbers: ")
    parts = raw.split()
    numbers = []
    for p in parts:
        numbers.append(int(p))
    return numbers


def get_target():
    # read target sum from user
    return int(input("Enter target: "))


def generate_signs(combo_number, n):
    # convert an integer (0 to 2**n - 1) into a list of 0s and 1s
    # each position maps to + (1) or - (0)
    # uses modulus to extract each bit — val % 2 always gives 0 or 1
    # then floor division shifts to the next bit
    signs = []
    val = combo_number
    for j in range(n):
        signs.append(val % 2)
        val = val // 2
    return signs


def compute_sum(numbers, signs):
    # apply the sign combination to the numbers and compute total
    # 1 means add, 0 means subtract
    total = 0
    for j in range(len(numbers)):
        if signs[j] == 1:
            total = total + numbers[j]
        else:
            total = total - numbers[j]
    return total


def build_expression(numbers, signs, target):
    # build a readable expression string like "-1 + 2 + 3 = 4"
    expression = ""
    for j in range(len(numbers)):
        if j == 0:
            # first number — no leading space, just sign
            if signs[j] == 1:
                expression = str(numbers[j])
            else:
                expression = "-" + str(numbers[j])
        else:
            # remaining numbers — add operator with spaces
            if signs[j] == 1:
                expression = expression + " + " + str(numbers[j])
            else:
                expression = expression + " - " + str(numbers[j])
    expression = expression + " = " + str(target)
    return expression


def find_solution(numbers, target):
    # explore the full state space: 2**n possible sign assignments
    # state space is all binary strings of length n
    # each integer from 0 to 2**n - 1 represents one combination
    n = len(numbers)
    total_combos = 2 ** n

    # transition: try each combination in order
    for i in range(total_combos):
        signs = generate_signs(i, n)
        total = compute_sum(numbers, signs)

        # check if this combination hits the target
        if total == target:
            return signs

    # invariant: we checked every combination — no solution exists
    return None


def main():
    numbers = get_numbers()
    target = get_target()

    # search the state space for a valid sign assignment
    signs = find_solution(numbers, target)

    if signs is not None:
        expression = build_expression(numbers, signs, target)
        print(expression)
    else:
        print("No solution possible")


main()
