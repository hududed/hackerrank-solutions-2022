from collections import deque


def rearrange(arr):
    """ only odd indexes from index 3 and above must be minimum
    """
    n = len(arr)
    arr.sort()

    if (len(arr) < 3):
        return arr

    ans = [0]*n
    p = 0
    q = n - 1
    for i in range(n):
        if (i+1) % 2 == 0:
            # even numbers get largest value
            ans[i] = arr[q]
            q -= 1
            print(i, ans)
        else:
            # odd numbers get minimum
            ans[i] = arr[p]
            p += 1

            print(i, ans)
    ans = deque(ans)
    ans.rotate(2)
    # ans[0], ans[1] = ans[1], ans[0]
    return list(ans)

    # # sort the arr to get minimal orde
    # arr = sorted(arr)
    # # return the arr if it contains only two elements
    # if (len(arr) < 3):
    #     return arr
    #     # using smallest number for division gives the maximum product
    #     # remove the first element
    # first_element = arr.pop(0)
    # # insert the first element ar position 3
    # arr.insert(3, first_element)
    # if (len(arr) <= 3):
    #     return arr
    #     # length odd case
    # if (len(arr) % 2 == 1):
    #     # pop the next smallest element and append it to the end of the array
    #     element = arr.pop(0)
    #     arr.append(element)
    #     # return the modified array
    # return arr


if __name__ == "__main__":
    # testing above function
    inp = [5, 7, 9, 21, 34]
    print(inp)
    print(rearrange(inp))
    print([9, 21, 5, 34, 7])
