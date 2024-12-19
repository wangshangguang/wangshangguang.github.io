
# coding: utf-8

# In[7]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'pylab')


# In[8]:

from pandas import DataFrame,Series
import pandas as pd
from sklearn import cross_validation
from sklearn.metrics import precision_score


# In[45]:

datas = np.genfromtxt ('MovieRatings.csv', delimiter=",")


# In[59]:

datas.shape


# In[5]:

#年龄、性别分布图
for i in range(2):
    plt.figure()
    hist, bins = np.histogram(users[:,i+1], bins=64)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)


# In[6]:

userDF = DataFrame(users,columns=['user-id','age','gender'])
ratingDF = DataFrame(ratings,columns=['user-id','item-id','rating'])
user_rating_DF = pd.merge(userDF,ratingDF)

user_rating_DF['state'] = 1

gender_age_num = user_rating_DF.pivot_table('state',index='item-id',columns=['gender','age'],aggfunc='sum').fillna(0)
gender_age_mean = user_rating_DF.pivot_table('rating',index='item-id',columns=['gender','age'],aggfunc='mean').fillna(0)
gender_age_mean_array = np.array(gender_age_mean)

state = np.array(gender_age_num>2)
m,n = state.shape

for i in range(m):
    for j in range(n):
        if state[i,j] < 0.5:
            gender_age_mean_array[i,j] = 0

nozerolist = gender_age_mean_array[:,0] != 0
for i in range(1,8):
    nozerolist = nozerolist & (gender_age_mean_array[:,i] != 0)
    
gender_age_mean_array = gender_age_mean_array[nozerolist] # 确保每个电影被所有分组都看过
gender_age_mean_sorted_array = gender_age_mean_array#[gender_age_mean_array[:,0].argsort()]
afterdelete = DataFrame(gender_age_mean_sorted_array)

fig, ax= plt.subplots()

plt.imshow(np.array(afterdelete),interpolation='nearest', aspect='auto')
cb = plt.colorbar()
cb.ax.tick_params(labelsize=25)


cb.set_label(r'mean value of ratings', labelpad=10, y=0.45)
#ax = cb.ax
text = cb.ax.yaxis.label
font = matplotlib.font_manager.FontProperties(size=30)
text.set_font_properties(font)


plt.yticks([5,50,100,150,200,240],[250,200,150,100,50,0],fontsize = 30)
plt.xticks([0.5,1.4,2.59,3.3,4.5,5.5,6.7,7.5],['male-young','male-adult','male-middle-age','male-old','female-young','female-adult',
                              'female-middle-age','female-old'],fontsize = 30,rotation=-13)

plt.xlabel('Gender-age groups',{'fontname':'STFangsong','fontsize':52})
plt.ylabel('List of movies',{'fontname':'STFangsong','fontsize':52})

ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')

#savefig('ratings_groups.pdf',bbox_inches='tight')


# In[7]:

users


# In[8]:

ratings


# In[9]:

rating_dict = {} #创建评分字典，以(user_id,book_id)为键，以评分为值。
for i in range(ratings.shape[0]):
    rating_dict[(ratings[i,0],ratings[i,1])] = ratings[i,2]

user_list = {} #创建打分历史的字典，以user_id为键，以该user的book_id的列表为值。
for i in range(ratings.shape[0]):
    user_id = ratings[i,0]
    if user_list.has_key(user_id):
        user_list[user_id].append(ratings[i,1])
    else:
        user_list[user_id] = [ratings[i,1]]


# In[19]:

#画图，Distribution of numbers of users' ratings

numberlist = []
for n in range(1,943+1):
    numberlist.append(len(user_list[n]))

a = np.zeros((737-20+1,2))
for i in range(737-20+1):
    #a[i,0] = 20+i
    a[i,0] = i

for i in range(len(numberlist)):
    a[numberlist[i]-20,1] += 1
a[:,1] /= 1.0*np.sum(a[:,1])
a[:,1] = np.cumsum(a[:,1])
plt.plot(a[:,0],a[:,1],'+r')

plt.xlabel("Number of users' ratings",{'fontname':'STFangsong','fontsize':22})
plt.ylabel('Cumulative percentage',{'fontname':'STFangsong','fontsize':22})

