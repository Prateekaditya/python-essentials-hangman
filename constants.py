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
    wordBank:tuple[WordEntity,...]=(
        WordEntity("PYTHON", "Not the snake, but you’ll definitely debug its bites"),
        WordEntity("ARRAY", "If you’re lost, just index your way out!"),
        WordEntity("LOOP", "Round and round we go, where it ends, nobody knows"),
        WordEntity("BINARY", "It’s all 1s and 0s—unless there’s a typo in your logic"),
        WordEntity("SYNTAX", "It’s like grammar... but mess it up, and the compiler screams"),
        WordEntity("DEBUG", "The art of turning coffee into error fixes"),
        WordEntity("STRING", "Characters all tied together, literally"),
        WordEntity("STACK", "Where things pile up, until it overflows"),
        WordEntity("QUEUE", "Stand in line… first come, first served"),
        WordEntity("CLASS", "Blueprints for objects—like a factory of ideas"),
        WordEntity("OBJECT", "An instance that thinks it’s special"),
        WordEntity("METHOD", "Functions that think they belong to someone"),
        WordEntity("VARIABLE", "A container that can’t decide what it wants to hold"),
        WordEntity("CONSTANT", "Unlike your mood, this one never changes"),
        WordEntity("MODULE", "A file that insists it knows everything"),
        WordEntity("IMPORT", "Because reinventing the wheel is overrated"),
        WordEntity("FUNCTION", "A reusable spell—you cast it, it returns something"),
        WordEntity("EXCEPTION", "When your code panics, this pops up"),
        WordEntity("BOOLEAN", "It only knows two moods: True or False"),
        WordEntity("RECURSION", "When a function can’t stop calling itself—like an echo"),
    )

GAME_CONSTANTS = GameConstants()    


class GAME_STATE(enum.StrEnum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    VICTORY = "VICTORY"
    DEFEAT = "DEFEAT"