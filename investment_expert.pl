
risk(low).
risk(medium).
risk(high).

goal(safety).
goal(growth).
goal(income).

recommend(low, safety, fixed_deposit).
recommend(low, income, bonds).
recommend(medium, growth, mutual_funds).
recommend(medium, income, bonds).
recommend(high, growth, stocks).
recommend(high, income, dividend_stocks).

start :-
    write('Enter your risk level : '),
    read(Risk),
    
    write('Enter your investment goal : '),
    read(Goal),

    recommend(Risk, Goal, Investment),

    write('Recommended investment: '),
    write(Investment),
    nl.
