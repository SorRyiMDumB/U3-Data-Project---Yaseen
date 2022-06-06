#bruh

### IMPORTS
# Database
import sqlite_Funcs

from numpy import append


# Graphing
import networkx as nx
import matplotlib.pyplot as plt

# System
import os
from tqdm import tqdm

exceptionlist = []


global G

connection = sqlite_Funcs.create_connection("data.sqlite")

def addnodes(GROPH):
    ''' adds all the nodes from the database'''
    select_users = "SELECT * from users"
    allusers = sqlite_Funcs.execute_read_query(connection, select_users)
    for i in allusers:
        GROPH.add_node(
        i[0], 
        year = i[1],                # shape /////
        house = i[2],               # edge, color, outline /////
        classes = i[3],             # edge 
        genshin = i[4],                 # edge, color, outline /////
        uni = i[5],                 # edge /////
        course = i[6],              # edge /////
        f1 = i[7],              # edge, shape outline /////
        sport = i[8],               # edge, color outline /////
        tutorMath = i[9],               # edge 
        tutorEng = i[10],               # edge 
        tutorHums = i[11],              # edge 
        tutorScience = i[12],               # edge 
        friends = i[13],                 # size
        
        colour = "white",
        weight = "1",
        shape = "o",
        outline = "black"
        )

### CONNECTOR
def hubber(GROPH,param : str):
    """ Connects nodes that share the same parameter to one node that is the prameter

    Args:
        param (str): Parameter to be checked 
    """

    global exceptionlist

    # List of unique values in the parameter 
    uniqueVal = []
    nodesthatsatify = []
    # for every node in the graph 
    #for node in tqdm(GROPH):
    #print(GROPH.nodes())
    for node in GROPH:
        if node in exceptionlist:
            pass
            #print("Node: ", node, " is in the exception list ", exceptionlist)
        else:
            nodesthatsatify.append(node)
            #print(nodesthatsatify)

            #print(node)
            #print(param)
            nodedata = GROPH.nodes[node][param]
            #print(nodedata)
        
        # if the data found is already in the unique value list, skip 
        if nodedata in uniqueVal:
            pass
        
        # if data is not in unique value list, add data point
        else:
            uniqueVal.append(nodedata)

    # removes case 0
    if "0" in uniqueVal:
        uniqueVal.remove("0")
    
    # prints out statement saying what the unique values are in the parameter after all nodes have been searched
    #print("#####################\nThe unique values in parameter: ",param, " are ", uniqueVal)

    nodecreated = []

    for uniquevalue in uniqueVal:
        #print(uniqueVal)
        #print(uniquevalue)
        nodename = "Atribute: " + str(uniquevalue)
        GROPH.add_node(str(nodename))
        exceptionlist.append(nodename)
        nodecreated.append(nodename)
        pass

    #print(nodecreated)

    for satnode in nodesthatsatify:
        #print(satnode)
        data = GROPH.nodes[satnode][param]
        #print(data)
        
        if str(data) == str(0):
            #print("data is 0")
            pass
        else:
            chese  = "Atribute: " + str(data)
            #print(satnode)
            #print(chese)
            #print(f"adding edge between {satnode} and {chese}")
            GROPH.add_edge(satnode, chese, weight=1)
        

"""
    #print("TEST exception list",exceptionlist)
    for Node in GROPH:

        if Node in exceptionlist:
            #print("Node: ", Node, " is in the exception list ", exceptionlist)
            pass

        else:
            data = GROPH.nodes[Node][param]
            for uniquevalue in uniqueVal:

                if data == uniquevalue:
                    chese  = "Atribute: " + str(uniquevalue)
                    GROPH.add_edge(Node, chese, weight=1)
"""


def classes_edge(GROPH,given_colour):

    global exceptionlist

    for node in GROPH:
        #print("OG NODE: ", node)

        if node in exceptionlist:
            #print(node, "execption")
            pass
        else:
            raw = GROPH.nodes[node]["classes"]
            worklist = raw.split("~")

            #print(node, "OG NODE DATA",worklist)
            
        for testnode in GROPH:
            
            if testnode in exceptionlist:
                #print(f"TEST: testnode {testnode} is in the exception")
                pass
            else:
                #print(f"TEST: testnode {testnode} is NOT in the exception")
                
                if node == testnode:
                    #print("nodes are the same")
                    pass
                
                else:
                    testraw = GROPH.nodes[testnode]["classes"]
                    #print(testraw)
                    testworklist = testraw.split("~")
                    a = set(testworklist).intersection(worklist)
                    #print(a)
                    if len(a) == 0:
                        pass
                    else:
                        if node in exceptionlist:
                            #print(f"TEST: NOT adding edge between {node} and {testnode}")
                            pass
                        else:
                            #print(f"TEST: adding edge between {node} and {testnode}")
                            GROPH.add_edge(node,testnode,colour= given_colour,weight= len(a))

def tutor(GROPH, param):
    global exceptionlist

    nodename = "Atribute: " + str(param)
    GROPH.add_node(str(nodename))
    exceptionlist.append(nodename)
    for node in GROPH:
        if node in exceptionlist:
            #print("Node: ", node, " is in the exception list ", exceptionlist)
            pass

        else:
            data = GROPH.nodes[node][param]
            #print(node,data,type(data))
            if data == str(1):
                #print("yes")
                GROPH.add_edge(node,str(nodename),weight= 1)
    pass


def defultgraph(GROPH):
    hubber(GROPH,"year")
    hubber(GROPH,"house")
    hubber(GROPH,"genshin")
    hubber(GROPH,"uni")
    hubber(GROPH,"course")
    hubber(GROPH,"f1")
    hubber(GROPH,"sport")
    tutor(GROPH,"tutorMath") 
    tutor(GROPH,"tutorEng") 
    tutor(GROPH,"tutorHums") 
    tutor(GROPH,"tutorScience") 
    hubber(GROPH,"friends")


    classes_edge(GROPH,'black')

    print(GROPH)

def drawgraph(GROPH):
    nx.draw(GROPH, with_labels = True)
    plt.show()

