from typing import Any

class Array:
    def __init__(self, n: int, dtype: Any):
        self.vals = [None] * n
        self.dtype = dtype

    def get(self, i: int) -> Any:
        """
        Return the value at index i
        """
        return self.vals[i]

    def put(self, i: int, val: Any) -> None:
        """
        Update the array at index i with val. Val must be same type
        as self.dtype
        """
        if not isinstance(val, self.dtype):
            raise ValueError(f"val is {type(val)}; must be {self.dtype}")

        self.vals[i] = val


