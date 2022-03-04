score = [(100,100), (95,90), (55,60), (75,80), (70,70)]

def get_avg(score):
    for i in range(len(score)):
        avg = 0
        for j in range(len(score[i])):
            avg = avg + score[i][j]
        print('number', i+1, 'average : ', avg/2)


get_avg(score)