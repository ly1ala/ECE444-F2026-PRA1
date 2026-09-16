class utils:
    @staticmethod
    def reversed(number: int) -> int:
        if type(number) is not int:
            raise TypeError("number must be an integer")

        sign = -1 if number < 0 else 1
        return sign * int(str(abs(number))[::-1])

    @staticmethod
    def formatter(number: int) -> tuple[str, str]:
        if type(number) is not int:
            raise TypeError("number must be an integer")

        return bin(number), oct(number)