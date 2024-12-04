# AoC 2024
# Dec04
# Part 2

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


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

for row_num in range(len(data)):
    #Xs.extend([(row_num, idx) for idx in find_letter(data[row_num], "X")])
    Ms.extend([(row_num, idx) for idx in find_letter(data[row_num], "M")])
    As.extend([(row_num, idx) for idx in find_letter(data[row_num], "A")])
    Ss.extend([(row_num, idx) for idx in find_letter(data[row_num], "S")])

#print(Xs)
print(Ms)
print(As)
print(Ss)

MAS_NW = neighbors(neighbors(Ms, As)["NW"], Ss)
MAS_NE = neighbors(neighbors(Ms, As)["NE"], Ss)
MAS_SW = neighbors(neighbors(Ms, As)["SW"], Ss)
MAS_SE = neighbors(neighbors(Ms, As)["SE"], Ss)

MAS_NW_Alist = [(ele[0]+1,ele[1]+1) for ele in MAS_NW["NW"]]
MAS_NE_Alist = [(ele[0]+1,ele[1]-1) for ele in MAS_NE["NE"]]
MAS_SW_Alist = [(ele[0]-1,ele[1]+1) for ele in MAS_SW["SW"]]
MAS_SE_Alist = [(ele[0]-1,ele[1]-1) for ele in MAS_SE["SE"]]

#XMAS_NW = neighbors(neighbors(neighbors(Xs, Ms)["NW"], As)["NW"], Ss)
#XMAS_N  = neighbors(neighbors(neighbors(Xs, Ms)["N"],  As)["N"], Ss)
#XMAS_NE = neighbors(neighbors(neighbors(Xs, Ms)["NE"], As)["NE"], Ss)
#XMAS_W  = neighbors(neighbors(neighbors(Xs, Ms)["W"],  As)["W"], Ss)
#XMAS_E  = neighbors(neighbors(neighbors(Xs, Ms)["E"],  As)["E"], Ss)
#XMAS_SW = neighbors(neighbors(neighbors(Xs, Ms)["SW"], As)["SW"], Ss)
#XMAS_S  = neighbors(neighbors(neighbors(Xs, Ms)["S"],  As)["S"], Ss)
#XMAS_SE = neighbors(neighbors(neighbors(Xs, Ms)["SE"], As)["SE"], Ss)
print('------------')
print('MAS_NW:')
print(MAS_NW["NW"])

print('------------')
print('MAS_NW_Alist:')
print(MAS_NW_Alist)

MAS_NW_NE_overlap = intersection(MAS_NW_Alist, MAS_NE_Alist)
MAS_NW_SW_overlap = intersection(MAS_NW_Alist, MAS_SW_Alist)
MAS_NE_SE_overlap = intersection(MAS_NE_Alist, MAS_SE_Alist)
MAS_SW_SE_overlap = intersection(MAS_SW_Alist, MAS_SE_Alist)

X_MAS_count = len(MAS_NW_NE_overlap) + len(MAS_NW_SW_overlap) + len(MAS_NE_SE_overlap) + len(MAS_SW_SE_overlap)
print("Number of X-MAS's: " + str(X_MAS_count))

#XMAS_count = len(XMAS_NW["NW"]) + len(XMAS_N["N"]) + len(XMAS_NE["NE"]) + len(XMAS_W["W"]) + len(XMAS_E["E"]) + len(XMAS_SW["SW"]) + len(XMAS_S["S"]) + len(XMAS_SE["SE"])
#print("Number of XMAS's: " + str(XMAS_count))
