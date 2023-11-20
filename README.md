# Travelling-Thief-Problem

DO NOT LEAVE IN FINAL REPO

The traveling thief problem combines the Traveling Salesman Problem (TSP) and the Knapsack Problem (KNP). Both problems will be explained in the following sections.

Traveling Salesman Problem (TSP)
In the TSP a salesman has to visit 𝑛
 cities. The distances are given by a map represented as a distance matrix 𝐴=(𝑑𝑖𝑗)
 with 𝑖,𝑗∈{0,..,𝑛}
. The salesman has to visit each city once and the result is a permutation vector 𝜋=(𝜋1,𝜋2,...,𝜋𝑛)
 , where 𝜋𝑖
 is the i-th city of the salesman. The distance between two cities divided by a constant velocity 𝑣
 results in the traveling time for the salesman denoted by 𝑓(𝜋)
. The goal is to minimize the total traveling time of the tour:

𝑚𝑖𝑛𝑠.𝑡.𝑓(𝜋)=𝑓(𝜋)𝜋=(𝜋1,𝜋2,...,𝜋𝑛)∈𝑃𝑛𝜋1=1∑𝑖=1𝑛−1𝑑𝜋𝑖,𝜋𝑖+1𝑣+𝑑𝜋𝑛,𝜋1𝑣
There are (𝑛−1)!2
 different tours to consider, if we assume that the salesman has to start from the first city and travels on a symmetric map where 𝑑𝑖,𝑗=𝑑𝑗,𝑖
.

Knapsack Problem (KNP)
For the Knapsack Problem a knapsack has to be filled with items without violating the maximum weight constraint. Each item 𝑗
 has a value 𝑏𝑗≥0
 and a weight 𝑤𝑗≥0
 where 𝑗∈{1,..,𝑚}
. The binary decision vector 𝑧=(𝑧1,..,𝑧𝑚)
 defines, if an item is picked or not. The search space of this problem contains 2^n combinations and the goal is to maximize the profit 𝑔(𝑧)
:

𝑚𝑎𝑥s.t.𝑔(𝑧)=𝑔(𝑧)∑𝑗=1𝑚𝑧𝑗𝑤𝑗≤𝑄𝑧=(𝑧1,..,𝑧𝑚)∈𝔹𝑚∑𝑗=1𝑚𝑧𝑗𝑏𝑗
Traveling Thief Problem (TTP)
The TTP is a combinatorial optimization problem that consists of two interweaving problems, TSP and KNP. After explaining the two components separately, the interdependence and the different models of the problem are described.

The Traveling Thief Problem combines the above defined subproblems and lets them interact with each other. The traveling thief can collect items from each city he is visiting. The items are stored in a knapsack carried by him. In more detail, each city 𝜋𝑖
 provides one or multiple items, which could be picked by the thief. There is an interaction between the subproblems: The velocity of the traveling thief depends on the current knapsack weight 𝑤
, which is carried by him. It is calculated by considering all cities, which were visited so far, and summing up the weights of all picked items. The weight at city 𝑖
 given 𝜋
 and 𝑧
 is calculated by:

𝑤(𝑖,𝜋,𝑧)=∑𝑘=1𝑖∑𝑗=1𝑚𝑎𝑗(𝜋𝑘)𝑤𝑗𝑧𝑗
The function 𝑎𝑗(𝜋𝑘)
 is defined for each item 𝑗
 and returns 1
 if the item could be stolen at city 𝜋𝑘
 and 0
 otherwise. The current weight of the knapsack has an influence on the velocity. When the thief picks an item, the weight of the knapsack increases and therefore the velocity of the thief decreases.

The velocity 𝑣
 is always in a specific range 𝑣=[𝑣𝑚𝑖𝑛,𝑣𝑚𝑎𝑥]
 and could not be negative for a feasible solution. Whenever the knapsack is heavier than the maximum weight 𝑄
, the capacity constraint is violated. However, to provide also the traveling time for infeasible solutions the velocity is set to 𝑣𝑚𝑖𝑛
, if 𝑤>𝑄
:

𝑣(𝑤)={𝑣𝑚𝑎𝑥−𝑤𝑄⋅(𝑣𝑚𝑎𝑥−𝑣𝑚𝑖𝑛)𝑣𝑚𝑖𝑛if 𝑤≤𝑄otherwise
If the knapsack is empty the velocity is equal to 𝑣𝑚𝑎𝑥
. Contrarily, if the current knapsack weight is equal to 𝑄
 the velocity is 𝑣𝑚𝑖𝑛
.

Furthermore, the traveling time of the thief is calculated by:

𝑓(𝜋,𝑧)=∑𝑖=1𝑛−1𝑑𝜋𝑖,𝜋𝑖+1𝑣(𝑤(𝑖,𝜋,𝑧))+𝑑𝜋𝑛,𝜋1𝑣(𝑤(𝑛,𝜋,𝑧))
The calculation is based on TSP, but the velocity is defined by a function instead of a constant value. This function takes the current weight, which depends on the index 𝑖
 of the tour. The current weight, and therefore also the velocity, will change on the tour by considering the picked items defined by 𝑧
. In order to calculate the total tour time, the velocity at each city needs to be known. For calculating the velocity at each city the current weight of the knapsack must be given. Since both calculations are based on 𝑧
 and 𝑧
 is part of the knapsack subproblem, it is very challenging to solve the problem to optimality. In fact, such problems are called interwoven systems as the solution of one subproblem highly depends on the solution of the other subproblems.

Here, we leave the profit unchanged to be calculated as in the KNP problem. Finally, the TTP problem is defined by

𝑚𝑖𝑛𝑚𝑎𝑥𝑓(𝜋,𝑧)𝑔(𝑧)𝑠.𝑡.==𝑓(𝜋,𝑧)𝑔(𝑧)∑𝑖=1𝑛−1𝑑𝜋𝑖,𝜋𝑖+1𝑣(𝑤(𝑖,𝜋,𝑧))+𝑑𝜋𝑛,𝜋1𝑣(𝑤(𝑛,𝜋,𝑧))∑𝑗=1𝑚𝑧𝑗𝑏𝑗𝜋=(𝜋1,𝜋2,...,𝜋𝑛)∈𝑃𝑛𝜋1=1𝑧=(𝑧1,..,𝑧𝑚)∈𝔹𝑚∑𝑗=1𝑚𝑧𝑗𝑤𝑗≤𝑄
In order to illustrate the equations and interdependence, an example scenario is presented in the following. The thief starts at city 1 and has to visit city 2, 3, 4 exactly once and to return to city 1. In this example, each city provides one item and the thief must decide to steal item or not.

Problem Specification copied from https://www.egr.msu.edu/coinlab/blankjul/gecco19-thief/#traveling-thief-problem-ttp