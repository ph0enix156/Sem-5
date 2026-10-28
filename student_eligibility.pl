% Student facts
student(nayna).
student(harshad).

completed_12th(nayna).
completed_12th(harshad).

completed_credits(nayna).
completed_credits(harshad).

no_backlog(nayna).
no_backlog(harshad).

valid_grade(nayna).
valid_grade(harshad).

degree(nayna, engineering).
degree(harshad, bba).
	
eligible(X) :-
    student(X),
    completed_12th(X),
    completed_credits(X),
    no_backlog(X),
    valid_grade(X).

% Check eligibility
start :-
    write('Enter Student Name: '),
    read(X),
    write('Enter Course: '),
    read(D),
    eligible(X),
    degree(X, D),
    write('Student is Eligible for: '),
    write(D),
    nl.