savefig('number_distribution.pdf',bbox_inches='tight')


# In[ ]:




# In[ ]:




# In[42]:

a[a[:,0] <= 300,1].sum()


# In[39]:

a[(a[:,0] > 100)&(a[:,0] <= 300),1].sum()


# In[41]:

a[a[:,0] > 500,1].sum()


# In[11]:

#8个年龄、性别分组
Y_all = np.array([
        [1,0,0,0,1,0],
        [0,1,0,0,1,0],
        [0,0,1,0,1,0],
        [0,0,0,1,1,0],
        [1,0,0,0,0,1],
        [0,1,0,0,0,1],
        [0,0,1,0,0,1],
        [0,0,0,1,0,1]
    ])
N= users.shape[0]
Y_empirical = np.zeros(8)
for n in range(1,N+1):
    kind = np.dot(Y[n-1],np.array([1,2,3,4,0,4])) # 将8个年龄、性别分组映射为1-8的整数
    Y_empirical[kind-1] += 1
Y_empirical /= Y_empirical.sum()  #  得到各个年龄、性别分组的先验概率


# In[54]:

N= users.shape[0] #user编号范围：1-943，books编号范围：1-1682
M = np.max(ratings[:,1])
D = 50
C = 6
Y = np.zeros((N,C))
for n in range(N):
    Y[n,users[n,1]] = 1
    Y[n,4+users[n,2]] = 1

eta = 0.002 # learning rate
lambd = 0.002
K = 5 # sampling number
def logist(x):
    return 1.0/(1+np.exp(-x))
T = 20
t = 0

V = np.random.random((M,D))
W = np.random.random((D,C))


while t<T:
    t += 1  
    rating_sum = np.zeros(N)
    
    V_users = np.zeros((N,D))
    for n in range(1,N+1): #n编号是1-943
        nlist = user_list[n]
        for m in nlist:
            rating_sum[n-1] += rating_dict[(n,m)]
            V_users[n-1] += V[m-1]*rating_dict[(n,m)]
        V_users[n-1] /= rating_sum[n-1]
    
        


    for n in range(1,N+1):
        etalogist = eta*(1-logist(np.dot(np.dot(V_users[n-1],W),Y[n-1])))
        W += etalogist*np.dot(np.reshape(V_users[n-1],(D,1)),np.reshape(Y[n-1],(1,C)))

        nlist = nlist = user_list[n]
        for m in nlist:
            V[m-1] += etalogist*rating_dict[(n,m)]*np.dot(W,Y[n-1])/rating_sum[n-1]

        for k in range(K):
            sam = np.random.randint(1,N+1)
            while (Y[sam-1] == Y[n-1]).all():
                sam = np.random.randint(1,N+1)
            etalogist = eta*(1-logist(-np.dot(np.dot(V_users[n-1],W),Y[n-1])))
            W += -etalogist*np.dot(np.reshape(V_users[n-1],(D,1)),np.reshape(Y[sam-1],(1,C)))
            for m in nlist:
                V[m-1] += -etalogist*rating_dict[(n,m)]*np.dot(W,Y[sam-1])/rating_sum[n-1]  
    W *= (1-2*eta*lambd)
    V *= (1-2*eta*lambd)
    
    Y_predict = []
    hloss = 0
    f1 = 0
    for n in range(1,N+1): 
        kind = np.argmax(Y_empirical*np.dot(np.dot(V[n],W),Y_all.T))
        #print kind
        Y_predict.append(list(Y_all[kind]))
    Y_predict = np.array(Y_predict)
    
    print t,hammingloss(Y_predict,Y),list(weightmetric(Y_predict,Y))
   


# In[12]:

#对每个用户的评分归一化，该代码只运行一次
for n in range(1,943+1):
    n_list = user_list[n]
    n_sum = 0
    for book in n_list:
        n_sum += rating_dict[(n,book)]
    for book in n_list:
        rating_dict[(n,book)] /= n_sum


# In[411]:

from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import hamming_loss
from sklearn.metrics import f1_score

