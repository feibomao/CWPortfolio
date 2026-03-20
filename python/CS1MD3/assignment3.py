from typing import List

def insert(data, s: str)-> None:
    if s == "":
        return
    if len(s) == 1:
        if s in data:
            data[s][1] = True
        else:
            data[s] = [{}, True]
    if s[0] in data:
        insert(data[s[0]][0], s[1:])
    else:
        data[s[0]]= [{}, False]
        insert(data[s[0]][0], s[1:])

def count_words(data)->int:
    """
    Returns the number of words encoded in data. You may assume
    data is a valid trie.

    >>> data = {}
    >>> insert(data, "test")
    >>> insert(data, "testing")
    >>> insert(data, "doc")
    >>> insert(data, "docs")
    >>> insert(data, "document")
    >>> insert(data, "documenting")

    >>> count_words(data)
    6
    """
    total = 0
    
    for letter in data:
        if data[letter][1]:
            total += 1
        if data[letter][0] != {}:
            total += count_words(data[letter][0])
    
    return total

def contains(data, s: str)-> bool:
    """
    Returns True if and only if s is encoded within data. You may
    assume data is a valid trie.

    >>> data = {}
    >>> insert(data, "tree")
    >>> insert(data, "trie")
    >>> insert(data, "try")
    >>> insert(data, "trying")
    
    >>> contains(data, "try")
    True
    >>> contains(data, "trying")
    True
    >>> contains(data, "the")
    False
    """
    if len(s) == 0:
        return False

    head = s[0]
    rest = s[1:]

    if head in data:
        nxt = data[head]
        if len(s) == 1:
            return nxt[1]

        '''
            if nxt[1] == True:
                return True
            return False
        '''
        return contains(nxt[0], rest)
    return False

def height(data)->int:
    """
    Returns the length of longest word encoded in data. You may
    assume that data is a valid trie.

    >>> data = {}
    >>> insert(data, "test")
    >>> insert(data, "testing")
    >>> insert(data, "doc")
    >>> insert(data, "docs")
    >>> insert(data, "document")
    >>> insert(data, "documenting")

    >>> height(data)
    11
    """

    def word_lengths (defs, length, L):
        for ch in defs:
            char = defs[ch]
            if char[1] == True:
                L.append(length)
            if char[0] != {}:
                word_lengths (char[0], length+1,L)

    lens_list = []
    word_lengths(data,1,lens_list)
    if lens_list == []:
        return 0
    return max(lens_list)
    

def count_from_prefix(data, prefix: str)-> int:
    """
    Returns the number of words in data which starts with the string
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.

    data = {}
    >>> insert(data, "python")
    >>> insert(data, "pro")
    >>> insert(data, "professionnal")
    >>> insert(data, "program")
    >>> insert(data, "programming")
    >>> insert(data, "programmer")
    >>> insert(data, "programmers")

    >>> count_from_prefix(data, 'pro')
    5
    """
    if prefix == "":
        return 0
    
    def from_prefix (trie,pref):
        if len(pref) == 0:
            return trie
        
        head = pref[0]
        tail = pref[1:]

        if head in trie:
            return from_prefix(trie[head][0],tail)
        return {}

    rest = from_prefix(data,prefix)
    return count_words(rest)

def get_suggestions(data, prefix:str)-> List[str]:
    """
    Returns a list of words which are encoded in data, and starts with
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.

    data = {}
    >>> insert(data, "python")
    >>> insert(data, "pro")
    >>> insert(data, "professionnal")
    >>> insert(data, "program")
    >>> insert(data, "programming")
    >>> insert(data, "programmer")
    >>> insert(data, "programmers")

    >>> get_suggestions(data, "progr")
    ['program', 'programming', 'programmer', 'programmers']
    """

    if prefix == "":
        return []

    def from_prefix (trie,pref):
        if len(pref) == 0:
            return trie
        
        head = pref[0]
        tail = pref[1:]

        if head in trie:
            return from_prefix(trie[head][0],tail)
        return {}

    def word_list (defs, word, L):
        for ch in defs:
            char = defs[ch]
            if char[1] == True:
                L.append(word+ch)
            if char[0] != {}:
                word_list(char[0], word+ch, L)

    words = []
    word_list(from_prefix(data,prefix) , prefix , words)
    return words
