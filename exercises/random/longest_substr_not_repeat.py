def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    # if len(s)==0:
    #     return ''
    i=1
    while i<len(s):
        j=0
        while j<i:
            if s[i] == s[j]:
                ss2 = lengthOfLongestSubstring(s[j+1:])
                if len(ss2)>i:
                    return ss2
                else:
                    return s[:i]
            j=j+1
        i=i+1
    return s
                
mystr=['leloluoipo','heloluoipo', 'abcabcbb', 'a','']
for st in mystr:
    print(f'For "{st}" the longest substring with no repeated '
          f'characters is "{lengthOfLongestSubstring(st)}"')