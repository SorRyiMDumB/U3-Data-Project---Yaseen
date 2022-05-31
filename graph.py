#bruh

### IMPORTS
# Database
import sqlite_Funcs
from tkinter import E

from numpy import append


# Graphing
import networkx as nx
import matplotlib.pyplot as plt

# System
import os

exceptionlist = []


global G

connection = sqlite_Funcs.create_connection("data.sqlite")

def addnodes():
    ''' adds all the nodes from the database'''
    select_users = "SELECT * from users"
    allusers = sqlite_Funcs.execute_read_query(connection, select_users)
    for i in allusers:
        G.add_node(
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
def hubber(param : str):
    """ Connects nodes that share the same parameter to one node that is the prameter

    Args:
        param (str): Parameter to be checked 
    """

    global exceptionlist

    # List of unique values in the parameter 
    uniqueVal = []

    # for every node in the graph 
    for node in G:
        if node in exceptionlist:
            print("Node: ", node, " is in the exception list ", exceptionlist)
        else:
            nodedata = G.nodes[node][param]
        
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
    print("#####################\nThe unique values in parameter: ",param, " are ", uniqueVal)



    for uniquevalue in uniqueVal:
        nodename = "Atribute: " + str(uniquevalue)
        G.add_node(str(nodename))
        exceptionlist.append(nodename)
        pass

    print("TEST exception list",exceptionlist)
    for Node in G:

        if Node in exceptionlist:
            print("Node: ", Node, " is in the exception list ", exceptionlist)

        else:
            data = G.nodes[Node][param]
            for uniquevalue in uniqueVal:

                if data == uniquevalue:
                    chese  = "Atribute: " + str(uniquevalue)
                    G.add_edge(Node, chese)

def classes_edge(given_colour):

    global exceptionlist

    for node in G:
        print("OG NODE: ", node)

        if node in exceptionlist:
            print(node, "execption")
            pass
        else:
            raw = G.nodes[node]["classes"]
            worklist = raw.split("~")

            print(node, "OG NODE DATA",worklist)
            
        for testnode in G:
            if testnode in exceptionlist:
                pass
            else:
                print(testnode)
                if node == testnode:
                    print("nodes are the same")
                else:
                    testraw = G.nodes[testnode]["classes"]
                    print(testraw)
                    testworklist = testraw.split("~")
                    a = set(testworklist).intersection(worklist)
                    print(a)
                    if len(a) == 0:
                        pass
                    else:
                        G.add_edge(node,testnode,colour= given_colour,weight= len(a))


def defultgraph():
    hubber("year")
    hubber("house")
    hubber("genshin")
    hubber("uni")
    hubber("course")
    hubber("f1")
    hubber("sport")
    #hubber("tutorMath") broken
    #hubber("tutorEng") broken
    #hubber("tutorHums") broken
    #hubber("tutorScience") broken
    hubber("friends")


    classes_edge('black')

    print(G)

    nx.draw(G, with_labels = True)
    plt.show()