% ==============================================================================
% STUDENT COURSE ELIGIBILITY EXPERT SYSTEM IN PROLOG
% ==============================================================================
%
% PREREQUISITES:
% - Requires SWI-Prolog interpreter installed on your system.
% 
% HOW TO INSTALL PROLOG:
% - Windows (via Winget in Terminal):
%     winget install SWI-Prolog.SWI-Prolog
%   Or download installer directly from: https://www.swi-prolog.org/download/stable
% - Linux (Ubuntu/Debian):
%     sudo apt update && sudo apt install swi-prolog
% - macOS:
%     brew install swi-prolog
%
% HOW TO RUN:
% 1. Open terminal in this directory and launch SWI-Prolog:
%      swipl student_eligibility.pl
% 2. At the Prolog prompt (?-), run the start predicate:
%      ?- start.
% 3. IMPORTANT PROLOG SYNTAX:
%    - Every input must be entered in lowercase and end with a period (.)!
%    Examples:
%      Enter Student Name: nayna.
%      Enter Course: engineering.
% 4. To exit Prolog, type:
%      halt.
% ==============================================================================

% ==============================================================================
% SECTION 1: KNOWLEDGE BASE - FACTS
% ==============================================================================
% Registered students
student(nayna).
student(harshad).

% Academic qualification facts: 12th Grade Completion
completed_12th(nayna).
completed_12th(harshad).

% Academic progression facts: Minimum Credits Requirement
completed_credits(nayna).
completed_credits(harshad).

% Disciplinary / Academic standing: No pending backlogs
no_backlog(nayna).
no_backlog(harshad).

% Minimum GPA / Passing grade verification
valid_grade(nayna).
valid_grade(harshad).

% Enrolled / Intended Degree Course mappings
degree(nayna, engineering).
degree(harshad, bba).


% ==============================================================================
% SECTION 2: INFERENCE RULES
% ==============================================================================
% Rule: eligible(X)
% A student X is eligible if ALL condition predicates evaluate to True:
%   1. X must be an enrolled student.
%   2. X must have completed 12th grade.
%   3. X must have satisfied credit requirements.
%   4. X must have no active backlogs.
%   5. X must maintain a valid passing grade.
eligible(X) :-
    student(X),
    completed_12th(X),
    completed_credits(X),
    no_backlog(X),
    valid_grade(X).


% ==============================================================================
% SECTION 3: USER CONSULTATION INTERACTION
% ==============================================================================
start :-
    write('==========================================='), nl,
    write('     STUDENT COURSE ELIGIBILITY SYSTEM     '), nl,
    write('==========================================='), nl,
    write('Known Students: nayna. | harshad.'), nl,
    write('Enter Student Name (lowercase, end with .): '),
    read(X),

    write('Enter Course (e.g., engineering. or bba.): '),
    read(D),
    nl,

    % Evaluate eligibility rule and degree association
    (   eligible(X), degree(X, D)
    ->  write('RESULT: [ELIGIBLE] Student '), write(X),
        write(' is eligible for course: '), write(D), nl
    ;   write('RESULT: [NOT ELIGIBLE] Requirements not satisfied for student '),
        write(X), write(' in course '), write(D), nl
    ).
