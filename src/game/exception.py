class GameRuleException(Exception):
    pass


class SizeNotValidException(GameRuleException):
    pass


class NoEmptyTileException(GameRuleException):
    pass


class NoTileFoundException(GameRuleException):
    pass


class MoveException(GameRuleException):
    pass
