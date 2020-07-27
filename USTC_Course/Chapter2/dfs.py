def dfs_re(G, s, dis):
    print(s)
    for w in G[s]:
        if w not in dis:
            dis.add(w)
            dfs_re(G, w, dis)


def dfs_iter(G, s):
    stack = [s]
    dis = set(s)
    while len(stack) > 0:
        top = stack.pop()
        for w in G[top]:
            if w not in dis:
                dis.add(w)
                stack.append(w)
        print(top)


def bfs(G, s):
    deque = [s]
    dis = set(s)
    while len(deque) > 0:
        top = deque.pop(0)
        for w in G[top]:
            if w not in dis:
                dis.add(w)
                deque.append(w)
        print(top)


if __name__ == '__main__':
    G = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E"],
        "D": ["B", "F"],
        "E": ["C", "F"],
        "F": ["D", "E"]
    }
    s = "A"
    dis = set(s)
    # dfs_iter(G, s)
    # dfs_re(G, s, dis)
    bfs(G, s)
