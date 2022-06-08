# CVRP_using_PULP_Algorithm

Multi-Objective Optimisation (MOO) for Vehicle Routing Problem(VRP), that is Capacitated Vehicle Routing Problem, is tried here for solution and optimisation using PULP package in python using LpMinimize for "CVRP" model.


# Problem Statement
In this challenge you will design an algorithm for the VRP. Delivery companies every day
need to deliver packages to many different clients. The deliveries are accomplished using an
available fleet of vehicles from a central warehouse. The goal of this exercise is to design a
route for each vehicle so that all customers are served, and the number of vehicles
(objective 1) along with the total traveled distance (objective 2) by all the vehicles are
minimized. In addition, the capacity of each vehicle should not be exceeded (constraint 1).

# Approach
The primary approach for using PULP package is the ease of coding optimisation problem with it. Considering the scenario in the Company environment the fast and efficient outputs are the priority.

# Installations
1) Python (Packages used PULP, PANDAS, NUMPY, MATPLOTLIB)
2) Pip
3) Virtual Environment

# Assumptions
1) Due date, service time, ready time are ignored from the dataset as stated in the problem statement
2) There is no cost of extra vehicle. Hence taken = 0.
3) There is no time delay and no time windows for our vehicle at the objective locations
4) Distance between client to client is calculated by Euclidean, as per the task.
5) Vehicle always starts from the depot customer_0 and delivers goods and then comes back to depot again after delivery.

# 1) Parsing Input

The initial data file "vrpdata.txt" which taken out to be in text format is used in the code.

# 2) Running PULP model for optimising the problem and getting the visualisation results alongwith

Run the algorithm activating the virtual environment and run this command (With clients less than 15, number of vehicles can be given in any number, the model returns the minimum vehicle required for the optimised route.

```bash
python pulp.py
```

# Problems with the PULP optimisation
The code is not efficient for multi objective optimisation if the number of clients served are more than 15, the model gave satisafactory results best best optimised routes and number of vehicles used only if the number of clients are less than 15. 

# Current Model Results - Visualisation

Even though the code is proper and working the optimisation for 25 clients as per the challenge using PULP model would take alot of time (which is not even feasible). But as the challenge was to optimise the route and vehicle, the algorithm effectively achieves that (even if results are avaible for less than 15 clients). The results as are as below:

## Model was input with number of clients = 14 and number of vehicles = 5

The model results are satisfactory for the above requirements and the processing time was 440 seconds.
![PULP_VRP_Results](https://user-images.githubusercontent.com/55597813/172597603-a32db11a-9db6-466d-b976-efa775932356.png)

# Solution to Complete the Task

As  I have not achieved the challenge of optimising the route anf number of vehicles for 25 Clients, I have decided to upgrade to MOO DEAP package for the task. DEAP is a complete and efficient Multi objective optimisation package. 
The algorithm and results for the complete challenge using the DEAP package can be found at:

```bash
[python rulp.py](https://github.com/xenvik/Capacitated_Vehicle_Routing_Problem_DEAP)
```
