def second_largest(numbers):
    unique=list(set(numbers))
    unique.sort()
    if len(unique)<2:
        return"Second largest not availabel"
    return unique[-2]
numbers=[10,25,40,15,30]
print("Second Largest:",second_largest(numbers))