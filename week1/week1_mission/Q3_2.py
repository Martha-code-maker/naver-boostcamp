score = [(100,100), (95,90), (55,60), (75,80), (70,70)]

def get_avg(score):
    avg = list(map(lambda x: (x[0]+ x[1])/2,score))
    for l, s in enumerate(avg):
        print(f'{l+1}번 , 평균 {s}')

get_avg(score) 