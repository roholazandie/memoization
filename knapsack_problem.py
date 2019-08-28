# Returns the maximum value that can be put in a knapsack of
# capacity W
from functools import lru_cache


#@lru_cache(maxsize=None)
def knapsack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapsack(W, wt, val, n - 1)

        # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n - 1] + knapsack(W - wt[n - 1], wt, val, n - 1),
                   knapsack(W, wt, val, n - 1))


if __name__ == "__main__":
    # To test above function
    val = [60, 100, 120, 100, 10, 30, 100, 50, 10]
    wt = [10, 20, 30, 10, 20, 30, 40, 10, 5]
    W = 500
    n = len(val)
    print(knapsack(W, wt, val, n))