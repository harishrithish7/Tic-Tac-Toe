import operator
import numpy as np
from numpy import *
from random import random,randint,uniform

def evolve(weights,fitnesses,retain=0.2,random_select=0.05) :
    """
    The function returns the individuals for the next generation using genetic algorithm.

    Genetic Algorithm:
        The best performing individuals are retained.
        Diversity is maintained by selecting random individuals from the not-so-good lot.
        These individuals(parents) mate among themselves to produce new individuals(children).
        The children and parents form the next generation.

    weights - Neural Network weights of the players
    fitnesses - fitnesses of each individual
    retain - retain percentage for next generation
    random_select - percentage of individuals to be selected randomly
                    to maintain diversity
    """
    retain_len = int(retain*len(fitnesses))
    grade = [ (fit,wt) for fit,wt in zip(fitnesses,weights) ]
    graded = [ x[1] for x in sorted(grade,key=operator.itemgetter(0),reverse=True) ]
    graded_fitness = [ x[0] for x in sorted(grade,key=operator.itemgetter(0),reverse=True) ]
    
    #selecting only the fittest individuals for next gen
    parents = graded[:retain_len]
    parent_fitness = graded_fitness[:retain_len]

    #selecting random individuals to maintain diversity
    for wt,fit in zip(graded[retain_len:],graded_fitness[retain_len:]) :
        if random_select > random() :
            parents.extend(wt)
            parent_fitness.append(fit)

    parents_len = len(parents)
    desired_len = len(fitnesses)-parents_len
    children = []

    #creating the rank_wheel for selecting male and female for reproduction
    rank_wheel = [ len(parents)-x for x in range(len(parents)) ]
    for x in range(1,len(rank_wheel)) :
        rank_wheel[x] += rank_wheel[x-1]
    max_rank = max(rank_wheel)
    
    #selecting the children
    while len(children) < desired_len :
        male = randint(1,max_rank)
        female = randint(1,max_rank)
        for i,rank in enumerate(rank_wheel) :
            if male <= rank :
                male = i
                break
        for i,rank in enumerate(rank_wheel) :
            if female <= rank :
                female = i
                break

        if male != female :
            male = parents[male]
            female = parents[female]
            child = np.copy(male)
            for i in range(male.shape[1]) :
                if random() > 0.5 :
                    try :
                        child[0,i] = female[0,i]
                    except IndexError :
                        return
            children.append(child)

    #children are now added to parents ; parents now contain all the individuals for next generation
    parents.extend(children)
    parents = [ mat(x) for x in parents ]
    return parents
