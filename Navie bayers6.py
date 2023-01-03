import pandas as pd
data=pd.read_csv('tennisdata.csv')
te=len(data)
np=len(data.loc[data[data.columns[-1]]=='Yes'])
nn=te-np
training=data.sample(frac=0.75,replace=False)
test=pd.concat([data,training]).drop_duplicates(keep=False)
print('training set:',training)
print('test set:',test)
prob={}
for col in training.columns[:-1]:
    prob[col]={}
    vals=set(data[col])
    for val in vals:
        temp=training.loc[data[col]==val]
        pe=len(temp.loc[temp[temp.columns[-1]]=='Yes'])
        ne=len(temp)-pe
        prob[col][val]=[pe/np,ne/nn]
prediction=[]
right_prediction=0
for i in range(len(test)):
    row=test.iloc[i,:]
    fpp=np/te
    fnn=nn/te
    for col in test.columns[:-1]:
        fpp*=prob[col][row[col]][0]
        fnn*=prob[col][row[col]][1]
    if fpp>fnn:
        prediction.append('Yes')
    else:
        prediction.append('No')
    if prediction[-1]==row[-1]:
        right_prediction+=1
print('actual:',list(test[test.columns[-1]]))
print('presicted:',prediction)
print('accuracy:',right_prediction/len(test))
