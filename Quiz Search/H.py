def count_checks(scores, target):
    checks = 0
    for i in range(len(scores)):
        checks += 1
        if scores[i] == target:
            return i, checks
    return -1, checks


def same_score_pairs(scores):
    pairs = 0
    checks = 0
    for i in range(len(scores)):
        for j in range(i + 1, len(scores)):
            checks += 1
            if scores[i] == scores[j]:
                pairs += 1
    return pairs, checks


def same_score_pairs_fast(scores):
    seen = {}
    pairs = 0
    for s in scores:
        pairs = pairs + seen.get(s, 0)
        seen[s] = seen.get(s, 0) + 1
    return pairs, len(scores)


class_a = [45, 62, 78, 85, 91, 56, 73, 62]
class_b = class_a + [88, 45, 70, 99, 62, 81, 77, 50]

results = []

for scores in [class_a, class_b]:
    n = len(scores)
    best = count_checks(scores, scores[0])[1]
    missing = count_checks(scores, 100)[1]
    pairs, pair_checks = same_score_pairs(scores)
    fast_pairs, fast_checks = same_score_pairs_fast(scores)

    results.append((missing, pair_checks))

    print(f"{n} students: best search {best} check, missing score {missing} checks")
    print(f"  same-score pairs: {pairs} with {pair_checks} checks (every pair);"
          f" {fast_pairs} with {fast_checks} checks (dictionary)")

print()
print("From 8 to 16 students (x2):")

missing_ratio = results[1][0] / results[0][0]
pairs_ratio = results[1][1] / results[0][1]

print(f"  missing-score search: x {missing_ratio:.1f} -> O(n)")
print(f"  same-score pairs: x {pairs_ratio:.2f} -> O(n^2)")
print("  dictionary version  : n checks -> O(n) time, O(n) extra space (the best way)")