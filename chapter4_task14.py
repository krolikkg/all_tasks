def stepPerms(steps):
    cache = [1, 2, 4]
    MAX_STEPS = 36

    assert 0 < steps <= MAX_STEPS

    if steps <= len(cache):
        return cache[steps - 1]

    for _ in range(steps - len(cache)):
        cache.append(cache[-1] + cache[-2] + cache[-3])

    return cache[-1]
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        print(res)
        
stepPerms(10)