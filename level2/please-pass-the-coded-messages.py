def list_to_int(l):
    if not l:
        return 0
    return int("".join([str(e) for e in l]))

def solution(l):
    l = sorted(l, reverse=True)
    idx_last = len(l) - 1
    s_3 = sum(l) % 3 
    
    if s_3 == 0:
        return list_to_int(l)
    
    elif s_3 == 1:
        for i in range(idx_last, 0 - 1, -1):
            if l[i] % 3 == 1:
                return list_to_int(l[:i] + l[i+1:])
        
        i = idx_last
        while i >= 0:
            if l[i] % 3 == 2:
                break
            i -= 1
            
        j = i - 1
        while j >= 0:
            if l[j] % 3 == 2:
                break
            j -= 1
        return list_to_int(l[:j] + l[j+1:i] + l[i+1:])
    else:
        for i in range(idx_last, 0 - 1, -1):
            if l[i] % 3 == 2:
                return list_to_int(l[:i] + l[i+1:])
            i -= 1
            
        i = idx_last
        while i >= 0:
            if l[i] % 3 == 1:
                break
            i -= 1
        j = i - 1
        while j >= 0:
            if l[j] % 3 == 1:
                break
            j -= 1
        return list_to_int(l[:j] + l[j+1:i] + l[i+1:])