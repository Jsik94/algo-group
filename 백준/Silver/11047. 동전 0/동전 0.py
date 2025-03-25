if __name__ == "__main__":
    n, k = map(int, input().split(' '))

    account_list = [int(input()) for _ in range(n)]

    # Sort account values in descending order
    account_list.sort(reverse=True)

    cnt = 0
    for account_value in account_list:
        if k == 0:
            break  # No need to continue if k is zero
        if k >= account_value:
            # How many times we can subtract account_value from k
            cnt += k // account_value
            k %= account_value  # Update k to the remainder

    print(cnt)
