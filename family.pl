% Facts
parent(john, mary).
parent(john, mike).
parent(susan, mary).
parent(susan, mike).

male(john).
female(susan).
female(mary).
male(mike).

% Rule: X is mother of Y
mother(X, Y) :-
    parent(X, Y),
    female(X).

% Rule: X is father of Y
father(X, Y) :-
    parent(X, Y),
    male(X).

% Rule: X and Y are siblings
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
 