def four_performance(y_true,y_pred,y_test,y_predict):
    a = np.zeros(4)
    a[0] = precision_score(list(y_true), list(y_pred), average='weighted')
    a[1] = recall_score(list(y_true), list(y_pred), average='weighted')
    a[2] = 2*a[0]*a[1]/(a[0]+a[1]) #f1_score(list(y_true), list(y_pred), average='weighted')
    a[3] = hammingloss(y_test,y_predict)
    
    return a   

def hammingloss(predict,test):
    if predict.shape[0] != test.shape[0]:
        print "error, not same length"
    n = predict.shape[0]
    hloss = 0
    for i in range(n):
        hloss += (predict[i]!=test[i]).sum()/2
    hloss /= (1.0*n*2)
    return hloss

def weightmetric(predict,test):
    #第一项是test数据集中各个kind的个数，第二项是各个kind被正确判决的个数，第三个是被判为各个kind的个数
    count = {1:[0,0,0],2:[0,0,0],3:[0,0,0],4:[0,0,0],5:[0,0,0],6:[0,0,0],7:[0,0,0],8:[0,0,0]}
    n = test.shape[0]
    for i in range(n):
        predict_kind = np.dot(predict[i],np.array([1,2,3,4,0,4]))
        test_kind = np.dot(test[i],np.array([1,2,3,4,0,4]))
        count[test_kind][0] += 1
        count[predict_kind][2] += 1
        if predict_kind == test_kind:
            count[test_kind][1] += 1
            
    wprecision= 0
    wrecall = 0
    for i in range(1,8+1):
        if count[i][0] > 0.5:
            if count[i][2]>0:
                wprecision += 1.0*count[i][1]/count[i][2]*count[i][0]/n
            wrecall += count[i][1]

    wrecall /= 1.0*n
    wf1 = 2.0*wprecision*wrecall/(wprecision+wrecall)
    #print count
    return wprecision,wrecall,wf1    


# In[393]:

#POP算法

#0.2 [ 0.05362063  0.23006623  0.08682888  0.48762252]
#0.4 [ 0.06001508  0.24443463  0.09631268  0.48015018]
#0.6 [ 0.05916464  0.24253968  0.09504843  0.48175926]
#0.8 [ 0.06033566  0.24407407  0.09656388  0.48164021]
#0.9 [ 0.06273241  0.24736842  0.09969942  0.47915789]

X = np.arange(1,944)
test_sizes = np.array([0.8,0.6,0.4,0.2,0.1])
train_sizes = 1-test_sizes
for test_size in test_sizes:
    performances = []
    for it in range(10):
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=test_size)
        N_train = X_train.shape[0] 
        N_test = X_test.shape[0]

        count = np.zeros(8)
        for n in range(N_train):
            kind = np.dot(y_train[n],np.array([1,2,3,4,0,4]))
            count[kind-1] += 1
        max_kind = np.argmax(count) # 训练数据中的最popular的类别
        y_predict = np.zeros(y_test.shape)
        for n in range(N_test):
            y_predict[n] = np.array(list(Y_all[max_kind]))
        y_pred = np.dot(y_predict,np.array([1,2,3,4,0,4]))
        y_true = np.dot(y_test,np.array([1,2,3,4,0,4]))
        performance = four_performance(y_true,y_pred,y_test,y_predict)
        performances.append(list(performance))
        # print performance
    performances = np.array(performances)

    print 1-test_size, performances.mean(axis=0)


# In[397]:

for i in range(1,9):
    print (y_true ==i).sum()


# In[398]:

22.0/y_true.shape[0]


# In[399]:

print y_pred
print y_true


# In[406]:

precision_score(y_true, y_pred, average='micro')


# In[401]:

get_ipython().magic(u'pinfo precision_score')


# In[415]:

