n = int(input())
for _ in range(n):
    word = input().strip()
    globals().setdefault('perms', {}).setdefault(''.join(sorted(word)), []).append(word)
m = int(input())
for _ in range(m):
    print(*sorted(globals()['perms'].get(''.join(sorted(input().strip())), [])), sep=' ')
