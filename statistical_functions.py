from math import *

#mesos oros
def mean_avg(X):
    n=len(X)
    sum=0
    for i in range(n):
        sum=sum+X[i]
    return float(sum)/n

#diakumansi
def variance(X):
    n=len(X)
    sum=0
    avg=mean_avg(X)
    for i in range(n):
        sum=sum+(X[i]-avg)**2

    return float(sum)/n

#tupiki apoklisi
def divergence(X):
    return sqrt(variance(X))

#sunithestero stoixeio se lista
def most_common(lst):
    return max(set(lst), key=lst.count)

#diamesos
#python is zero based, so for median calculation we check (n/2 -1)th and (n/2)th elements for even crowd, and (n/2 -1)th element for odd crowd
def median(X):
    X.sort()
    n=len(X)
    if len(X) % 2 ==1:
        elem=floor(float(n)/2)
        return X[int(elem)]
    else:
        elem1=n/2 -1
        elem2=(n/2)
        return float((X[elem1]+X[elem2]))/2

#suntelestis asummetrias
def asymmetry_coefficient(X):
    avg=mean_avg(X)
    s=divergence(X)
    delta=median(X)
    return 3*(avg-delta)/(s)

#suntelestis kurtotitas
def curvature_coefficient(X):
    s=divergence(X)
    n=len(X)
    sum=0
    avg=mean_avg(X)
    for i in range(n):
        sum=sum+(X[i]-avg)**4
    return sum/( (s**4)*n )




#Example
X8=[200,240,250,215,199,201,171,176,215,220,
   210,190,255,179,178,233,200,182,210,225,
   180,170,195,173,187,185,241,192,205,232,
   170,175,190,183,238,187,189,202,200,240,
   205,185,188,203,247,177,178,213,188,250,
   250,205,256,206,219,249,184,222,197,185,
   250,260,285,214,221,259,195,232,205,180,
   170,160,211,254,225,231,185,242,193,170,
   175,165,188,236,207,233,199,252,173,175,
   235,230,198,199,211,184,201,260,263,195]


print 'crowd: ', len(X8)
print 'average: ', mean_avg(X8)
print 'Variance: ',variance(X8)
print 'Divergence: ', divergence(X8)
print 'Median: ', median(X8)
print 'Asymmetry Coefficient: ',asymmetry_coefficient(X8)
print 'Curvature Coefficient: ',curvature_coefficient(X8)

