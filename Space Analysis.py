import random
import time

# ============================================================
# PART 1 — Classify Space Complexity
# ============================================================

def reverse_string(s):
    return s[::-1]

# Space O: O(n)
# Reason: Slicing creates a new string containing all n characters.


def count_letters(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Space O: O(n)
# Reason: It creates a new dictionary and stores character frequency


def matrix_identity(n):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix

# Space O: O(n²)
# Reason: An n × n matrix contains n² elements.


def running_sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

# Space O: O(1)
# Reason: Only a fixed number of variables (total and x) are used
# regardless of input size.


# ============================================================
# PART 2 — Duplicate Email Detection
# ============================================================

NUM_EMAILS = 10_000
random.seed(42)

domains = ["gmail.com", "yahoo.com", "outlook.com", "company.com"]

unique_emails = [
    f"user{i}@{domains[i % len(domains)]}"
    for i in range(8_000)
]

_dupes = random.choices(unique_emails, k=2_000)

all_emails = unique_emails + _dupes
random.shuffle(all_emails)


# ---- Approach 1: Set-based -----------------------------------------------
# Time:  O(n)
# Space: O(n)

def find_duplicates_set(emails):
    """
    Return a set of email addresses that appear more than once.

    Uses O(n) extra space (a 'seen' set + a 'duplicates' set).
    """
    seen = set()
    duplicates = set()

    for email in emails:
        if email in seen:
            duplicates.add(email)
        else:
            seen.add(email)

    return duplicates


# ---- Approach 2: Sort-and-scan -------------------------------------------
# Time:  O(n log n)
# Space: O(1) extra (excluding the sorted copy)

def find_duplicates_sort(emails):
    """
    Return a set of email addresses that appear more than once.

    Uses O(1) extra space beyond the sorted copy.
    """
    sorted_emails = sorted(emails)

    duplicates = set()

    for i in range(1, len(sorted_emails)):
        if sorted_emails[i] == sorted_emails[i - 1]:
            duplicates.add(sorted_emails[i])

    return duplicates


# ============================================================
# RAM Question
# ============================================================

# 4 GB RAM  → I would choose sort-and-scan because it minimizes
#             additional memory usage and scales better when RAM
#             is limited.

# 64 GB RAM → I would choose the set-based approach because it is
#             O(n) time and provides significantly faster lookups
#             while memory is plentiful.


def benchmark(func, data, label):
    start = time.time()
    result = func(data)
    elapsed = (time.time() - start) * 1000
    return result, elapsed


if __name__ == "__main__":
    print("=" * 60)
    print(f"Duplicate Email Detection ({NUM_EMAILS:,} emails)")
    print("=" * 60)

    dupes_set, t_set = benchmark(find_duplicates_set, all_emails, "set")
    dupes_sort, t_sort = benchmark(find_duplicates_sort, all_emails, "sort")

    print(
        f"  Set approach    : {len(dupes_set):>5} duplicates  {t_set:.3f} ms"
    )
    print(
        f"  Sort+scan       : {len(dupes_sort):>5} duplicates  {t_sort:.3f} ms"
    )

    print(f"  Both agree      : {dupes_set == dupes_sort}")