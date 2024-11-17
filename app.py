import numpy as np

def calculate(input):
    matrix = np.array(input).reshape(3, 3)

    calculations ={
        'mean':[
           # row
           matrix.mean(axis=0).tolist(),
           # col
           matrix.mean(axis=1).tolist(),
           matrix.mean().tolist()
],
'variance':[
         # row
         matrix.var(axis=0).tolist(),
         # col
         matrix.var(axis=1).tolist(),
         matrix.var().tolist()
],
'standard deviation':[
    # row
    matrix.std(axis=0).tolist(),
    # col
    matrix.std(axis=1).tolist(),
    matrix.std().tolist()

]
,
'max':[
     # row
    matrix.max(axis=0).tolist(),
    # col
    matrix.max(axis=1).tolist(),
    matrix.max().tolist()
],

'min':[
    # row
    matrix.min(axis=0).tolist(),
    # col
    matrix.min(axis=1).tolist(),
    matrix.min().tolist() 
],

'sum':[
     # row
    matrix.sum(axis=0).tolist(),
    # col
    matrix.sum(axis=1).tolist(),
    matrix.sum().tolist()
]
}
    return calculations


print(calculate([0,1,2,3,4,5,6,7,8]))