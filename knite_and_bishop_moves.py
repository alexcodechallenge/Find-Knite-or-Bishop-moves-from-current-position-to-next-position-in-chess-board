from itertools import product
def knight_moves(currentpos,nextpos):
    x,y = currentpos
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]    
    #print(moves)
    if nextpos in moves:
        return True
    else:
        return False
def bishop_moves(currentpos, nextpos) :
    bishopX, bishopY = currentpos
    pawnX, pawnY = nextpos
    if (pawnX - bishopX == pawnY - bishopY) :
        return True
    elif (-pawnX + bishopX == pawnY - bishopY):
        return True     
    else:
        return False     
def valid_move_or_not(piece,currentpos,nextpos):
    #your code goes here
    my_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    cur = currentpos
    cur = list(cur)
    nxt = nextpos
    nxt = list(nxt)
    currentpos = (int(my_dict[cur[0]]),int(cur[1]))
    nextpos = (int(my_dict[nxt[0]]),int(nxt[1]))    
    if piece=='Knight':
        rslt = knight_moves(currentpos,nextpos)
    elif piece=='Bishop':
        rslt = bishop_moves(currentpos,nextpos)
    else:
        return False
    return rslt
    return True

if __name__=='__main__':
    #you can run your tests here
    print(valid_move_or_not("Knight","e5","g4"))
    print(valid_move_or_not("Bishop","d5","f4"))
