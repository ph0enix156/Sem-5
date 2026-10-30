% ==============================================================================
% INVESTMENT ADVISOR EXPERT SYSTEM (RULE-BASED INFERENCE IN PROLOG)
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
% 1. Open your terminal in this directory and launch SWI-Prolog:
%      swipl investment_expert.pl
% 2. At the Prolog prompt (?-), execute the start predicate:
%      ?- start.
% 3. IMPORTANT PROLOG SYNTAX:
%    Every input you type in Prolog MUST end with a period (.)!
%    Examples:
%      Enter your risk level: low.
%      Enter your investment goal: safety.
% 4. To exit Prolog prompt, type:
%      halt.
% ==============================================================================

% ==============================================================================
% SECTION 1: KNOWLEDGE BASE - FACT DEFINITIONS (VALID DOMAINS)
% ==============================================================================
% Valid risk tolerance levels
risk(low).
risk(medium).
risk(high).

% Valid financial goals
goal(safety).
goal(growth).
goal(income).

% ==============================================================================
% SECTION 2: INFERENCE RULES - INVESTMENT RECOMMENDATIONS
% ==============================================================================
% Format: recommend(RiskTolerance, FinancialGoal, RecommendedAsset).
%
% Rule 1: Low risk + Capital preservation -> Fixed Deposit
recommend(low, safety, fixed_deposit).

% Rule 2: Low risk + Regular income -> Government/Corporate Bonds
recommend(low, income, bonds).

% Rule 3: Moderate risk + Long-term capital growth -> Diversified Mutual Funds
recommend(medium, growth, mutual_funds).

% Rule 4: Moderate risk + Steady income -> Balanced Bonds
recommend(medium, income, bonds).

% Rule 5: High risk + Aggressive capital growth -> Equity Stocks
recommend(high, growth, stocks).

% Rule 6: High risk + High periodic cash flow -> Dividend Yielding Stocks
recommend(high, income, dividend_stocks).

% ==============================================================================
% SECTION 3: USER INTERACTION ENGINE (CONSULTATION INTERFACE)
% ==============================================================================
% 'start/0' predicate queries user, matches rules against facts, and infers recommendation
start :-
    write('==========================================='), nl,
    write('      INVESTMENT ADVISOR EXPERT SYSTEM     '), nl,
    write('==========================================='), nl,
    write('Available Risk Levels: low. | medium. | high.'), nl,
    write('Enter your risk level (must end with .): '),
    read(Risk),

    nl,
    write('Available Goals: safety. | growth. | income.'), nl,
    write('Enter your investment goal (must end with .): '),
    read(Goal),

    nl,
    % Rule evaluation: unification finds the matching recommendation fact
    (   recommend(Risk, Goal, Investment)
    ->  write('-------------------------------------------'), nl,
        write('Recommended Investment Portfolio: '),
        write(Investment), nl,
        write('-------------------------------------------'), nl
    ;   write('Sorry, no suitable investment recommendation found for this combination.'), nl
    ).
