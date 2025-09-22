import random
from dataclasses import dataclass, field
from constants import  GAME_CONSTANTS,GAME_STATE,WordEntity
from collections import deque,Counter
from utils import clearscreen
@dataclass
class GameStatus:
    state: GAME_STATE = GAME_STATE.NOT_STARTED
    lives_remaining: int = GAME_CONSTANTS.lives
    masked_word: list[str] = field(default_factory=list)
    target: WordEntity | None = None
    recent_guesses:deque=field(default_factory=lambda:deque(maxlen=3))


game_status = GameStatus()


def render_game_screen():
    clearscreen()

    print("-" * GAME_CONSTANTS.screen_width)
    print(f"{GAME_CONSTANTS.name:^{GAME_CONSTANTS.screen_width}}")
    print(
        f"{(GAME_CONSTANTS.life_symbol + ' ') * game_status.lives_remaining:>{GAME_CONSTANTS.screen_width}}"
    )
    if game_status.state == GAME_STATE.IN_PROGRESS:
        print(f"{' '.join(game_status.masked_word)}")
        print(f"{game_status.target.hint} 💡")
        print(f"Recent Guessed Letters: {game_status.recent_guesses}")
    elif game_status.state == GAME_STATE.VICTORY:
        print(f"🎉 You Won! You solved the word: {game_status.target.text} 🎉")
    elif game_status.state == GAME_STATE.DEFEAT:
        print(f"💔 Game Over! The word was: {game_status.target.text}")


def get_guessed_letter() -> str:
    while True:
        guess = input("Enter an alphabetic character: ").strip().upper()
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print(
                "Invalid input! Please enter a single alphabetic character. Try again..."
            )


def get_guess_letter():
     return random.choice(GAME_CONSTANTS.wordBank)
    


def set_guess_letter(target_word: str, masked_word: list[str], letter: str) -> None:
    for i in range(len(target_word)):
        if target_word[i] == letter and masked_word[i] == "_":
            masked_word[i] = letter
            break


def process_guess(guess: str) -> None:
    # TODO - 7.1: Validate player guess and update game status
    target_count=Counter(game_status.target.text)
    guess_count=Counter([letter for letter in game_status.masked_word if letter != "_"])
    remaining_count=target_count-guess_count
    if remaining_count[guess]>0:
        set_guess_letter(game_status.target.text,game_status.masked_word,guess)
        guess_count[guess]+=1
    else :
        game_status.lives_remaining-=1
    game_status.recent_guesses.append(guess)
    if target_count==guess_count:
        game_status.state=GAME_STATE.VICTORY
    elif game_status.lives_remaining==0:
        game_status.state=GAME_STATE.DEFEAT


def start_game():
    render_game_screen()
    input("Press a key to START the game...")
    game_status.state = GAME_STATE.IN_PROGRESS
    game_status.target = get_guess_letter()
    game_status.masked_word = list("_" * len(f"{game_status.target.text}"))


def main():
    
    start_game()

    while game_status.state not in [GAME_STATE.VICTORY, GAME_STATE.DEFEAT]:
        render_game_screen()
        guess = get_guessed_letter()
        process_guess(guess)
    render_game_screen()


if __name__ == "__main__":
    main()
