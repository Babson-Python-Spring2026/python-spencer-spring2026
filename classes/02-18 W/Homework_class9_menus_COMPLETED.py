'''
We want to create a command line driven menu system with 4 levels

1. Clients
    1. Select Client
        1. View Client Summary
        2. Manage Client Cash
    2. Create Client
        1. New Individual
        2. New Joint

2. Portfolios
    1. Trade
        1. Buy
        2. Sell
    2. Performance
        1. Holdings Snapshot
        2. P/L Report

1st level                                   (Clients LHS,                             |                  Portfolios RHS)
2nd level              (Select Client,                         Create Client)         |        (Trade,                  Performance)
3rd level (View Client Summary, Manage Client Cash)    (New Individual, New Joint)    |      (Buy, Sell)         (Holdings Snapshot, P/L Report)
4th leaf  (View Client Summary, Manage Client Cash)    (New Individual, New Joint)    |      (Buy, Sell)         (Holdings Snapshot, P/L Report)


The left hand side (LHS) is provided below. Your job:

1) complete the right hand side (RHS)
    a) Hint: this is copy and paste
    b) changing what gets printed

2) explain in your own words what the program does
    a) Try to include state, transitions and invariants
    b) Does menu control come from logic or program structure

3) assume you are at a leaf endpoint. Instead of returning to level 3
   return to level 1

4) How many discrete paths are in this menu system
'''

'''
===================================================================================
PART 2: STI EXPLANATION
===================================================================================

What the program does:
This is a nested menu system that lets users navigate through different options.
You start at the top level and drill down into submenus until you hit a "leaf" 
(an endpoint with no more choices). Then you work your way back up.

STATE:
The main state is basically "where am I in the menu tree". But heres the thing -
theres no explicit state variable tracking the level. The state is implicit in which
while loop youre currently inside. If youre in the innermost while loop under
Clients > Select Client, thats your state. The `choice` variable holds the most
recent selection but it gets reused at every level so its not really tracking
overall state.

The `to_top` flag is different though - thats an explicit state variable I added
for the return-to-top feature. It acts like a signal that propagates up through
the nested loops. When its True, each loop checks it and breaks immediately.

TRANSITIONS:
- Selecting a numbered option (1 or 2) transitions you deeper into the menu
- Pressing Enter with no input (returns None) triggers a break which transitions
  you back up one level
- The continue statement keeps you at the current level after hitting a leaf
- Setting to_top = True at a leaf causes a chain of breaks that unwinds all the 
  way back to level 1 (where to_top gets reset to False)

INVARIANTS:
- Each menu level always shows a header, displays options, and waits for input
- A break statement only exits ONE while loop - it cant skip multiple levels
  (this tripped me up at first, I thought break would go all the way back)
- You can only move one level at a time in either direction

Does control come from logic or structure?
I'd say its the STRUCTURE thats doing the heavy lifting here. The nested while 
loops ARE the state machine. Each while loop represents a level in the menu.
Yeah theres if/elif logic for handling choices, but the actual "where am I" 
state comes from which loop youre sitting in. If you wanted logic-based control
youd have like a single while loop with a state variable and a big switch 
statement. This is different - the nesting itself encodes the hierarchy.

===================================================================================
'''

'''
OIM 3600 - Menu Navigation Assignment Rubric
--------------------------------------------

Student Name: ______________________
Score: ______ / 100


FUNCTIONAL REQUIREMENTS (70 pts)
--------------------------------

TOP / CLIENTS / PORTFOLIOS NAVIGATION (30 pts)

[ ] TOP menu displays correctly
[ ] Can navigate TOP → CLIENTS → back to TOP
[ ] Can navigate TOP → PORTFOLIOS → back to TOP
[ ] No infinite loops
[ ] No accidental fall-through (one choice triggers one action)


PORTFOLIO BRANCH IMPLEMENTATION (20 pts)

[ ] Portfolio branch fully implemented
[ ] At least one working leaf under PORTFOLIOS
[ ] Back behavior correct within portfolio branch


EXIT-TO-TOP BEHAVIOR (20 pts - A-level feature)

[ ] "Return to Top" works from at least one CLIENT leaf
[ ] "Return to Top" works from at least one PORTFOLIO leaf
[ ] No duplicate menus printed after return
[ ] No stuck loops after return
[ ] to_top cleared only at TOP level


CONTROL FLOW QUALITY (15 pts)

[ ] Correct one-level unwind via break
[ ] Each loop checks to_top appropriately
[ ] Code readable and logically structured


STI EXPLANATION (15 pts)

[ ] Identifies key state variables (to_top, etc.)
[ ] Correctly defines transitions
[ ] States invariant about unwinding
[ ] Distinguishes state vs control flow


GRADE BANDS
-----------

C (70-79)
- Honest attempt
- Portfolio branch partially implemented
- Some unwind logic present
- STI explanation minimal or partially incorrect

B (80-89)
- Both branches work correctly
- One-level back behavior correct
- No infinite loops
- STI explanation identifies state, transitions, invariant

A (90-100)
- Exit-to-top works from leaf level (both branches)
- No duplicate menus or stuck loops
- to_top handled cleanly
- STI explanation clearly distinguishes state vs control flow
'''


