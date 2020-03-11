count_val =0
def dfs(numbers,target,depth,sums):
    global count_val
    depth = depth
    if depth == len(numbers):
        if sums == target:
            count_val += 1
            return
        else:
            return

    dfs(numbers,target,depth+1,sums+numbers[depth] )
    dfs(numbers,target,depth+1,sums-numbers[depth] )
        
def solution(numbers, target):
   
    
    dfs(numbers,target,0,0)
    return count_val

