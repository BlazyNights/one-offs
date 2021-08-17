import typing


def check_single_number(i: int) -> typing.Union[str, None]:
    output = ''
    if i % 3 == 0:
        output = f'{output}fizz'
    if i % 5 == 0:
        output = f'{output}buzz'
    if not output:
        output = None
    return output


class FizzBuzz:
    """
    This is just getting stupid at this point
    """
    def __init__(self,
                 iter_input: typing.Iterable[int],
                 process_up_front: bool):
        self.iter_input = iter_input
        self.fizzed = []
        self.buzzed = []
        self.fizzbuzzed = []
        if process_up_front:
            self._process_all()

    def _process_all(self) -> None:
        for i in self.iter_input:
            if check_single_number(i) == 'fizzbuzz':
                self.fizzed.append(i)
                self.buzzed.append(i)
                self.fizzbuzzed.append(i)
                continue
            if check_single_number(i) == 'fizz':
                self.fizzed.append(i)
            if check_single_number(i) == 'buzz':
                self.buzzed.append(i)

    def fizz(self) -> list:
        if self.fizzed:
            return self.fizzed
        for i in self.iter_input:
            if check_single_number(i) == 'fizz':
                self.fizzed.append(i)
        return self.fizzed

    def buzz(self) -> list:
        if self.buzzed:
            return self.buzzed
        for i in self.iter_input:
            if check_single_number(i) == 'buzz':
                self.buzzed.append(i)
        return self.buzzed

    def fizzbuzz(self) -> list:
        if self.fizzbuzzed:
            return self.fizzbuzzed
        for i in self.iter_input:
            if check_single_number(i) == 'fizzbuzz':
                self.fizzbuzzed.append(i)
        return self.fizzbuzzed

    def return_all(self) -> dict:
        return {
            'fizz': self.fizz(),
            'buzz': self.buzz(),
            'fizzbuzz': self.fizzbuzz()
        }

    def traditional_fizzbuzz(self) -> None:
        """
        A more traditional fizzbuzz experience, does not modify or use
        the object variables other than the iterable
        """
        for i in self.iter_input:
            print(i)
            result = check_single_number(i)
            if result:
                print(result)


overengineered_fizzbuzz = FizzBuzz(range(1, 21), False)
print(overengineered_fizzbuzz.fizz())
print(overengineered_fizzbuzz.buzz())
print(overengineered_fizzbuzz.fizzbuzz())
overengineered_fizzbuzz.traditional_fizzbuzz()
print(overengineered_fizzbuzz.return_all())


overengineered_fizzbuzz = FizzBuzz(range(1, 21), True)
print(overengineered_fizzbuzz.fizz())
print(overengineered_fizzbuzz.buzz())
print(overengineered_fizzbuzz.fizzbuzz())
print(overengineered_fizzbuzz.return_all())
