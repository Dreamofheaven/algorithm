def solution(records):
    answers = []
    my_dict = {}
    result = []
    
    for record in records:
        record_list = record.split()
        
        if record_list[0] != 'Leave':
            my_dict[record_list[1]] = record_list[-1] 
        
        if record_list[0] == 'Enter' or record_list[0] == 'Leave':
            answers.append((record_list[1], record_list[0]))
            
    for answer in answers:
        user = my_dict[answer[0]]
        if answer[-1] == 'Enter':
            result.append( user + '님이 들어왔습니다.')
        elif answer[-1] == 'Leave':
            result.append( user + '님이 나갔습니다.' )
    
    return result