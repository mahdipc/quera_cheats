def words_check(text):
    alpha = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    words = text.split()
    res = []
    for word in words:
        s = ''
        for w in word:
            if w in alpha:
                s += w
        if len(s)*2 > len(word):
            res.append(s[0].upper()+s[1:].lower())
    return dict((x, res.count(x)) for x in set(res))


