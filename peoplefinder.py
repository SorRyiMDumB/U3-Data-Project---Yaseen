from cmath import inf
import graphing
import networkx as nx
from statistics import mode
 
from collections import Counter
G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

def influence(GROPH, aa):
    influence = {}                                                                      # Dictionary called influence is created

    for node in GROPH:                                                            # Iterates through all nodes in the graph
        if type(node) == int:                                                       # Checks if the node is a student ( the way that my graph is set up allows me to cheat
                                                                                              # by checking if the node is a interger as only students are labelled as 1, 2 ... intergers )
            
            deg = GROPH.degree(node)                                        # Finds the degree of the node
            fri = GROPH.nodes[node]["friends"]                          # Finds how many friends the respondant said they had
            year =  ( 1 / GROPH.nodes[node]["year"] ) * 100        # Finds what year level they are in and changes the value to better suit the calculation

            hobbyscore = 0                                                          # Creates a hobbyscore variable 

            hobbylist = ['genshin', 'f1', 'sport']                          # Creates a attributes list with attributes that I think are hobbies
            
            for hoe in hobbylist:                                                  # Iterates through the hobby list
                chsee = GROPH.nodes[node][hoe]                          # Finds the hobbies that the node does
                
                if chsee != 0:                                                          # If the hobby is not 0
                    hobbyscore = hobbyscore + 1                             # Adds one to the hobby score

            influence[node] = ( deg * (fri * 0.93) ) - year             # The node and its infuluence score are added to the dictionary infulence 
            highest_val = influence[node]                                    # The highest value is set an arbitray value
            highest = node                                                           # The highest node is set an arbitray node

    for student in influence:                                                   # Iterates through the students in influence dictionary 
        if highest_val > influence[student]:                              # finds the node with the highest score
            pass
        else:
            highest_val = influence[student]
            highest = student

    a = (GROPH.nodes[highest]["friends"])
    
    if aa == 'print':                                                                  # prints out the person who is the most infuential
        print(
f"""
    Student {highest} connects to {GROPH.degree(highest)} diffrent things and has {a} friends,
    therefore they are the most influential person. They were given a score of {influence[highest]}. 
    You must know {highest} to become the most influential"""
)
    else:
        return influence










def atar(GROPH, aa):
    bigbrains = []

    nerd_subjects = [ 'Atribute: tutorMath', 'Atribute: tutorEng', 'Atribute: tutorHums', 'Atribute: tutorScience']
    for subjects in nerd_subjects:
        nerds = list(GROPH.neighbors(subjects))
        for people in nerds:
            bigbrains.append(people)
    
    if aa == 'print':
        print(
f"""
    Student {mode(bigbrains)} is the best person to maxmise your atar/studyscore, as they have the most tutors"""
)
    else:
        return bigbrains











def news(GROPH):
    
    influ = influence(GROPH,'disco')
    trust = atar(GROPH, 'parabola')
    newspeople = {}
    for i in influ:
        newspeople[i] = influ[i]
    
    #print(trust)
    #print(influ)
    #print(newspeople)


    for people in trust:
        newscore = newspeople[people] * 2.52
        #print(newspeople[people])
        newspeople[people] = newscore 

    #print(newspeople)
    
    highest = 0
    for persons in newspeople:
        if highest > newspeople[persons]:
            pass
        else:
            highest = persons 
    
    print(
f"""
    The person who can spread news the best is {highest} as they have the highest trust/influence rating at {newspeople[highest]}"""
)
    pass

#print(list(G.neighbors(26)))
#print(G.nodes[26]["classes"])

influence(G,'print')
atar(G, 'print')
news(G)
print("\n")
#graphing.drawgraph(G)