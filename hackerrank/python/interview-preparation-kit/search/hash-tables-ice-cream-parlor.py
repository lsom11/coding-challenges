def icecream(flavors, M):
    # O(N) complexity
    flavor_map = {}
    for idx, flavor in enumerate(flavors):
        # subtract from total
        residual = (M - flavor)
        # if the remainder is in the dict we're done, print the sorted indices
        if residual in flavor_map:
            return sorted([flavor_map[residual], idx])
        # else store a copy of the remainder with the index for future use
        if not flavor in flavor_map:
            flavor_map[flavor] = idx


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        flavors = map(int, input().split())
        result_arr = icecream(flavors, m)
        print(result_arr[0]+1, result_arr[1]+1)
