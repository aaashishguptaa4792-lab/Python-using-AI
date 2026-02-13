test_cases= [
    (15,12),
    (12,2),
    (10,11),
    (20,6),
    (4,4),
]

print(f"{'Pair':<10} |{'Condition Met'}")
print("-" * 30)

for v1, v2 in test_cases:
    is_met=(v1 > 10 and v2 > 10)and (v1 > 5 or v2 > 5)
  
    result = "Yes" if is_met else "No"
    print(f"{v1},{v2}):<10 | {result}")
