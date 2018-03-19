####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team02' # Only 10 chars displayed.
strategy_name = 'AnahFaniel, Jade Gardner, Genia Hudson'
strategy_description = 'Genia Hudson Team 2'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    
    def play_round(player1, player2, score1, score2, moves1, moves2):
    '''
    Calls the move() function from each module which return
    'c' or 'b' for collude or betray for each player.
    The history is provided in a string, e.g. 'ccb' indicates the player
    colluded in the first two rounds and betrayed in the most recent round.
    Returns a 2-tuple with score1 and score2 incremented by this round
    '''
    
  def play_iterative_rounds(player1, player2):
    '''
    Plays a random number of rounds (between 100 and 200 rounds) 
    of the iterative prisoners' dilemma between two strategies.
    player1 and player2 are modules.
    Returns 4-tuple, for example ('cc', 'bb', -200, 600) 
    but with much longer strings 
    '''
    number_of_rounds = random.randint(100, 200)
    moves1 = ''
    moves2 = ''
    score1 = 0
    score2 = 0
    for round in range(number_of_rounds):
        score1, score2, moves1, moves2 = play_round(player1, player2, score1, score2, moves1, moves2)
    return (score1, score2, moves1, moves2)
    
    Release = 0 #(R, "reward" in literature) when both players collude
    TREAT = 100 # (T, "temptation" in literature) when you betray your partner
    SEVERE_PUNISHMENT = -500 # (S, "sucker" in literature) when your partner betrays you
    PUNISHMENT = -250 # (P) when both players betray each other
    
     # Keep T > R > P > S to be a Prisoner's Dilemma
    # Keep 2R > T + S to be an Iterative Prisoner's Dilemma
    
    ERROR = -250
    
    # Get the two players' actions and remember them.
    action1 = player1.move(moves1, moves2, score1, score2)
    action2 = player2.move(moves2, moves1, score2, score1)
    if (type(action1) != str) or (len(action1) != 1):
        action1=' '
    if (type(action2) != str) or (len(action2) != 1):
        action2=' '
    
    # Change scores based upon player actions.
    actions = action1 + action2
    if actions == 'cc':
        # Both players collude; get reward.
        score1 += RELEASE
        score2 += RELEASE
    elif actions == 'cb':
        # Player 1 colludes, player 2 betrays; get severe, treat.
        score1 += SEVERE_PUNISHMENT
        score2 += TREAT
    elif actions == 'bc':
        # Player 1 betrays, player 2 colludes; get treat, severe.
        score1 += TREAT
        score2 += SEVERE_PUNISHMENT 
    elif actions == 'bb':
        # Both players betray; get punishment.   
        score1 += PUNISHMENT
        score2 += PUNISHMENT     
    else:
        # Both players get the "error score" if someone's code returns an improper action.
        score1 += ERROR
        score2 += ERROR
    
    # Append the actions to the previous histories.
    if action1 in 'bc':
        moves1 += action1
    else:
        moves1 += ' '
    if action2 in 'bc':
        moves2 += action2
    else:
        moves2 += ' '
                    
    # Return scores incremented by this round's results.
    return (score1, score2, moves1, moves2)  
            
def make_reports(modules, scores, moves):
    section0 = make_section0(modules, scores)
    section1 = make_section1(modules, scores)
    section2 = make_section2(modules, scores)
    
    section3 = []
    for index in range(len(modules)):
        section3.append(make_section3(modules, moves, scores, index))
    return section0, section1, section2, section3

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b') 
    ####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Melanin Poppin' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    return 'c'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
         
