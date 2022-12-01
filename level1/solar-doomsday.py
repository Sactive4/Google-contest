
def solution(area: int):
    squares_list = []
    res_list = []
    cur_area = area
    
    # calculating list of square numbers
    num = 1
    while num*num <= area:
        squares_list.append(num*num)
        num = num + 1
    
    # bin search
    while cur_area > 0:
        left_idx = 0
        right_idx = len(squares_list)-1
        
        while left_idx <= right_idx:
            mid_idx = (right_idx + left_idx)//2
            mid = squares_list[mid_idx]
            
            if mid <= cur_area:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
        
        closest_panel_id = right_idx
        
        res_list.append(squares_list[closest_panel_id])
        cur_area = cur_area - squares_list[closest_panel_id]
    
    return res_list

print(solution(12))
