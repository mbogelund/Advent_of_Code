# AoC 2024
# Dec04
# Part 1

import re

# Import today's data
#data = [l.strip() for l in open("Input/example.txt", "rt")]
data = [l.strip() for l in open("Input/input.txt", "rt")]
print(data)
print("----------------")

Xs = []
Ms = []
As = []
Ss = []

def find_letter(s, ch):
    return [idx for idx, letter in enumerate(s) if letter == ch]

def neighbors(letter_list, next_letter_list):
    
    NWlist = []
    N_list = []
    NElist = []
    W_list = []
    E_list = []
    SWlist = []
    S_list = []
    SElist = []
    for letter in letter_list:
        nw = (letter[0]-1, letter[1]-1) 
        n_ = (letter[0]-1, letter[1])
        ne = (letter[0]-1, letter[1]+1)
        w_ = (letter[0], letter[1]-1)
        e_ = (letter[0], letter[1]+1)
        sw = (letter[0]+1, letter[1]-1)
        s_ = (letter[0]+1, letter[1])
        se = (letter[0]+1, letter[1]+1)

        if nw in next_letter_list:
            NWlist.append(nw)
        if n_ in next_letter_list:
            N_list.append(n_)
        if ne in next_letter_list:
            NElist.append(ne)
        if w_ in next_letter_list:
            W_list.append(w_)
        if e_ in next_letter_list:
            E_list.append(e_)
        if sw in next_letter_list:
            SWlist.append(sw)
        if s_ in next_letter_list:
            S_list.append(s_)
        if se in next_letter_list:
            SElist.append(se)
        
        rDict = {"NW": NWlist,
                 "N" : N_list,
                 "NE": NElist,
                 "W" : W_list,
                 "E" : E_list,
                 "SW": SWlist,
                 "S" : S_list,
                 "SE": SElist
                 }
        
    return rDict


for row_num in range(len(data)):
    Xs.extend([(row_num, idx) for idx in find_letter(data[row_num], "X")])
    Ms.extend([(row_num, idx) for idx in find_letter(data[row_num], "M")])
    As.extend([(row_num, idx) for idx in find_letter(data[row_num], "A")])
    Ss.extend([(row_num, idx) for idx in find_letter(data[row_num], "S")])

print(Xs)
print(Ms)
print(As)
print(Ss)

XM = neighbors(Xs, Ms)
print(XM)

XMA_NW = neighbors(neighbors(Xs, Ms)["NW"], As)
print('------------')
print('XMA_NW:')
print(XMA_NW["NW"])

XMAS_NW = neighbors(neighbors(neighbors(Xs, Ms)["NW"], As)["NW"], Ss)
XMAS_N  = neighbors(neighbors(neighbors(Xs, Ms)["N"],  As)["N"], Ss)
XMAS_NE = neighbors(neighbors(neighbors(Xs, Ms)["NE"], As)["NE"], Ss)
XMAS_W  = neighbors(neighbors(neighbors(Xs, Ms)["W"],  As)["W"], Ss)
XMAS_E  = neighbors(neighbors(neighbors(Xs, Ms)["E"],  As)["E"], Ss)
XMAS_SW = neighbors(neighbors(neighbors(Xs, Ms)["SW"], As)["SW"], Ss)
XMAS_S  = neighbors(neighbors(neighbors(Xs, Ms)["S"],  As)["S"], Ss)
XMAS_SE = neighbors(neighbors(neighbors(Xs, Ms)["SE"], As)["SE"], Ss)
print('------------')
print('XMAS_NW:')
print(XMAS_NW["NW"])

XMAS_count = len(XMAS_NW["NW"]) + len(XMAS_N["N"]) + len(XMAS_NE["NE"]) + len(XMAS_W["W"]) + len(XMAS_E["E"]) + len(XMAS_SW["SW"]) + len(XMAS_S["S"]) + len(XMAS_SE["SE"])
print("Number of XMAS's: " + str(XMAS_count))
