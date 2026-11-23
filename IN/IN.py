def find_seat(seats, target):
    low, high, checks = 0, len(seats) - 1, 0
    while low <= high:
        mid = (low + high) // 2
        checks += 1

        if seats[mid] == target:
            return mid, checks
        elif seats[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, checks

def find_seat_recursive(seats, target, low, high, depth):
    if low > high:
        return -1, depth
    mid = (low + high) // 2
    if seats[mid] == target:
        return mid, depth
    elif seats[mid] < target:
        return find_seat_recursive(seats, target, mid + 1, high, depth + 1)
    else:
        return find_seat_recursive(seats, target, low, mid - 1, depth + 1)

seats = [101, 104, 108, 112, 115, 120, 125, 130, 135, 140, 145, 150]

print("🚆 Free seats:", seats)

for target in [130, 101, 150, 133]:
    index, checks = find_seat(seats, target)
    rindex, depth = find_seat_recursive(seats, target, 0, len(seats) - 1, 1)

    if index == -1:
        print("❌ Seat", target, ": not free   🔄 loop checks =", checks, "  🌳 recursion depth =", depth)
    else:
        print("✅ Seat", target, ": index", index, "  🔄 loop checks =", checks, "  🌳 recursion depth =", depth)
        
print("📊 Same answers with", len(seats), "seats.")
print("🔄 Loop: O(log n) time, O(1) extra space.")
print("🌳 Recursion: O(log n) time, O(log n) extra space.")
print("🚉 Empty coach:", find_seat([], 120), find_seat_recursive([], 120, 0, -1, 1))