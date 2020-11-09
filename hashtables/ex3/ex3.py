def intersection(arrays):
    cache = {}
    # loop through every subarray in our list of arrays
    for subarray in arrays:
        # if not in cache, add it
        for i in subarray:
            if i not in cache:
                cache[i] = 0
            else:
                cache[i] += 1

    result = []
    # if the index value is == the number of ararys, it is in all of them
    for k in cache:
        if cache[k] == len(arrays) - 1:
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