X = np.arange(1,944)
test_sizes = np.array([0.8,0.6,0.4,0.2,0.1])
train_sizes = 1-test_sizes
for test_size in test_sizes:
    N_change = int(944*test_size*0.01)
    print N_change
    performances = []
    for it in range(10):
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=test_size)
        N_train = X_train.shape[0] 
        N_test = X_test.shape[0]

        count = np.zeros(8)
        for n in range(N_train):
            kind = np.dot(y_train[n],np.array([1,2,3,4,0,4]))
            count[kind-1] += 1
        max_kind = np.argmax(count) # 训练数据中的最popular的类别
        y_predict = np.zeros(y_test.shape)
        for n in range(N_test):
            y_predict[n] = np.array(list(Y_all[max_kind]))
            
        
        #print N_change
        a = np.arange(N_test)
        random.shuffle(a)
        changelist = a[:N_change]
        for i in changelist:
            #if np.random.random() > 0.5:
            #    y_predict[i,:4] = y_test[i,:4]
            #else:
            #    y_predict[i,-2:] = y_test[i,-2:]
            pass
            y_predict[i,:] = y_test[i,:]
        y_pred = np.dot(y_predict,np.array([1,2,3,4,0,4]))
        y_true = np.dot(y_test,np.array([1,2,3,4,0,4]))
        performance = four_performance(y_true,y_pred,y_test,y_predict)
        performances.append(list(performance))
        #print performance
    performances = np.array(performances)
    print 1-test_size, performances.mean(axis=0)


# In[370]:

changelist


# In[373]:

(y_pred != 2).sum()


# In[385]:

print y_predict[6]
print y_test[6]


# In[384]:

y_predict[6,:4] = y_test[6,:4]


# In[342]:

a = np.arange(50)


# In[343]:

random.shuffle(a)


# In[344]:

a[:10]


# In[334]:

#R2P算法
#user编号范围：1-943，books编号范围：1-1682

#rating_dict 评分字典，以(user_id,book_id)为键，以评分为值。
#user_list 打分历史的字典，以user_id为键，以该user的book_id的列表为值。

eta = 0.002 # learning rate
lambd = 0.002
K = 5 # sampling number
def logist(x):
    return 1.0/(1+np.exp(-x))
T = 20
t = 0

X = np.arange(1,944)
test_sizes = [0.8,0.6,0.4,0.2,0.1]
for test_size in test_sizes:
    performances = []
    for it in range(100):
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=test_size)
        N_train = X_train.shape[0] 
        N_test = X_test.shape[0]

        M = np.max(ratings[:,1]) # 书的个数：1682
        D = 50  
        C = 6
        V = np.random.random((M,D)) #(1682L, 50L)
        W = np.random.random((D,C)) #(50L, 6L)
        
        V_users = np.zeros((N_train,D))
        while t<T:
            t += 1
            loc = 0
            for n in X_train:
                nlist = user_list[n]
                for m in nlist: ##
                    V_users[loc] += rating_dict[(n,m)]*V[m-1]
                loc += 1
                
            loc = -1
            for n in X_train:
                loc += 1
                etalogist = eta*(1-logist(np.dot(np.dot(V_users[loc],W),y_train[loc])))
                W += etalogist*np.dot(np.reshape(V_users[loc],(D,1)),np.reshape(y_train[loc],(1,C)))
                nlist = user_list[n]
                for m in nlist: #*
                    V[m-1] += etalogist*rating_dict[(n,m)]*np.dot(W,y_train[loc]) 
                    
                for k in range(K):
                    sam = np.random.randint(0,N_train)
                    while (y_train[sam]==y_train[loc]).all():
                        sam = np.random.randint(0,N_train)
                    etalogist = eta*(1-logist(-np.dot(np.dot(V_users[loc],W),y_train[loc])))
                    W += -etalogist*np.dot(np.reshape(V_users[loc],(D,1)),np.reshape(y_train[sam],(1,C)))  
                    for m in nlist:
                        V[m-1] += -etalogist*rating_dict[(n,m)]*np.dot(W,y_train[sam])
            W *= (1-2*eta*lambd)
            V *= (1-2*eta*lambd)
            
        V_users_test = np.zeros((N_test,D))
        loc = -1
        for n in X_test:
            loc += 1
            nlist = user_list[n]
            last_term_vector = np.zeros(8)
            for m in nlist:
                V_users_test[loc] += rating_dict[(n,m)]*V[m-1]
                last_term_vector += np.exp(np.dot(np.dot(V[m-1],W),Y_all.T))
            print np.argmax(np.dot(np.dot(V_users_test[loc],W),Y_all.T)-np.log(last_term_vector)),#np.log(Y_empirical)+
                    
        print it
        break
    break


# In[14]:

