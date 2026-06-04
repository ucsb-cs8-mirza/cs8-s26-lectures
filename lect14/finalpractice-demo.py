# CS8 — Code Tracing & Recursion — Live Demo
# Run each section to show buggy vs. correct behavior.
# Toggle between buggy_* and fixed_* calls at the bottom of each section.

# =============================================================================
# PART 1 — WARM-UP TRACE
# =============================================================================

def mystery(nums):
    total = 0
    for n in nums:
        total = total + n
    return total

print("=== Warm-up ===")
print(mystery([3, 1, 4]))   # expected: 8


# =============================================================================
# EXAMPLE A — 'or' chaining bug
# Spec: return True if direction is 'north', 'south', 'east', or 'west'
# =============================================================================

def is_valid_direction_A_buggy(direction: str) -> bool:
    if direction == "north" or "south" or "east" or "west":
        return True
    else:
        return False

def is_valid_direction_A_fixed(direction: str) -> bool:
    pass  # YOUR FIX HERE

print("\n=== Example A — 'or' chaining ===")
print("'north' ->", is_valid_direction_A_buggy("north"))   # True  (accidentally correct)
print("'UP'    ->", is_valid_direction_A_buggy("UP"))       # True  (WRONG — should be False)
print("''      ->", is_valid_direction_A_buggy(""))         # True  (WRONG — should be False)

# After fix:
# print("'north' ->", is_valid_direction_A_fixed("north"))
# print("'UP'    ->", is_valid_direction_A_fixed("UP"))
# print("''      ->", is_valid_direction_A_fixed(""))


# =============================================================================
# EXAMPLE B — function name vs. parameter, return "True" vs. return True
# Spec: same as above
# =============================================================================

def is_valid_direction_B_buggy(direction: str) -> bool:
    if is_valid_direction_B_buggy == "north":
        return "True"
    else:
        return "False"

def is_valid_direction_B_fixed(direction: str) -> bool:
    pass  # YOUR FIX HERE

print("\n=== Example B — function name vs. parameter, string vs. bool ===")
result = is_valid_direction_B_buggy("north")
print("'north' ->", result)                  # "False" (string) — condition never True
print("type   ->", type(result))             # <class 'str'>
print("== False ->", result == False)        # False  (string "False" != bool False)
print("if result: ->", bool(result))         # True!  (non-empty string is truthy)

# After fix:
# result = is_valid_direction_B_fixed("north")
# print("'north' ->", result)
# print("type   ->", type(result))
# print("== False ->", result == False)


# =============================================================================
# EXAMPLE C — return inside the loop (early exit)
# Spec: return "Mostly warm" if more than half the temps are >= 70, else "Mostly cool"
# =============================================================================

def is_warm(temp):
    return temp >= 70

def week_summary_C_buggy(temps: list) -> str:
    count = 0
    for temp in temps:
        if is_warm(temp):
            count += 1
        if count > len(temps) / 2:
            return "Mostly warm"
        if count <= len(temps) / 2:
            return "Mostly cool"

def week_summary_C_fixed(temps: list) -> str:
    pass  # YOUR FIX HERE

print("\n=== Example C — return inside the loop ===")
temps = [80, 60, 75, 65, 90]   # 3 warm out of 5 → should be "Mostly warm"
print("temps:", temps)
print("buggy  ->", week_summary_C_buggy(temps))   # "Mostly cool" (wrong — only saw first temp)

# After fix:
# print("fixed  ->", week_summary_C_fixed(temps))


# =============================================================================
# EXAMPLE D — += 0 instead of = 1, and return inside the loop
# Spec: return a dict mapping each word to how many times it appears
# =============================================================================

def word_count_D_buggy(sentence: str) -> dict:
    counts = {}
    for word in sentence.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] += 0   # bug 1: KeyError — key doesn't exist yet
        return counts           # bug 2: returns after first word only

def word_count_D_fixed(sentence: str) -> dict:
    counts = {}
    for word in sentence.split():
        pass  # YOUR FIX HERE
    return counts

print("\n=== Example D — += 0 and return inside loop ===")
try:
    print("buggy ->", word_count_D_buggy("cat dog cat"))
except KeyError as e:
    print("buggy -> KeyError:", e)

# After fix:
# print("fixed ->", word_count_D_fixed("cat dog cat"))   # {'cat': 2, 'dog': 1}
# print("fixed ->", word_count_D_fixed("the the the"))   # {'the': 3}


# =============================================================================
# EXAMPLE E — shadowing the helper function name
# Spec: given a dict of {name: score}, return {'high': count, 'low': count}
#       where 'high' means score >= 70
# =============================================================================

