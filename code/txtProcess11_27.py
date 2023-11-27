import re
import pandas as pd
import numpy as np

def process_txt(file_path):
    filename = file_path
    with open(filename,'r',encoding='UTF-8') as f:
        contents=f.readlines()
        f.close()

    cityIndex = contents.index('NODE_COORD_SECTION\t(INDEX, X, Y): \n')
    itemIndex = contents.index('ITEMS SECTION\t(INDEX, PROFIT, WEIGHT, ASSIGNED NODE NUMBER): \n')
    contents[cityIndex] = re.sub(',|\(|\)|\:|NODE_COORD_SECTION','',contents[cityIndex])
    contents[itemIndex] = re.sub(',|\(|\)|\:|ITEMS SECTION|ASSIGNED|NUMBER','',contents[itemIndex])
    cityList = contents[cityIndex:itemIndex]
    itemList = contents[itemIndex:]

    f = open('city.txt','w')
    f.writelines(cityList)
    f.close
    f = open('item.txt','w')
    f.writelines(itemList)
    f.close

    info = contents[0:cityIndex]
    # infoList = []
    # for i in range(2,8):
    #     print(i)
    #     infoList.append(float(re.sub(r'[A-Z]|[a-z]|:', "", info[i])))
    # infoList = [DIMENSION,NUMBER_OF_ITEMS,CAPACITY_OF_KNAPSACK,MIN_SPEED,MAX_SPEED,RENTING_RATIO]
    DIMENSION = int(re.sub(r'\D', "", info[2]))
    NUMBER_OF_ITEMS = int(re.sub(r'\D', "", info[3]))
    CAPACITY_OF_KNAPSACK = int(re.sub(r'\D', "", info[4]))
    MIN_SPEED= float(re.sub(r'[A-Z]|[a-z]|:', "", info[5]))
    MAX_SPEED= float(re.sub(r'[A-Z]|[a-z]|:', "", info[6]))
    RENTING_RATIO= float(re.sub(r'[A-Z]|[a-z]|:', "", info[7]))
    return DIMENSION,NUMBER_OF_ITEMS,CAPACITY_OF_KNAPSACK,MIN_SPEED,MAX_SPEED,RENTING_RATIO

def make_distance_matrix(DIMENSION):
    city_count = DIMENSION
    node_info = pd.read_table('city.txt', delim_whitespace=True)
    distanceMatrix = np.zeros((city_count,city_count))
    for i in range(city_count):
        for j in range(city_count):
            x = np.power(node_info['X'][i]-node_info['X'][j],2)
            y = np.power(node_info['Y'][i]-node_info['Y'][j],2)
            distance = np.sqrt(x+y)
            distanceMatrix[i][j] = distance
    return distanceMatrix

def make_item_matrix(DIMENSION,NUMBER_OF_ITEMS):
    itemMatrix = np.zeros((DIMENSION,NUMBER_OF_ITEMS),dtype=int)
    print(itemMatrix.shape)
    item_info = pd.read_table('item.txt', delim_whitespace=True)
    item_node = item_info['NODE'].tolist()
    item_index = item_info['INDEX'].tolist()
    item_weight = item_info['WEIGHT'].to_numpy()
    item_value = item_info['PROFIT'].to_numpy()
    for i in range(NUMBER_OF_ITEMS):
        itemMatrix[item_node[i]-1][item_index[i]-1]=1
    return itemMatrix,item_value,item_weight

file_path = 'D:/workspace/EA-TTP/resources/a280-n1395.txt'
# parameters in txt file
DIMENSION,NUMBER_OF_ITEMS,CAPACITY_OF_KNAPSACK,MIN_SPEED,MAX_SPEED,RENTING_RATIO = process_txt(file_path)
print(NUMBER_OF_ITEMS)
# get distance_matrix
distance_matrix = make_distance_matrix(DIMENSION)
print(distance_matrix)
# get item_to_city_mapping,item_values,item_weights
item_to_city_mapping,item_values,item_weights = make_item_matrix(DIMENSION,NUMBER_OF_ITEMS)
print(item_to_city_mapping)
print(item_values)