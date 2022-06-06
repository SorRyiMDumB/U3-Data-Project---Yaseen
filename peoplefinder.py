from cmath import inf
import graphing
import networkx as nx
from statistics import mode
 
from collections import Counter
G = nx.Graph()

graphing.addnodes(G)
graphing.defultgraph(G)

def influence(GROPH, aa):
    influence = {}
    for node in GROPH:
        #print(f"{node} is type {type(node)}")
        if type(node) == int:
            deg = GROPH.degree(node)
            fri = GROPH.nodes[node]["friends"]
            year =  ( 1 / GROPH.nodes[node]["year"] ) * 100

            hobbyscore = 0

            hobbylist = ['genshin', 'f1', 'sport']
            
            for hoe in hobbylist:
                chsee = GROPH.nodes[node][hoe]
                
                if chsee != 0:
                    hobbyscore = hobbyscore + 1
            #print(node, hobbyscore)

            influence[node] = ( deg * (fri * 0.93) ) - year
            highest_val = influence[node]
            highest = node
    
    #print(influence)
    for student in influence:
        if highest_val > influence[student]:
            pass
        else:
            highest_val = influence[student]
            highest = student
    a = (GROPH.nodes[highest]["friends"])
    
    if aa == 'print':
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