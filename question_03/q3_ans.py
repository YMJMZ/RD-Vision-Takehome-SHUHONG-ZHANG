import torch

def corr2d(X, K): # 2D cross correlation
    m, n = K.shape
    res = torch.zeros((X.shape[0] + m - 1, X.shape[1] + n + 1))
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            res[i,j] = torch.sum(X[i: i+m, j:j+n] * K)
    return res

X = torch.ones((6, 8))
X[:, 2:6] = 0
K = torch.tensor([1, 0, -1]).repeat(3,1) # Vertical Edge filter
K = torch.transpose(K, 0, 1) # Horizontal Edge filter
Y = corr2d(X, K)