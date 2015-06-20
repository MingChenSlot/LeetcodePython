__author__ = 'mingchen'

# @param {string} s
# @param {string} t
# @return {boolean}
def isIsomorphic(s, t):
    if s == t:
        return True
    if len(s) is not len(t):
        return False

    char_map = {}
    for(first, second) in zip(s, t):
        if first not in char_map:
            if second in char_map.values():
                return False
            char_map[first] = second
        else:
            if char_map[first] is not second:
                return False
    return True

if __name__ == "__main__":
    print isIsomorphic("egg", "add")
    print isIsomorphic("foo", "bar")
    print isIsomorphic("paper", "title")
    print isIsomorphic("abcd#*$#&*", "abcd#*$#&*")
