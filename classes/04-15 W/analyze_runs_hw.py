# analyze_runs homework
# STI analysis before coding

# State:
#   - current_run: list of values in the run we're currently building
#   - direction: which way the current run is going ("inc", "dec", or None)
#   - longest_inc / longest_dec: best run lengths found so far
#   - best_inc_values / best_dec_values: the actual values of those best runs
#   - count_inc / count_dec: how many complete runs of each type we've seen
#
# Transitions:
#   - if next number > previous: we're increasing
#       - if we were already increasing, extend the run
#       - if we were decreasing or flat, finalize the old run and start fresh
#   - if next number < previous: we're decreasing (same logic, opposite direction)
#   - if next number == previous: the run breaks, finalize whatever we had
#
# Invariants:
#   1. current_run always has at least 1 element once we start scanning
#   2. longest_inc and longest_dec never decrease as we go through the list
#   3. count_inc and count_dec only go up when a run actually ends (not while we're still in it)
#   4. len(best_inc_values) == longest_inc and len(best_dec_values) == longest_dec at all times


def analyze_runs(nums):
    if len(nums) < 2:
        return {
            "longest_increasing_run": 0,
            "longest_decreasing_run": 0,
            "num_increasing_runs": 0,
            "num_decreasing_runs": 0,
            "longest_run_values": []
        }

    # state initialization
    direction = None
    current_run = [nums[0]]

    longest_inc = 0
    longest_dec = 0
    best_inc_values = []
    best_dec_values = []
    count_inc = 0
    count_dec = 0

    i = 1
    while i < len(nums):
        prev = nums[i - 1]
        curr = nums[i]

        if curr > prev:
            # transition: start or continue an increasing run
            if direction == "inc":
                current_run.append(curr)
            else:
                # finalize whatever run we were in
                if direction == "dec":
                    count_dec += 1
                    if len(current_run) > longest_dec:
                        longest_dec = len(current_run)
                        best_dec_values = current_run[:]
                # start new increasing run from previous value
                current_run = [prev, curr]
                direction = "inc"

        elif curr < prev:
            # transition: start or continue a decreasing run
            if direction == "dec":
                current_run.append(curr)
            else:
                if direction == "inc":
                    count_inc += 1
                    if len(current_run) > longest_inc:
                        longest_inc = len(current_run)
                        best_inc_values = current_run[:]
                current_run = [prev, curr]
                direction = "dec"

        else:
            # equal values break any run
            if direction == "inc":
                count_inc += 1
                if len(current_run) > longest_inc:
                    longest_inc = len(current_run)
                    best_inc_values = current_run[:]
            elif direction == "dec":
                count_dec += 1
                if len(current_run) > longest_dec:
                    longest_dec = len(current_run)
                    best_dec_values = current_run[:]

            current_run = [curr]
            direction = None

        i += 1

    # finalize the last run after the loop ends
    if direction == "inc":
        count_inc += 1
        if len(current_run) > longest_inc:
            longest_inc = len(current_run)
            best_inc_values = current_run[:]
    elif direction == "dec":
        count_dec += 1
        if len(current_run) > longest_dec:
            longest_dec = len(current_run)
            best_dec_values = current_run[:]

    # pick whichever is longer for longest_run_values
    if longest_inc >= longest_dec:
        longest_run_values = best_inc_values
    else:
        longest_run_values = best_dec_values

    return {
        "longest_increasing_run": longest_inc,
        "longest_decreasing_run": longest_dec,
        "num_increasing_runs": count_inc,
        "num_decreasing_runs": count_dec,
        "longest_run_values": longest_run_values
    }


# test cases from the assignment
print(analyze_runs([3, 5, 7, 2, 1, 4]))
print(analyze_runs([1, 2, 3, 4]))
print(analyze_runs([5, 4, 3, 2]))
print(analyze_runs([1, 1, 1]))
print(analyze_runs([4]))
print(analyze_runs([2, 5, 5, 4, 3, 6]))
