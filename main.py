def searchM(mat, value):
  #validation if array len = 0 then return False
    if len(mat) == 0:
        return False
      #row_len is amount of rows in mat array (row_len = 3)
      #col_len is amount of indexs in mat array[0] (col_len = 4)
    row_len = len(mat)
    col_len = len(mat[0])
  
    low = 0
    high = row_len * col_len

    while low < high:
        mid = (low + high) // 2
      #mid // col_len is row position e.g, row 0 is [1, 5, 7, 9]
      #mid modulo col_len is colum position e.g, [2] is '7' in row 0
        if mat[mid // col_len][mid % col_len] == value:
            return True
          #if smaller than value then position moves left
        elif mat[mid // col_len][mid % col_len] < value:
            low = mid + 1
        else:
            high = mid
    return False

# 2d array
mat = [
    [1, 5, 7, 9],
    [10, 13, 16, 19],
    [21, 25, 29, 31],
]

print(searchM(mat, 5))
#True
print(searchM(mat, 4))
#False