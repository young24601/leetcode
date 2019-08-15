# given a list of words sorted by the alien alphabet

# Alphabet is b f g q
# bgg
# fbq
# fqf
# ffq
# gfg
# looking at first letter, b < f < g

# build a graph that has these relations.  Nodes will point to other nodes it is
# in front of.

# class G has methods.
# add and remove edges
# def add(self, c1, c2)
# def remove(self, c1, c2)
# def outgoing(self, c) # returns list of characters
# def incoming(self, c) # returns list of characters


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Graph:
    def add(self, c1, c2):
        c1.next = c2


def gen_graph(wordList):

    for word in wordList:


    return 0



gen_graph(["bgg", "fbq", "fqf", "ffq", "gfg"])
