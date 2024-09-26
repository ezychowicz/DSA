def tanagram(x,y,t):
    N = len(x)
    if len(x) != len(y):
        return False
    count = [0]*(ord('z') - ord('a') + 1)
    available = [[] for _ in range (ord('z') - ord('a') + 1)]
    for i in range (N):
        available[ord(x[i]) - ord('a')].append(i)
    for i in range (N):
        if not available[ord(y[i]) - ord('a')] or count[ord(y[i]) - ord('a')] >= len(available[ord(y[i]) - ord('a')]):
            return False
        else:
            if available[ord(y[i]) - ord('a')][count[ord(y[i]) - ord('a')]] < i - t or available[ord(y[i]) - ord('a')][count[ord(y[i]) - ord('a')]] > i + t:
                return False
            count[ord(y[i]) - ord('a')] += 1
    return True
print(tanagram("kotomysz","tokmysoz",3))