import random
import time

# Fancy banners
def show_intro():
    print(r"""
╔════════════════════════════════════════════╗
║    🎮 WELCOME TO TERMINAL BATTLE ARENA 🎮  ║
║       🪨 Rock ⚔ Paper 🛡 Scissors        ║
╚════════════════════════════════════════════╝
          Prepare for an epic showdown!
""")

# Add flair to choices
def emoji_choice(choice):
    return {
        "rock": "🪨 Rock",
        "paper": "📄 Paper",
        "scissors": "✂️ Scissors"
    }[choice]

# Get user choice
def get_player_move():
    print("\n🧙 Choose your weapon: [rock/paper/scissors]")
    choice = input("👉 Your move: ").lower().strip()
    if choice not in ['rock', 'paper', 'scissors']:
        print("❌ Invalid move. Try again.")
        return None
    return choice

# Decide winner
def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

# Game animation
def battle_animation():
    print("\n⚔️  Clash begins...", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()

# Game loop
def play_battle():
    player_score = 0
    computer_score = 0
    round_num = 1

    show_intro()

    while True:
        print(f"\n🌟 ROUND {round_num} 🌟")
        player_move = None
        while player_move is None:
            player_move = get_player_move()

        computer_move = random.choice(["rock", "paper", "scissors"])

        print(f"\n🧝‍♂️ You chose:     {emoji_choice(player_move)}")
        print(f"🤖 Computer chose: {emoji_choice(computer_move)}")
        
        battle_animation()

        result = decide_winner(player_move, computer_move)

        if result == "tie":
            print("🤝 It's a draw! Both warriors stand tall.")
        elif result == "player":
            print("🎯 You strike true! A powerful hit!")
            player_score += 1
        else:
            print("💥 Oof! Computer lands a sneaky blow!")
            computer_score += 1

        print(f"\n📊 Scoreboard — You: {player_score} | Computer: {computer_score}")

        again = input("\n🔁 Do you want another round? (y/n): ").strip().lower()
        if again != 'y':
            break
        round_num += 1

    # Game summary
    print("\n🏁 BATTLE OVER!")
    print(f"\n📜 Final Tally — You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("🏆 VICTORY! You are the champion of the arena! 🎉")
    elif computer_score > player_score:
        print("🧊 DEFEAT. The computer has bested you... this time.")
    else:
        print("⚔️ STALEMATE. You both fought bravely!")

    print("\n🙏 Thanks for playing Rock ⚔ Paper 🛡 Scissors!")

# Start the game
if __name__ == "__main__":
    play_battle()
