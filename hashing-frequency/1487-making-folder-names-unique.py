#  names = ["pes","fifa","gta","pes(2019)"]
# at ith minute create a folder with the name names[i] if dupl

# hash map for frequency counting
# question asks for an array, making a new result array instead of in place
# track suffixes for base names
# track smallest next available suffix
# mark unique names as used

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        used = {} # stores next available suffix by nam
        result = []
        
        for name in names:
            if name not in used:
                result.append(name)
                used[name] = 1  
            else:
                k = used[name]
                while f"{name}({k})" in used: # will skip over names like onepiece(6) that were created before onepiece(4)
                    k += 1
                new_name = f"{name}({k})"
                result.append(new_name)
                used[name] = k + 1 
                used[new_name] = 1 
                
        return result
