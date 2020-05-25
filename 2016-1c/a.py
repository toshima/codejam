for tc in range(int(raw_input())):
    raw_input()
    parties = {}
    for i, s in enumerate(raw_input().split()):
        party = chr(ord('A') + i)
        parties[party] = int(s)

    print "Case #%d:" % (tc+1),

    while parties:
        s = sorted(parties, key=parties.get)[::-1]
        if len(s) > 1 and len(parties) != 3:
            parties[s[0]] -= 1
            parties[s[1]] -= 1
            print s[0] + s[1],
            if not parties[s[0]]:
                del parties[s[0]]
            if not parties[s[1]]:
                del parties[s[1]]
        else:
            parties[s[0]] -= 1
            print s[0],
            if not parties[s[0]]:
                del parties[s[0]]

    print