def get_category(score: int) -> str:
    if score >= 70:
        return "high"
    return "low"

def count_by_category_E_buggy(scores: dict) -> dict:
    get_category = {}                    # shadows the helper function above!
    for score in scores.values():
        category = get_category(score)   # now calling a dict, not a function → TypeError
        get_category[category] += 1
    return get_category

def count_by_category_E_fixed(scores: dict) -> dict:
    pass  # YOUR FIX HERE

print("\n=== Example E — shadowing function name ===")
scores = {"Alice": 85, "Bob": 55, "Carol": 92, "Dan": 60}
try:
    print("buggy ->", count_by_category_E_buggy(scores))
except TypeError as e:
    print("buggy -> TypeError:", e)

# After fix:
# print("fixed ->", count_by_category_E_fixed(scores))   # {'high': 2, 'low': 2}


# =============================================================================
# EXAMPLE F — function not called, wrong method on dict
# Spec: passes_threshold(value, threshold) returns True if value >= threshold.
#       filter_dict(d, threshold) returns a new dict with only entries whose
#       value passes the threshold, calling passes_threshold inside the loop.
# =============================================================================

def passes_threshold(value: int, threshold: int) -> bool:
    if value >= threshold:
        return True
    else:
        return False

def filter_dict_F_buggy(d: dict, threshold: int) -> dict:
    if passes_threshold is True:         # function object is never True — condition never fires
        return d.append[passes_threshold]  # append doesn't exist on dicts; never reached anyway

def filter_dict_F_fixed(d: dict, threshold: int) -> dict:
    pass  # YOUR FIX HERE

print("\n=== Example F — function not called, wrong dict method ===")
d = {"Alice": 88, "Bob": 45, "Carol": 72, "Dan": 50}
print("buggy ->", filter_dict_F_buggy(d, 70))   # None — condition never True

# After fix:
# print("fixed ->", filter_dict_F_fixed(d, 70))   # {'Alice': 88, 'Carol': 72}
# print("fixed ->", filter_dict_F_fixed(d, 90))   # {}


# =============================================================================
# PART 3 — LOOPS VS. RECURSION
# =============================================================================

def is_passing(score):
    return score >= 60

# --- count_passing: loop version ---
def count_passing_loop(scores: list) -> int:
    count = 0
    for score in scores:
        if is_passing(score):
            count += 1
    return count

# --- count_passing: recursive version ---
def count_passing_rec(scores: list) -> int:
    if scores == []:
        return 0
    first = scores[0]
    rest  = scores[1:]
    if is_passing(first):
        return 1 + count_passing_rec(rest)
    else:
        return 0 + count_passing_rec(rest)

print("\n=== count_passing: loop vs. recursion ===")
test = [45, 80, 72, 55, 90]
print("loop ->", count_passing_loop(test))   # 3
print("rec  ->", count_passing_rec(test))    # 3
print("[]   ->", count_passing_rec([]))      # 0


# =============================================================================
# PRACTICE PROBLEMS — fill these in
# =============================================================================

# --- Problem 1: sum_list ---

def sum_list_loop(nums: list) -> int:
    pass  # YOUR CODE HERE

def sum_list_rec(nums: list) -> int:
    pass  # YOUR CODE HERE

print("\n=== Problem 1: sum_list ===")
# print("loop ->", sum_list_loop([1, 2, 3, 4]))   # 10
# print("rec  ->", sum_list_rec([1, 2, 3, 4]))    # 10
# print("rec  ->", sum_list_rec([]))              # 0


# --- Problem 2: count_above ---

def count_above_loop(nums: list, cutoff: int) -> int:
    pass  # YOUR CODE HERE

def count_above_rec(nums: list, cutoff: int) -> int:
    pass  # YOUR CODE HERE

print("\n=== Problem 2: count_above ===")
# print("loop ->", count_above_loop([10, 3, 8, 15], 7))   # 3
# print("rec  ->", count_above_rec([10, 3, 8, 15], 7))    # 3
# print("rec  ->", count_above_rec([1, 2], 5))            # 0


# --- Problem 3 (challenge): keys_with_value ---

def keys_with_value_loop(d: dict, target) -> list:
    pass  # YOUR CODE HERE

def keys_with_value_rec(items: list, target) -> list:
    # hint: call with list(d.items()) as the first argument
    pass  # YOUR CODE HERE

print("\n=== Problem 3: keys_with_value ===")
# d = {"a": 1, "b": 2, "c": 1}
# print("loop ->", keys_with_value_loop(d, 1))             # ['a', 'c']
# print("rec  ->", keys_with_value_rec(list(d.items()), 1)) # ['a', 'c']
# print("rec  ->", keys_with_value_rec([], 1))             # []
