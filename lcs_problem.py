from functools import lru_cache


@lru_cache(maxsize=None)
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


def lcs_dynamic(a, b):
    # generate matrix of length of longest common subsequence for substrings of both words
    lengths = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    # read a substring from the matrix
    result = ''
    j = len(b)
    for i in range(1, len(a) + 1):
        if lengths[i][j] != lengths[i - 1][j]:
            result += a[i - 1]

    return result


if __name__ == "__main__":
    X = "Then if you look at any path in the graph, the diagonal edges form a subsequence of the two strings"
    Y = "Conversely, if you define the horizontal and vertical edges to have length zero, and the diagonal edges to have length one"
    print("Length of LCS is ", lcs(X, Y, len(X), len(Y)))
    print(lcs_dynamic(X, Y))
