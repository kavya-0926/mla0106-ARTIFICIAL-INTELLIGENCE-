parent(ram,raj).
parent(ram,rita).
parent(raj,anu).

grandparent(X,Y) :- parent(X,Z), parent(Z,Y).

