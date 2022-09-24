import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

#fixPoint approach
def weeklyRisk2(p0, a0, a3):
    b2 = (a0 - a3)/3
    a1 = a0 - b2 
    a2 = a0 - 2*b2
    a3 = a0 - 3*b2
    a4 = a0 - 3*b2 + ((1+3*b2-a0)/11)
    a5 = a0 - 3*b2 + ((1+3*b2-a0)/11)*2
    mon = pow(p0, 5)*a1*90/121 + pow(p0,4)*a1*(-479/121) + pow(p0,3)*a1*(1018/121) + pow(p0,2)*a1*(-1080/121) +p0*a1*(572/121)
    tue = pow(p0, 5)*a2*90/121 + pow(p0,4)*a2*(-479/121) + pow(p0,3)*a2*(1018/121) + pow(p0,2)*a2*(-1080/121) +p0*a2*(451/121) + p0
    wed = pow(p0, 5)*a3*90/121 + pow(p0,4)*a3*(-479/121) + pow(p0,3)*a3*(1018/121) + pow(p0,2)*a3*(-959/121) +p0*a3*(330/121) - pow(p0, 2) + 2*p0
    thu = pow(p0, 5)*a4*90/121 + pow(p0,4)*a4*(-479/121) + pow(p0,3)*a4*(897/121) + pow(p0,2)*a4*(-717/121) +p0*a4*(19/11) +pow(p0, 3) - 3*pow(p0, 2) + 3*p0
    fri = pow(p0, 5)*a5*90/121 + pow(p0,4)*a5*(-369/121) + pow(p0,3)*a5*(567/121) + pow(p0,2)*a5*(-387/121) +p0*a5*(9/11) -pow(p0, 4)*(10/11) +pow(p0, 3)*(41/11) - pow(p0, 2)*(63/11) + p0*(43/11)
    weekList = [mon, tue, wed, thu, fri]
    minRisk = 1
    index = 0
    minIndex = -1
    for item in weekList:
        if item < minRisk:
            minRisk = item
            minIndex = index
        index += 1
    return minRisk, minIndex

def flexiblePoints2():
    data = []
    for a3 in range(1, 100):
        for a0 in range(a3, 100):
            for p in range(1, 25):
                _, day = weeklyRisk2(p*0.02, a0* 0.01, a3* 0.01)
                row = [a0*0.01, a3*0.01, p*0.02, day]
                data.append(row)
    return data
data2 = flexiblePoints2()
df2 = pd.DataFrame(data2)
df2.columns = ['a3', 'a0','p', 'best']
fig = px.scatter_3d(df2, x='a3', y='a0', z='p', color='best')
fig.show()

