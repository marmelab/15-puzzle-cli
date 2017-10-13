class GameRuleException(Exception):
    pass


class NoEmptyTileException(GameRuleException):
    pass


class MoveException(GameRuleException):
    pass
