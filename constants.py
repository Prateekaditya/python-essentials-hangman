from typing import NamedTuple
import enum

class WordEntity(NamedTuple):
    text:str
    hint:str

    
class GameConstants(NamedTuple):
    name: str = "Hangman with 🐍"
    lives: int = 5
    life_symbol: str = "❤️"
    screen_width: int = 80

GAME_CONSTANTS = GameConstants()    


class GAME_STATE(enum.StrEnum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    VICTORY = "VICTORY"
    DEFEAT = "DEFEAT"