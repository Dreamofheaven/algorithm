from collections import deque

def solution(queue1, queue2):
    Q_sum = (sum(queue1) + sum(queue2)) // 2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    # 큐1을 대상으로 잡고, 큐1의 합이 Q_sum이랑 같게 될 때까지 반복
    q1_sum = sum(q1)
    answer = 0
    
    while q1_sum != Q_sum:
        if q1_sum < Q_sum:
            item = q2.popleft()
            q1.append(item)
            q1_sum += item
        else:
            item = q1.popleft()
            q1_sum -= item
            
        if not q2:
            return -1
        
        answer += 1
    
    return answer
    
    