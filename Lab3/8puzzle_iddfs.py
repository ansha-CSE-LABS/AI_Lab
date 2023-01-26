def dfs(src,target,limit,visited_states):
    if src == target:
        return True
    if limit <= 0:
        return False
    visited_states.append(src)
    moves = possible_moves(src,visited_states)   
    for move in moves:
        if dfs(move, target, limit-1, visited_states):
            return True
    return False
def possible_moves(state,visited_states):
    b=state.index(-1)
    d=[]
    if b not in (0,1,2):
        d.append("up")
    if b not in (6,7,8):
        d.append("down")
    if b not in (0,3,6):
        d.append("left")
    if b not in (2,5,8):
        d.append("right")
    return [ move for move in gen(state,b,d) if move not in visited_states]
def gen(state,b,d):
    x=[]
    for i in d:
        temp=state.copy()
        if i == "up":
            temp[b-3],temp[b]=temp[b],temp[b-3]
        elif i=="down":
            temp[b+3],temp[b]=temp[b],temp[b+3]
        elif i=="right":
            temp[b+1],temp[b]=temp[b],temp[b+1]
        elif i=="left":
            temp[b-1],temp[b]=temp[b],temp[b-1]
        x.append(temp)
    return x
def iddfs(src,target,depth):
    for i in range(depth):
        visited_states = []
        if dfs(src,target,i+1,visited_states):
            return True
    return False
src = [1,2,3,-1,4,5,6,7,8] 
target=[1,2,3,6,4,5,-1,7,8]

depth = 1
iddfs(src, target, depth)
