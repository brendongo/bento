class tqdm:
    def __init__(
        self,
        iterable=None,
        desc=None,
        total=None,
        leave=True,
        file=None,
        ncols=None,
        mininterval=0.1,
        maxinterval=10.0,
        miniters=None,
        ascii=None,
        disable=False,
        unit="it",
        unit_scale=False,
        dynamic_ncols=False,
        smoothing=0.3,
        bar_format=None,
        initial=0,
        position=None,
        postfix=None,
        unit_divisor=1000,
    ): ...
    def update(self, n: int = 1) -> None: ...
    def close(self) -> None: ...
    def set_postfix_str(self, text: str) -> None: ...
