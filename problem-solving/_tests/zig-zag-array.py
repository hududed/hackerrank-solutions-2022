# https://codescript.in/mountblue-technologies-question-asked-on-23-january-2021/128/


def minOperation(arr):
    # A = arr
    # A = [float('inf')] + A + [float('inf')]
    # # print(A)
    # res = [0, 0]
    # for i in range(1, len(A) - 1):
    #     res[i % 2] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)
    #     print(i, max(0, A[i] - min(A[i - 1], A[i + 1]) + 1), res)
    # return min(res)

    nums = arr
    nums = [float('inf')]+nums+[float('inf')]
    n1 = 0
    for i in range(1, len(nums)-1, 2):
        if nums[i] >= min(nums[i-1], nums[i+1]):
            n1 += nums[i]-min(nums[i-1], nums[i+1])+1
    n2 = 0
    for i in range(2, len(nums)-1, 2):
        if nums[i] >= min(nums[i-1], nums[i+1]):
            n2 += nums[i]-min(nums[i-1], nums[i+1])+1
    return min(n1, n2)


def main():
    arr = [1, 2, 3, 4, 5]
    res = minOperation(arr)
    print(res)


if __name__ == "__main__":
    main()
