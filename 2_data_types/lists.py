data_types = ["String", 100, 99.99, True, False]

for data in data_types:
    print(f"{type(data)}: {data}")

print()

months = ["January", "February", "March"]
print(months[0])
print(months[1])

print()

months.append("April")
for month in months:
    print(month)

print()

# error: IndexError
# print(months[4])

months.remove("April")
for month in months:
    print(month)