def rows(letter):
    pos = ord(letter) - ord('A')
    
    num_rows = pos
    middle_space = 0
    row_letter = 'A'
    
    diamond_list = []
    
    for i in range(pos + 1):
        cur_str = ''
        for j in range(pos):
            cur_str = cur_str + ' '
         
        cur_str = cur_str + row_letter
        
        for k in range(middle_space):
            cur_str = cur_str + ' '
        
        if i != 0:
            cur_str = cur_str + row_letter
            
        for j in range(pos):
            cur_str = cur_str + ' '
            
        pos = pos - 1
        middle_space = middle_space + 2
        
        diamond_list.append(cur_str)
    
    j = len(diamond_list) - 2
    for i in range(num_rows):
        diamond_list-append(diamond_list[j])
        
    return diamond_list
        
            
            
        
