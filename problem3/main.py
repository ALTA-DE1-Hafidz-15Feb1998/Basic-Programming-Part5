def join_array_remove_duplicate(arrayA, arrayB):
    # your code here
    # Create a set to store unique elements
    unique_elements = set()
    # Add elements from arrayA to the set and result list
    result = []
    for item in arrayA:
        if item not in unique_elements:
            unique_elements.add(item)
            result.append(item)
    # Add elements from arrayB to the set and result list
    for item in arrayB:
        if item not in unique_elements:
            unique_elements.add(item)
            result.append(item)

    return result

if __name__ == '__main__':
    # Test cases
    print(join_array_remove_duplicate(["apel", "anggur"], ["lemon", "leci", "nanas"]))
    # ["apel", "anggur", "lemon", "leci", "nanas"]

    print(join_array_remove_duplicate(["samsung", "apple"], ["apple", "sony", "xiaomi"]))
    # ["samsung", "apple", "sony", "xiaomi"]

    print(join_array_remove_duplicate(["football", "basketball"], ["basketball", "football"]))
    # ["football", "basketball"]
