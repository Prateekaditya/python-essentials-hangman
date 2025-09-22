from dataclasses import dataclass, field
from constants import  GAME_CONSTANTS,GAME_STATE,WordEntity
from collections import deque
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
    # TODO - 5.1: Create a word bank
    # TODO - 6.1: return a word randomly and hint associated with it
    # Word Bank with Hints
    # PYTHON, Not the snake, but you’ll definitely debug its bites
    # ARRAY, If you’re lost, just index your way out!
    # LOOP, Round and round we go, where it ends, nobody knows
    # BINARY, It’s all 1s and 0s—unless there’s a typo in your logic
    # SYNTAX, It’s like grammar... but mess it up, and the compiler screams
    pass


def set_guess_letter(target_word: str, masked_word: list[str], letter: str) -> None:
    for i in range(len(target_word)):
        if target_word[i] == letter and masked_word[i] == "_":
            masked_word[i] = letter
            break


def process_guess(guess: str) -> None:
    # TODO - 7.1: Validate player guess and update game status
    pass


def main():
    # TODO - 4.1: How can we do better?
    render_game_screen()
    input("Press a key to START the game...")
    game_status.state = GAME_STATE.IN_PROGRESS
    game_status.target = get_guess_letter()
    game_status.masked_word = list("_" * len("<Target Word>"))

    while game_status.state not in [GAME_STATE.VICTORY, GAME_STATE.DEFEAT]:
        render_game_screen()
        guess = get_guessed_letter()
        process_guess(guess)
    render_game_screen()


if __name__ == "__main__":
    main()