'''
THIS ASSIGNMENT WILL BE DUE 2/25 (NEXT WEDNESDAY) SO YOU CAN ASK QUESTIONS NEXT MONDAY (2/23)
'''



import functions2 as fn2

# flag for returning directly to top menu from any leaf
to_top = False

while True:
    # reset to_top flag at level 1 - this is the ONLY place it gets cleared
    to_top = False
    
    fn2.clear_screen()
    fn2.print_header('Top Menu level 1')
    options=['Clients', 'Portfolios'] #level 1 options
    fn2.display_menu(options)
    choice = fn2.get_menu_choice(options)

    if choice is None:
        print('exit top level menu')
        fn2.pause(1)
        break
    elif choice == 1:
        while True:
            # check if we need to skip back to top
            if to_top:
                break
                
            fn2.clear_screen()
            fn2.print_header('Clients level 2')
            options=['Select Client', 'Create Client'] #level 2 options
            fn2.display_menu(options)
            choice = fn2.get_menu_choice(options)

            if choice is None:
                print('return to level 1')
                fn2.pause(1)
                break
            elif choice == 1:
                while True:
                    # check if we need to skip back to top
                    if to_top:
                        break
                        
                    fn2.clear_screen()
                    fn2.print_header('Select Client level 3')
                    options=['View Client Summary', 'Manage Client Cash'] #level 3 options
                    fn2.display_menu(options)
                    choice = fn2.get_menu_choice(options)

                    if choice is None:
                        print('return to level 2')
                        fn2.pause(1)
                        break
                    elif choice == 1:
                        # no while statement leaf
                        fn2.clear_screen()
                        fn2.print_header('View Client Summary level 4')
                        # no options leaf
                        print('you have reached View Client Summary')
                        # option to return to top menu
                        go_top = input('\nType "top" to return to main menu, or press Enter for level 3: ')
                        if go_top.lower() == 'top':
                            to_top = True
                            break
                        fn2.pause(1)
                        
                        continue # not needed but shows intent
                           
                    elif choice == 2:
                        # no while statement leaf
                        fn2.clear_screen()
                        fn2.print_header('Manage Client Cash level 4')
                        # no options leaf
                        print('you have reached Manage Client Cash')
                        # option to return to top menu
                        go_top = input('\nType "top" to return to main menu, or press Enter for level 3: ')
                        if go_top.lower() == 'top':
                            to_top = True
                            break
                        fn2.pause(1)

                        continue # not needed but shows intent

            elif choice == 2:
                while True:
                    # check if we need to skip back to top
                    if to_top:
                        break
                        
                    fn2.clear_screen()
                    fn2.print_header('Create Client level 3')
                    options=['New Individual', 'New Joint'] #level 3 options
                    fn2.display_menu(options)
                    choice = fn2.get_menu_choice(options)

                    if choice is None:
                        print('return to level 2')
                        fn2.pause(1)
                        break
                    elif choice == 1:
                        # no while statement leaf
                        fn2.clear_screen()
                        fn2.print_header('New Individual level 4')
                        # no options leaf
                        print('you have reached New Individual')
                        # option to return to top menu
                        go_top = input('\nType "top" to return to main menu, or press Enter for level 3: ')
                        if go_top.lower() == 'top':
                            to_top = True
                            break
                        fn2.pause(1)

                        continue # not needed but shows intent
                           
                    elif choice == 2:
                        # no while statement leaf
                        fn2.clear_screen()
                        fn2.print_header('New Joint level 4')
                        # no options leaf
                        print('you have reached New Joint')
                        # option to return to top menu
                        go_top = input('\nType "top" to return to main menu, or press Enter for level 3: ')
                        if go_top.lower() == 'top':
                            to_top = True
                            break
                        fn2.pause(1) 

                        continue # not needed but shows intent   
    elif choice == 2:
        # PORTFOLIOS BRANCH (RHS) - mirrors the Clients structure
        while True:
            # check if we need to skip back to top
            if to_top:
                break
                
            fn2.clear_screen()
            fn2.print_header('Portfolios level 2')            
            options = ['Trade', 'Performance'] #level 2 options
            fn2.display_menu(options)
            choice = fn2.get_menu_choice(options)

            if choice is None:
                print('return to level 1')
                fn2.pause(1)
                break
            elif choice == 1:
                while True:
                    # check if we need to skip back to top
                    if to_top:
                        break
                        
                    fn2.clear_screen()
                    fn2.print_header('Trade level 3')
                    options = ['Buy', 'Sell'] #level 3 options
                    fn2.display_menu(options)
                    choice = fn2.get_menu_choice(options)

                    if choice is None:
                        print('return to level 2')
                        fn2.pause(1)
                        break
                    elif choice == 1:
                        # no while statement leaf
                        fn2.clear_screen()
                        fn2.print_header('Buy level 4')
                        # no options leaf
                        print('you have reached Buy')
                        # option to return to top menu
                        go_top = input('\nType "top" to return to main menu, or press Enter for level 3: ')
                        if go_top.lower() == 'top':
                            to_top = True
                            break
                        fn2.pause(1)

                        continue # not needed but shows intent

                    elif choice == 2:
                        # no while statement leaf
                        fn2.clear_screen()
                        fn2.print_header('Sell level 4')
                        # no options leaf
                        print('you have reached Sell')
                        # option to return to top menu
                        go_top = input('\nType "top" to return to main menu, or press Enter for level 3: ')
                        if go_top.lower() == 'top':
                            to_top = True
                            break
                        fn2.pause(1)

                        continue # not needed but shows intent

            elif choice == 2:
                while True:
                    # check if we need to skip back to top
                    if to_top:
                        break
                        
                    fn2.clear_screen()
                    fn2.print_header('Performance level 3')
                    options = ['Holdings Snapshot', 'P/L Report'] #level 3 options
                    fn2.display_menu(options)
                    choice = fn2.get_menu_choice(options)

                    if choice is None:
                        print('return to level 2')
                        fn2.pause(1)
                        break
                    elif choice == 1:
                        # no while statement leaf
                        fn2.clear_screen()
                        fn2.print_header('Holdings Snapshot level 4')
                        # no options leaf
                        print('you have reached Holdings Snapshot')
                        # option to return to top menu
                        go_top = input('\nType "top" to return to main menu, or press Enter for level 3: ')
                        if go_top.lower() == 'top':
                            to_top = True
                            break
                        fn2.pause(1)

                        continue # not needed but shows intent

                    elif choice == 2:
                        # no while statement leaf
                        fn2.clear_screen()
                        fn2.print_header('P/L Report level 4')
                        # no options leaf
                        print('you have reached P/L Report')
                        # option to return to top menu
                        go_top = input('\nType "top" to return to main menu, or press Enter for level 3: ')
                        if go_top.lower() == 'top':
                            to_top = True
                            break
                        fn2.pause(1)

                        continue # not needed but shows intent


'''
===================================================================================
PART 4: DISCRETE PATHS
===================================================================================

There are 8 discrete paths to leaf endpoints:

Clients side (4 paths):
1. Top -> Clients -> Select Client -> View Client Summary
2. Top -> Clients -> Select Client -> Manage Client Cash
3. Top -> Clients -> Create Client -> New Individual
4. Top -> Clients -> Create Client -> New Joint

Portfolios side (4 paths):
5. Top -> Portfolios -> Trade -> Buy
6. Top -> Portfolios -> Trade -> Sell
7. Top -> Portfolios -> Performance -> Holdings Snapshot
8. Top -> Portfolios -> Performance -> P/L Report

Plus theres the exit path from the top menu (pressing enter at level 1) but I 
dont think that counts as a "path through the menu" since youre just leaving.

===================================================================================
'''
