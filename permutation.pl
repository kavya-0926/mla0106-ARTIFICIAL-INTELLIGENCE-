perm([],[]).
perm(L,[H|T]) :-
    delete(H,L,R),
    perm(R,T).
