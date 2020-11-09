def has_negatives(a):
    neg_cache = {}

    for i in a:
        neg_cache[i] = -i

    result = []

    for i in neg_cache.keys():
        if i > 0 and neg_cache[i] in neg_cache:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
