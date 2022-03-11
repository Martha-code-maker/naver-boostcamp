import numpy as np

xy = np.array([[1.,2.,3.,4.,5.,6.],
              [10.,20.,30.,40.,50.,60.]])


x_train = xy[0]             # 입력값
y_train = xy[1]             # 정답값    #데이터 분리

beta_gd = np.random.rand(1)     # 직선의 기울기,weight
bias = np.random.rand(1)        # y절편

learning_rate = 0.001


for i in range(1000):
    pred = (x_train * beta_gd) + bias
    error = ((pred - y_train) ** 2).mean()

    beta_gd -= learning_rate * ((pred-y_train) * x_train * 2).mean()
    bias -= learning_rate * ((pred-y_train) * 2).mean()

    if i % 100 == 0 :
        print("Epoch ({:10d}/1000) error: {:10f}, beta_gd: {:10f}, bias: {:10f}".format(i,error,beta_gd.item(),bias.item()))