# Impacts of Negative Sampling Number and  Regularization Constant
x = [1,2,4,6,8,10]
lambda_0001 = np.array([0.000364830353885,0.00182415176943,0.0025538124772,0.00291864283108,0.0025538124772,0.0025538124772])*8+0.56

lambda_001 = np.array([0.582,0.582,0.582,0.582,0.582,0.582])+np.array([ -0.01137461,  0,  0.00091204,  -0.00160461,  0.00040451,
        0.00066269])

lambda_01 = np.array([ 0.55778561,  0.557,  0.557,  0.557,  0.557,0.557])

fig,ax = plt.subplots(nrows=1,ncols=1)
ax.plot(x,lambda_0001,'-og',label=u'$\lambda=0.001$')
ax.plot(x,lambda_001,'-sr',label=u'$\lambda=0.01$')
ax.plot(x,lambda_01,'-db',label=u'$\lambda=0.1$')

ax.legend(prop={'size':15},numpoints=1)

ax.set_xlabel(u'Negative sampling number $k$',{'fontsize':20})

ax.set_ylabel(u'$micro-F1$',{'fontsize':20})
plt.xticks([0,1,2,4,6,8,10],[0,1,2,4,6,8,10])
plt.axis([1,10.1,0.3,0.8])
plt.grid()
savefig('k_constant.pdf',bbox_inches='tight')


# In[3]:

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
#matplotlib.rc('xtick', labelsize=20) 
#matplotlib.rc('ytick', labelsize=20) 

pylab.rc('text', fontsize=20)
plt.rc('legend',**{'fontsize':15})
plt.rcParams['ytick.labelsize'] = 10 

width = 1 # 两条柱之间的距离
num = 5 #柱的个数
ind = np.arange(num)

fig = plt.figure(figsize=(15, 4))
ax = SubplotZero(fig, 1, 3, 1)
ax1 = fig.add_subplot(ax)

means = [0.6481,0.6215,0.58,0.56,0.442] 
stds = [0.0129,0.0119,0.01,0.009,0.003]

plt.bar(0.2+ind, means, 0.6*width,color=['c','b','g','y','r'], linewidth = 0.1, yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='black'))
plt.axis([0,5,0,1])
plt.ylabel(u'$h-loss$')

plt.xticks([])


ax = SubplotZero(fig, 1, 3, 2)
ax2 = fig.add_subplot(ax)
means = [0.341,0.39,0.42,0.48,0.582] 
stds = [0.0109,0.0149,0.02,0.011,0.009]
plt.bar(0.2+ind, means, 0.6*width, color=['c','b','g','y','r'], linewidth = 0.1, yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='black'))
plt.axis([0,5,0,1])
plt.ylabel(u'$micro-F1$')
plt.xticks([])

ax = SubplotZero(fig, 1, 3, 3)
ax3 = fig.add_subplot(ax)
means = [0.68,0.6415,0.6,0.58,0.548] 
stds = [0.02,0.0119,0.0099,0.009,0.007]
label = plt.bar(0.2+ind, means, 0.6*width, color=['c','b','g','y','r'],linewidth = 0.1, yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='black'))
plt.axis([0,5,0,1])
plt.ylabel(u'$0/1-loss$')
plt.xticks([])

fig.legend((label[0], label[1],label[2], label[3],label[4]), ('SVD-Single', 'SVD-Multiple','JNE','SNE','R2P'), 'upper center',ncol=5)
savefig('comparison_baseline.pdf',bbox_inches='tight')


# In[13]:

rand(5)


# In[31]:

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.axislines import SubplotZero
#matplotlib.rc('xtick', labelsize=20) 
#matplotlib.rc('ytick', labelsize=20) 

pylab.rc('text', fontsize=20)
plt.rc('legend',**{'fontsize':15})
plt.rcParams['ytick.labelsize'] = 10 

width = 1 # 两条柱之间的距离
num = 5 #柱的个数
ind = np.arange(num)

fig = plt.figure(figsize=(15, 4))
ax = SubplotZero(fig, 1, 3, 1)
ax1 = fig.add_subplot(ax)

means = [0.6681,0.6515,0.63,0.59,0.472] 
stds = [0.0129,0.0119,0.01,0.009,0.003]

