import numpy as np
import pandas as pd
import pulp
import itertools
from matplotlib import pyplot as plt


# customer count ('0' is depot) 
customer_count = 14

# the number of vehicle
vehicle_count = 5

# the capacity of vehicle
vehicle_capacity = 70

# fix random seed
np.random.seed(seed=999)


"""
READING FILE
"""
df = pd.read_csv(r'vrpdata.txt', sep = " ")
df = df.iloc[0:customer_count+1]

Y, X = list(df["Y"]), list(df["X"])
coordinates = np.column_stack((X, Y))

Demand = list(df["Demand"])
n = len(coordinates)
depot, customers = coordinates[0, :], coordinates[1:, :]
M = 100**100 #Random Large Number

## Calculating distance between two clients
"""
Parameters: Dataframe
Returns: Distance Results
"""
def _distance_calculator(_df):
    
    _distance_result = np.zeros((len(_df),len(_df)))
    _df['X-Y'] = '0'

    for i in range(len(_df)):
        for j in range(len(_df)):
            
            # calculate distance of all pairs
            '''variable_1: X[i,j] =(0,1), i,j = Nodes'''
            #x[i, j] = m.addVar(vtype=GRB.BINARY, name="x%d,%d" % (i, j))
            _distance_result[i, j] = np.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
            if i == j:
                _distance_result[i, j] = M  ## big 'M'
            continue
    return _distance_result

distance = _distance_calculator(df)


## Running PULP algorithm for results
for vehicle_count in range(1,vehicle_count+1):
    
    # definition of LpProblem instance
    problem = pulp.LpProblem("CVRP", pulp.LpMinimize)

    # definition of variables which are 0/1
    x = [[[pulp.LpVariable("x%s_%s,%s"%(i,j,k), cat="Binary") if i != j else None for k in range(vehicle_count)]for j in range(customer_count)] for i in range(customer_count)]

    # add objective function
    problem += pulp.lpSum(distance[i][j] * x[i][j][k] if i != j else 0
                          for k in range(vehicle_count) 
                          for j in range(customer_count) 
                          for i in range (customer_count))

    # constraints
    # forluma (2)
    for j in range(1, customer_count):
        problem += pulp.lpSum(x[i][j][k] if i != j else 0 
                              for i in range(customer_count) 
                              for k in range(vehicle_count)) == 1 

    # forluma (3)
    for k in range(vehicle_count):
        problem += pulp.lpSum(x[0][j][k] for j in range(1,customer_count)) == 1
        problem += pulp.lpSum(x[i][0][k] for i in range(1,customer_count)) == 1

    # forluma (4)
    for k in range(vehicle_count):
        for j in range(customer_count):
            problem += pulp.lpSum(x[i][j][k] if i != j else 0 
                                  for i in range(customer_count)) -  pulp.lpSum(x[j][i][k] for i in range(customer_count)) == 0

    #forluma (5)
    for k in range(vehicle_count):
        problem += pulp.lpSum(df.Demand[j] * x[i][j][k] if i != j else 0 for i in range(customer_count) for j in range (1,customer_count)) <= vehicle_capacity


    #formula (6)
    subtours = []
    for i in range(2,customer_count):
         subtours += itertools.combinations(range(1,customer_count), i)

    for s in subtours:
        problem += pulp.lpSum(x[i][j][k] if i !=j else 0 for i, j in itertools.permutations(s,2) for k in range(vehicle_count)) <= len(s) - 1

    
    # print vehicle_count which needed for solving problem
    # print calculated minimum distance value
    if problem.solve() == 1:
        print('Vehicle Requirements:', vehicle_count)
        print('Moving Distance:', pulp.value(problem.objective))
        break


## Visualization of Results
plt.figure(figsize=(8,8))
for i in range(customer_count):    
    if i == 0:
        plt.scatter(df.X[i], df.Y[i], c='green', s=200)
        plt.text(df.X[i], df.Y[i], "depot", fontsize=12)
    else:
        plt.scatter(df.X[i], df.Y[i], c='orange', s=200)
        plt.text(df.X[i], df.Y[i], str(df.CUST[i]), fontsize=12)

for k in range(vehicle_count):
    for i in range(customer_count):
        for j in range(customer_count):
            if i != j and pulp.value(x[i][j][k]) == 1:
                plt.plot([df.X[i], df.X[j]], [df.Y[i], df.Y[j]], c="black")

plt.show()
