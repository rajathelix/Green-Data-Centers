import numpy as np
import matplotlib.pyplot as plt
import csv
# Reads data
def read_data():
    x=[]
    y=[]
    z=[]
    with open('data.csv') as csvfile:
        readCSV=csv.reader(csvfile,delimiter=',')
        for row in readCSV:
            x.append(float(row[0]))
            y.append(float(row[1]))
            z.append(float(row[2]))
    return [x,y,z]

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y**2)
    SS_xx = np.sum(x*x - n*m_x**2)
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return(b_0, b_1)
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
    plt.plot(x,y_pred,color='g')
    # putting labels
    plt.xlabel('Time (Seconds)')
    plt.ylabel('Temperature (Celsius)')
 
    # function to show plot
    plt.show()
def plot_histogram(x, y, b):
    plt.bar(x,y)
    #for i in range(len(y)):
        #plt.hlines(y[i],0,x[i])
    plt.ylabel('Temperature (Celsius)')
    plt.xlabel('Time (Seconds)')
    plt.show()
def main():
    d=read_data()
    x=np.array(d[0])
    y=np.array(d[1])
    # estimating coefficients
    b = estimate_coef(x, y)
    #print("Estimated coefficients:\nb_0 = {}  \
          #\nb_1 = {}".format(b[0], b[1]))
    # plotting regression line
    plot_histogram(x, y, b)
    plot_regression_line(x,y,b)
    predict(x,y)
def predict(x,y):
    time=int(input("Probable temperature at time= "))
    x1 = np.array(x)
    y1 = np.array(y)
    b=estimate_coef(x1, y1)
    y_pred = b[0] + b[1]*time
    if(y_pred>=27.0):
        print("Temperature will be above thresdold value.")
        print("Extensive cooling will be initialized.")
    else:
        print("Temperature will be normal.")
    print("Expected temperature (Celsius) is: ",y_pred)

if __name__ =="__main__":
    main()
