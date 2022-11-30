from classes import deck, player

bicycle = deck.Deck()
dealer = player.Player("DeanTheDealer")
player1 = player.Player("JimBob")

player1.turn = True

for i in range(2):
    dealer.hit(bicycle.deal_card())
    player1.hit(bicycle.deal_card())

# conditions for game end
# if all players turn == False



while dealer.turn == True or player1.turn == True:
    #Player 1 turn
    while player1.turn == True:
        current_hand_value = player1.get_total()

        print("======- Dealers hand -======")
        dealer.display_hand()
        print(f"Dealer has: {dealer.get_total()}")
        print("============================\n\n")
        print("=======- Your hand -========")
        player1.display_hand()
        print(f"Player has: {current_hand_value}")
        print("============================\n")

        choice = input("[1]Hit or [2]Stay:\n> ")

        if choice == "1":
            player1.hit(bicycle.deal_card())
            new_hand = player1.get_total()
            if new_hand > 21:
                print(f"Player BUSTED with {player1.get_total()}")
                player1.hand = []
                player1.stay()
        elif choice == "2":
            player1.stay()
            print(f"Staying at: {player1.get_total()}\n")
        else:
            input("Please choose a valid option\nPress [enter] to continue...")

    # Dealer Turn (This should always be last)
    while dealer.turn == True:
        d_total = dealer.get_total()
        print(f"Dealer has: {d_total}")
        if d_total > 16:
            dealer.stay()
            print(f"Dealer stays at: {dealer.get_total()}")
        else:
            random_card = bicycle.deal_card()
            dealer.hit(random_card)
            print(f"Dealer gets {random_card.string_val} of {random_card.suit}")
            if dealer.get_total() > 21:
                print(f"Dealer BUSTED with {dealer.get_total()}")
                dealer.hand = []
                dealer.stay()


    dealer_hand = dealer.get_total()
    player1_hand = player1.get_total()

    if dealer_hand > player1_hand:
        print(f"You Lose..")
    elif dealer_hand < player1_hand:
        print(f"You WIN!!")
    else:
        print("IDK what happened but you didn't win or lose")