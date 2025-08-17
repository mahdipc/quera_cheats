k = int(input().strip())

wall = "########"
hall = "......."
full_bottom = "#" * 23

lines = []


def slot_label(idx):
    return f"ghorfe{idx}"


idx = 1
for _ in range(4):
    lines.append(f"{wall}{hall}{wall}")
    left = slot_label(idx) if idx <= k else hall
    right = slot_label(idx + 1) if idx + 1 <= k else hall
    lines.append(f"#{left}{hall}{right}#")
    idx += 2

lines.append(full_bottom)

print("\n".join(lines))
