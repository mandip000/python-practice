numbers = []
for i in range(5):
    numbers.append(int(input("Enter number: ")))

print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Reversed:", numbers[::-1])