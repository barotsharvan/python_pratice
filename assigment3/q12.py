# Sets
# Q12

visitors = set()

n = int(input("Enter the number of visitors: "))

for _ in range(n):
    name = input("Enter visitor name: ")
    visitors.add(name)

# Display visitor names
print("\nUnique Visitors:")
for visitor in visitors:
    print(visitor)
