curr_ele = 0
col_elems = {}
 
def rec(curr_col, gr):
    global curr_ele
    global col_elems
    if gr[curr_ele] == '.':
        curr_ele += 1
        return
    ele = gr[curr_ele]
    if curr_col not in col_elems:
        col_elems[curr_col] = [ele]
    else:
        col_elems[curr_col].append(ele)
    curr_ele += 2
    rec(curr_col-1, gr)
    rec(curr_col+1, gr)
    curr_ele += 1
 
def solve():
    global col_elems
    inp = input().split()
    col = int(inp[0])
    gr = inp[1]
    rec(0, gr)
    if col in col_elems:
        print("".join(sorted(col_elems[col])))
    else:
        print("Common Gandhijee!")
 
    
for _ in range(int(input())):
    curr_ele = 0
    col_elems = {}
    solve()
