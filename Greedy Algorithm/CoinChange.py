# /*
# Given a value of V Rs and an infinite supply of each of the denominations {1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, The task is to find the minimum number of coins and/or notes needed to make the change?
#
# Examples:
#
# Input: V = 70
# Output: 2
# Explanation: We need a 50 Rs note and a 20 Rs note.
#
# Input: V = 121
# Output: 3
# Explanation: We need a 100 Rs note, a 20 Rs note, and a 1 Rs coin.

# Solution
def findMin(deno, V):
    ans = []
    i = len(deno) - 1
    while i >= 0:
        while V >= deno[i]:
            V -= deno[i]
            ans.append(deno[i])
        i -= 1

    print(ans)


if __name__ == '__main__':
    deno = [1, 2, 5, 10, 20, 50,
            100, 500, 1000]
    n = 93

    findMin(deno, n)
