def get_indices_of_item_weights(weights, length, limit):
    # make an empty cache
    cache = {}

    # storing the weights with index as value

    for k, v in enumerate(weights):
        cache[v] = k

    # find the indicies that sum up to the limit value

    for k, w in enumerate(weights):
        # check if limit - weight is in cache
        if (limit - w) in cache:
            # if it is, and is greater than k, return answer as tuple
            if cache[limit-w] > k:
                return (cache[limit-w], k)

            # if it is not greater, flip the tuple
            else:
                return (k, cache[limit-w])


# # for testing
#
# wt = [ 4, 6, 10, 15, 16 ]
# len = 5
# lim = 16
#
# print(get_indices_of_item_weights(wt, len, lim))
