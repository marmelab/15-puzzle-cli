class GameRuleException(Exception):
    pass


class GridSizeNotValidException(GameRuleException):
    pass


class NoEmptyTileException(GameRuleException):
    pass


class NoTileFoundException(GameRuleException):
    pass


class MoveException(GameRuleException):
    pass
