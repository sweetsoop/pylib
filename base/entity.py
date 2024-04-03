from pylib.mixin.dict_mixin import DictMixin


class Entity(DictMixin):
    def __init__(self) -> None:
        super().__init__()