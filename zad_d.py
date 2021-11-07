# for loop
for index, element in enumerate(range(1,11)):
    if not index%2==0:
        print(element)

# list comprehension
[print(element) for index, element in enumerate(range(1,11)) if not index%2==0]