source = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []

""" Basic method
for s in source:
    if s%2==0:
        result.append(s)

print(result)"""

result = [s for s in source if s % 2 == 0]
print(result)

source = [(1, 2, 3, ), (4, 5, 6, ), (7, 8, 9, )]
result = []

""" Basic method
for columns in source:
    for row in columns:
        result.append(row)
"""
result = [row for columns in source for row in columns]
print(result)

source = [30, 15, -5, 7, 15, -9]
result = [s if s > 0 else 0 for s in source]
print(result)
