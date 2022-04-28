import numpy as np

def solve_normaleq(A, b):
    trans_A = A.T #Aの転置行列
    b_h = len(b)
    AA_inv_trans_A = np.dot(np.linalg.inv(np.dot(trans_A, A)), trans_A) #Aの逆行列とAの積の逆行列とAの転置行列の積．
    
    AA_h, AA_w = AA_inv_trans_A.shape
    
    if(AA_w != b_h):
        print("Aの逆行列の列数と行列bの行数が等しくありません")
        exit()
    answer = np.dot(AA_inv_trans_A, b)
    return answer


A = np.array([[2, 1], [4, 1], [9, 1]])
b = np.array([3, 7, 11])
print(solve_normaleq(A, b))
