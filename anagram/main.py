import collections

def anagram_def(strs : list[str]) -> list[list[str]]:
    anagram = collections.defaultdict(list)
    
    for word in strs:
        anagram[''.join(sorted(word))].append(word)       
    return list(anagram.values())

print(anagram_def(['eat','tea','tan','ate','nat','bat']))