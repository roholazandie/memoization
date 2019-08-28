from functools import lru_cache


@lru_cache(maxsize=None)
def count_n_ways(dist):
    # Base cases
    if dist < 0:
        return 0

    if dist == 0:
        return 1

    # Recur for all previous 3 and
    # add the results
    return (count_n_ways(dist - 1) +
            count_n_ways(dist - 2) +
            count_n_ways(dist - 3))


if __name__ == "__main__":
    dist = 40
    print(count_n_ways(dist))
