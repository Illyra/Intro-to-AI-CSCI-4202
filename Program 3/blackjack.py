import random

decks = 6                                                               # Setting the size of the shoe
shoe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4 * decks          # Creating the shoe
random.shuffle(shoe)                                                    # Shuffle the shoe

def deal():
    hand = []

    for i in range(2):
        card = shoe.pop()
        if card == 1:
            card = "A"
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        hand.append(card)
    return hand

def game_end():
    global result
    global dealer_total_var
    global player_total_var

    print("Dealers hand: " + str(dealer_total_var))
    print("Your hand: " + str(player_total_var))

    if player_total_var == dealer_total_var:
        print("Draw")
        result = "draw"
    elif player_total_var > dealer_total_var:
        print("You won")
        result = "won"
    elif dealer_total_var >= 22:
        print("Dealer busted")
        result = "won"
    else:
        print("You lost")
        result = "lost"

    print("Game ended")

def total(hand):
    total = 0
    for card in hand:
        if card == "A" and total >= 11:
            total += 1
        elif card == "A" and total <= 10:
            total += 11
        elif card == "J" or card == "Q" or card == "K":
            total += 10
        else:
            total += card
    return total

def dealer_turn():
    global dealer_total_var
    print("Dealers turn")

    while True:
        dealer_total_var = total(dealer_hand)

        print("Dealers hand is: " + str(dealer_hand))
        print("Dealers current total is: " + str(dealer_total_var))

        if dealer_total_var >= 17:
            game_end()
            break
        else:
            card = shoe.pop()
            if card == 1:
                card = "A"
            if card == 11:
                card = "J"
            if card == 12:
                card = "Q"
            if card == 13:
                card = "K"
            dealer_hand.append(card)

def blackjack():
    global result

    result = "blackjack"
    print("Player got a Blackjack")

def play_split():
    choice = input("Would you like to split your cards? y/n\n")
    if choice == "n":
        play()
    else:
        return

def stand():
    print("Ok, stand")
    dealer_turn()

def hit():
    global result
    global player_total_var

    while True:
        print("Ok, hit")
        
        card = shoe.pop()
        if card == 1:
            card = "A"
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        player_hand.append(card)
        
        player_total_var = total(player_hand)
        print("Players hand is: " + str(player_hand))
        print("Players current total is: " + str(player_total_var))

        if player_total_var >= 22:
            print("Looks like you busted")
            result = "lost"
            break

        choice = input("would you like to hit again or stand?\n")
        if choice == "stand":
            stand()
            break

def double():
    print("Ok, double")

def play():
    global result

    choice = input("Would you like to Hit, Stand or Double?\n")
    if choice == "stand":
        stand()
    elif choice == "hit":
        hit()
    elif choice == "double":
        double()
    else:
        print("Error, command not known")
        result  = "error"

def game(discord_uid, bet):
    global result
    global dealer_hand
    global player_hand

    global dealer_total_var
    global player_total_var

    result = ""

    dealer_hand = deal()
    player_hand = deal()

    dealer_total_var = total(dealer_hand)
    player_total_var = total(player_hand)

    print("Dealers current hand is: " + str(dealer_hand))
    print("Dealers current total is: " + str(dealer_total_var))
    
    print("Players current hand is: " + str(player_hand))
    print("Players current total is: " + str(player_total_var))

    if player_total_var == 21:
        blackjack()
    elif player_hand[0] == player_hand[-1]:
        play_split()
    else:
        play()

    return result

if __name__ == "__main__":
    game()