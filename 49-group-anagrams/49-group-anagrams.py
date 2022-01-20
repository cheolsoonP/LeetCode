class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            # dict[키].append(값)
            # sorted는 list로 형태를 반환, join으로 합쳐주어 키로 만듦.
            anagrams[''.join(sorted(word))].append(word)
            
        return list(anagrams.values())