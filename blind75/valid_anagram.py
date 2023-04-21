s = "anagram"
t = "nagaram"

s1 = "aabbbb"
t1 = "aaaabb"

s_dict = {}
t_dict = {}


def check_anagram(s, t):
    if len(t) == len(s):
        for i in range(len(s)):
            # s_dict[s[i]] = 1 + s_dict.get(s[i],0)
            # t_dict[t[i]] = 1 + t_dict.get(t[i],0)

            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1

            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
    else:
        print('len not same')
        return False

    for i in s_dict:
        if i not in t_dict:
            print('t not in s')
            return False
        if t_dict[i] != s_dict[i]:
            print('t not same with s')
            return False
    return True


def neetcode(s, t):
    if len(s) != len(t):
        return False
    hashs = {}
    hasht = {}
    for i in range(len(s)):
        hashs[s[i]] = 1+hashs.get(s[i], 0)
        hasht[t[i]] = 1+hasht.get(t[i], 0)

    for i in hashs:
        if hashs[i] != hasht.get(i, 0):
            return False
    return True


print(check_anagram(s1, t1))
print(neetcode(s1, t1))
print(f's_dict : {s_dict}')
print(f't_dict : {t_dict}')
if 'x' not in s_dict:
    print('not')