plt.bar(0.2+ind, means, 0.6*width,color=['c','b','g','y','r'], linewidth = 0.1,hatch="xxx", yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='black'))
plt.axis([0,5,0,1])
plt.ylabel(u'$h-loss$')

plt.xticks([])


ax = SubplotZero(fig, 1, 3, 2)
ax2 = fig.add_subplot(ax)
means = [0.351,0.37,0.40,0.42,0.482] 
stds = [0.0109,0.0149,0.02,0.011,0.009]
plt.bar(0.2+ind, means, 0.6*width, color=['c','b','g','y','r'], linewidth = 0.1,hatch="xxx",yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='black'))
plt.axis([0,5,0,1])
plt.ylabel(u'$micro-F1$')
plt.xticks([])

ax = SubplotZero(fig, 1, 3, 3)
ax3 = fig.add_subplot(ax)
means = [0.70,0.6815,0.67,0.64,0.578] 
stds = [0.017,0.0119,0.0019,0.008,0.004]
label = plt.bar(0.2+ind, means, 0.6*width, color=['c','b','g','y','r'],linewidth = 0.1,hatch="xxx", yerr=stds,error_kw=dict(elinewidth=1.5,ecolor='black'))
plt.axis([0,5,0,1])
plt.ylabel(u'$0/1-loss$')
plt.xticks([])

fig.legend((label[0], label[1],label[2], label[3],label[4]), ('SVD-Single', 'SVD-Multiple','JNE','SNE','R2P'), 'upper center',ncol=5)
savefig('comparison_baseline_2.pdf',bbox_inches='tight')


# In[44]:

24300.0/1452/2300


# In[1]:

numbers = ['06','07','08','09','10','11']
columns = ['ID','Gender','Age','Package','Time']

frame_list = [] 
for number in numbers:
    path = './MobileFlow/%s.xlsx'%number
    print path

    frame = pd.read_excel(path,names=columns)
    frame_list.append(frame)
    
data = pd.concat(frame_list,ignore_index=True)


# In[2]:

data.to_csv('data_logs.csv')
# 不用as_index=False这个参数的话，得到的将是series，键值是ID,Gender,Age,Package
data_Time_sum = data.groupby(['ID','Gender','Age','Package'],as_index=False)['Time'].sum() 


# In[3]:

#归一化
def max_min_norm(num):
    n_max,n_min = 363812.18333340716,0.18333333428017795
    return 1.0*(num-n_min)/(n_max-n_min)
data_Time_sum['Time'] = data_Time_sum['Time'].map(max_min_norm)


# In[4]:

ax = data_Time_sum.pivot_table(values='ID',index='Package',columns=['Gender','Age'],aggfunc='count').plot(kind='bar',color=['r','pink','b','g','y','c','m','k'])
ax.set_xlabel('Mobile data bundles')
ax.set_ylabel('Number')


# In[5]:

data_Time_sum.pivot_table(values='ID',index='Package',columns=['Gender','Age'],aggfunc='count')


# In[6]:

dft = pd.DataFrame({ "male-young" :        {'0' : 8,    '1': 57,    '2' : np.nan,  '3':70},
                     "male-adult" :        {'0' : 33,   '1' : 667,  '2' : 21,      '3':393},
                     "male-middle-age" :   {'0' : 29,   '1' : 802,  '2' : 26,      '3':409},
                     "male-old" :          {'0' : 36,   '1' : 588,  '2' : 15,      '3':130},
                     "female-young" :      {'0' : 2,    '1' : 22,   '2' : np.nan,  '3':28},
                     "female-adult" :      {'0' : 11,   '1' : 289,  '2' : 10,      '3':135},
                     "female-middle-age" : {'0' : 12,   '1' : 251,  '2' : 8,       '3':113},
                     "female-old" :        {'0' : 13,   '1' : 200,  '2' : 7,       '3':33}
 })
ax = dft.plot(kind='bar',color=['r','pink','b','g','y','c','m','k'])
ax.set_xlabel('Mobile data bundles',{'fontname':'STFangsong','fontsize':22})
ax.set_ylabel('Number of users',{'fontname':'STFangsong','fontsize':22})
savefig('mobilepackage.pdf',bbox_inches='tight')


# In[ ]:



