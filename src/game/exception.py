class GameRuleException(Exception):
    pass


class NoEmptyTileException(GameRuleException):
    pass


class NoTileFoundException(GameRuleException):
    pass


class MoveException(GameRuleException):
    pass
