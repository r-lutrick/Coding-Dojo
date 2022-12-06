from classes import deck, player

# Instanciate the Deck, Dealer and Player(s)
bicycle = deck.Deck()
dealer = player.Dealer("DeanTheDealer")
player1 = player.Player("JimBob")

# Deal cards
# Eventually the 2 will be replaced with num_of_players
for i in range(2):
    dealer.hit(bicycle.deal_card())
    player1.hit(bicycle.deal_card())

# Using a while loop to allow for future game use
# Plans to add multiple players to a table
while dealer.turn == True or player1.turn == True:
    # Start the game
    print("======- Dealers hand -======")
    dealer.display_hand()
    print(f"Dealer: {dealer.get_total()}")
    print("============================\n\n")

    # Player 1 turn
    while player1.turn == True:
        # Total value of cards
        current_hand_value = player1.get_total()

        # Display
        print("\n=======- Your hand -========")
        player1.display_hand()
        print(f"Player has: {current_hand_value}")
        print("============================\n")

        # Check for BlackJack and Win
        if (player1.get_total() == 21):
            print(f"BLACKJACK!!! {player1.get_total()}\n")
            player1.hand = []
            player1.stay()
        else:
            choice = input("[1]Hit or [2]Stay:\n> ")

            # Hit
            if choice == "1":
                # Get, display and add card to hand
                incoming_card = bicycle.deal_card()
                incoming_card.card_info()
                player1.hit(incoming_card)
                # Evaluate total value of cards in hand
                new_hand = player1.get_total()

                # Check for bust
                if new_hand > 21:
                    print(f"Player BUSTED! {player1.get_total()}\n")
                    # Resets for future use
                    player1.hand = []
                    player1.stay()

                # Check for BlackJack
                if new_hand == 21:
                    print(f"BLACKJACK! {player1.get_total()}\n")
                    # Resets for future use
                    player1.hand = []
                    player1.stay()
            # Stay
            elif choice == "2":
                player1.stay()
                print(f"Staying: {player1.get_total()}\n")
            # Default
            else:
                input(
                    "Please choose a valid option\nPress [enter] to continue...")

    # Dealer Turn (This should always be last)
    while dealer.turn == True:
        # Start turn with total card value from hand
        d_total = dealer.get_total()

        # Dealer must stay past 16 points
        if d_total > 16:
            dealer.stay()
            print(f"Dealer stays: {dealer.get_total()}")
        else:
            # Get, display and add card to hand
            random_card = bicycle.deal_card()
            print(f"Dealer: {d_total}")
            dealer.hit(random_card)
            # Dealt card
            print(
                f"Dealer gets {random_card.string_val} {random_card.suit}")
            # Evaluate if card total value is Bust
            if dealer.get_total() > 21:
                print(f"Dealer BUSTED! {dealer.get_total()}")
                # Resets for future use
                dealer.hand = []
                dealer.stay()

    # Get game totals
    dealer_hand = dealer.get_total()
    player1_hand = player1.get_total()

    # Game decision
    if dealer_hand > player1_hand:
        print(f"\n\t... You Lose ...\n")
    elif dealer_hand < player1_hand:
        print(f"\n\t!!! You WIN !!!\n")
    else:
        print("\n\t=== You Push ===\n")
