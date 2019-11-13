from sudoku_grid import SudoCell
for i in range(1,10):
    for j in range(1,10):
        extra_x = int((j - 1)/ 3)
        extra_y = int((i - 1)/ 3)
        if i == 1 and j == 1:
            locals()['cell' + str(i) + '_' + str(j)] = SudoCell(64 + (j - 1)*30 + extra_x, 200 + (i - 1) * 30 + extra_y, [i,j], 0, 1)
            print(cell1_1.rect,  cell1_1.location)
        else:
            locals()['cell' + str(i) + '_' + str(j)] = SudoCell(64 + (j - 1)*30 + extra_x, 200 + (i - 1) * 30 + extra_y, [i,j], 0, 0)
# print(cell1_1.rect,  cell1_1.location)
# print(cell1_2.rect,  cell1_2.location)
# print(cell1_3.rect,  cell1_1.location)
# print(cell1_4.rect,  cell1_1.location)
# print(cell1_5.rect,  cell1_1.location)
# print(cell1_6.rect,  cell1_1.location)
# print(cell1_7.rect,  cell1_1.location)
# print(cell1_8.rect,  cell1_1.location)
# print(cell1_9.rect,  cell1_9.location)

# print(cell1_1.rect,  cell1_1.location)
# print(cell2_1.rect,  cell1_2.location)
# print(cell3_1.rect,  cell1_1.location)
# print(cell4_1.rect,  cell1_1.location)
# print(cell5_1.rect,  cell1_1.location)
# print(cell6_1.rect,  cell1_1.location)
# print(cell7_1.rect,  cell1_1.location)
# print(cell8_1.rect,  cell1_1.location)
# print(cell9_1.rect,  cell1_9.location)

