delete(X,[X|T],T).
delete(X,[H|T],[H|R]) :-
    delete(X,T,R).
