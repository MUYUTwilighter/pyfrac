class frac:
    def __init__(self, *nums) -> None:
        for num in nums:
            assert type(num) in (int, float, complex, frac), \
                "TypeError: Can only convert int, float, complex or frac to frac"
            assert num != 0, "ZeroDivisionError: division by zero"
            if type(num) == complex:
                assert (len(str(num.real)) - str(num.real).find('.') - 1) <= 17 and \
                    (len(str(num.imag)) - str(num.imag).find('.') - 1) <= 17, \
                    "TooSmallError: frac contains too small numbers and can not be reduced."
            elif type(num) == float:
                assert (len(str(num)) - str(num).find('.') - 1) <= 17, \
                    "TooSmallError: frac contains too small numbers and can not be reduced."
        if len(nums) == 0:
            nums = (0, 1)
        self.num = 0
        '''Do not modify this in the way like self.num = 0'''
        self.den = 1
        '''Do not modify this in the way like self.den = 0'''
        self.reduce(nums)
        del nums
    
    # "{}".format(self)
    def __format__(self, format_spec:str) -> str:
        return "{} / {}".format(self.num, self.den)

    # abs(self)
    def __abs__(self) -> float:
        return abs(self.calc())
    
    # bool(self)
    def __bool__(self) -> bool:
        return bool(self.num)

    # int(self)
    def __int__(self) -> int:
        assert type(self.num) != complex, \
            "ValueError: Can not convert fractions with complex to integer"
        return int(self.calc())
    
    # float(self)
    def __float__(self) -> float:
        assert type(self.num) != complex, \
            "ValueError: Can not convert fractions with complex to float"
        return self.calc()
    
    # complex(self)
    def __complex__(self) -> complex:
        return complex(self.calc())

    # str(self)
    def __str__(self) -> str:
        return "{} / {}".format(self.num, self.den)
    
    #
    def __repr__(self) -> str:
        '''Return stringn'''
        return "frac({}, {})".format(self.num, self.den)

    # 
    def __call__(self, index:int = 2) -> tuple or int or complex:
        '''
        self(index = 2)
        index:
            0, return numerator
            1, return denominator
            2, return (numerator, denominator)
        '''
        assert type(index) == int, \
            "TypeError: argument 'index' expecting integers"
        assert index in range(0, 3), \
            "TypeError: index out of range"
        if index == 0:
            return self.num
        elif index == 1:
            return self.den
        else:
            return (self.num, self.den)

    # compute
    # +
    def __add__(self, other = 0):
        assert (type(other) in (int, float, frac, complex)), \
            "TypeError: unsupported operand type(s) for +: 'frac' and '{}'".format(type(other))
        if type(other) != frac:
            other = frac(other)
        return frac(self.num * other.den + self.den * other.num, self.den * other.den)
    
    def __radd__(self, other = 0):
        assert (type(other) in (int, float, frac, complex)), \
            "TypeError: unsupported operand type(s) for +: 'frac' and '{}'".format(type(other))
        if type(other) != frac:
            other = frac(other)
        return frac(self.num * other.den + self.den * other.num, self.den * other.den)
    
    # -
    def __sub__(self, other = 0):
        assert (type(other) in (int, float, frac, complex)), \
            "TypeError: unsupported operand type(s) for -: 'frac' and '{}'".format(type(other))
        if type(other) != frac:
            other = frac(other)
        return frac(other.den * self.num - other.num * self.den, self.den * other.den)
    
    def __rsub__(self, other = 0):
        assert (type(other) in (int, float, frac, complex)), \
            "TypeError: unsupported operand type(s) for -: 'frac' and '{}'".format(type(other))
        if type(other) != frac:
            other = frac(other)
        return frac(other.num * self.den - other.den * self.num, self.den * other.den)
    
    # *
    def __mul__(self, other = 1):
        assert (type(other) in (int, float, frac, complex)), \
            "TypeError: unsupported operand type(s) for *: 'frac' and '{}'".format(type(other))
        if type(other) != frac:
            other = frac(other)
        return frac(self.num * other.num, self.den * other.den)
    
    def __rmul__(self, other = 1):
        assert (type(other) in (int, float, frac, complex)), \
            "TypeError: unsupported operand type(s) for *: 'frac' and '{}'".format(type(other))
        if type(other) != frac:
            other = frac(other)
        return frac(self.num * other.num, self.den * other.den)
    
    # /
    def __truediv__(self, other):
        assert type(other) in (int, float, frac, complex), \
            "TypeError: unsupported operand type(s) for /: 'frac' and '{}'".format(type(other))
        if type(other) != frac:
            other = frac(other)
        return frac(self.num * other.den, self.den * other.num)
    
    def __rtruediv__(self, other):
        assert type(other) in (int, float, frac, complex), \
            "TypeError: unsupported operand type(s) for /: 'frac' and '{}'".format(type(other))
        if type(other) != frac:
            other = frac(other)
        return frac(self.den * other.num, self.num * other.den)
    
    # //
    def __floordiv__(self, other) -> int:
        assert type(other) in (int, float, frac), \
            "TypeError: unsupported operand type(s) for //: 'frac' and '{}'".format(type(other))
        assert type(self.num) != complex, \
            "TypeError: Cannot take floor of a fraction with complex"
        if type(other) == frac:
            assert type(other.num) != complex, \
                "TypeError: Cannot take floor of a fraction with complex"
            return (self.num * other.den) // (other.num * self.den)
        else:
            return self.num // (other * self.den)
    
    def __rfloordiv__(self, other) -> int:
        assert type(other) in (int, float, frac), \
            "TypeError: unsupported operand type(s) for //: 'frac' and '{}'".format(type(other))
        assert type(self.num) != complex, \
            "TypeError: Cannot take floor of a fraction with complex"
        if type(other) == frac:
            assert type(other.num) != complex, \
                "TypeError: Cannot take floor of a fraction with complex"
            return (other.num * self.den) // (self.num * other.den)
        else:
            return (other * self.den) // self.num
    
    # %
    def __mod__(self, other):
        assert type(other) in (int, float, frac), \
            "TypeError: unsupported operand type(s) for %: 'frac' and '{}'".format(type(other))
        assert type(self.num) != complex, \
            "TypeError: Cannot mod a fraction with complex"
        if type(other) != frac:
            tmp = frac(other)
        else:
            tmp = other
        assert type(tmp.num) != complex, \
            "TypeError: Cannot mod a fraction with complex"
        return frac((self.num * tmp.den) % (self.den * tmp.den), self.den * tmp.den)
    
    def __rmod__(self, other):
        assert type(other) in (int, float, frac), \
            "TypeError: unsupported operand type(s) for %: 'frac' and '{}'".format(type(other))
        assert type(self.num) != complex, \
            "TypeError: Cannot mod a fraction with complex"
        if type(other) != frac:
            tmp = frac(other)
        else:
            tmp = other
        assert type(tmp.num) != complex, \
            "TypeError: Cannot mod a fraction with complex"
        return frac((tmp.num * self.den ) % (tmp.den * self.num), self.den * tmp.den)
    
    # **
    def __pow__(self, other) -> float:
        assert type(other) in (int, float, frac, complex), \
            "TypeError: unsupported operand type(s) for **: 'frac' and '{}'".format(type(other))
        if type(other) == frac:
            return self.num ** other.calc() / self.den ** other.calc()
        else:
            return self.num ** other / self.den ** other

    def __rpow__(self, other):
        assert type(other) in (int, float, frac, complex), \
            "TypeError: unsupported operand type(s) for **: 'frac' and '{}'".format(type(other))
        if type(other) == frac:
            return other.num ** self.calc() / other.den ** self.calc()
        else:
            return other ** self.calc()
    
    # divmod(self, x)
    def __divmod__(self, x: int) -> tuple:
        assert type(x) in (int, float, frac), \
            "TypeError: can only mod and div frac by int, float or frac"
        return (self // x, self % x)
    
    def __rdivmod__(self, x: int) -> tuple:
        assert type(x) in (int, float, frac), \
            "TypeError: can only mod and div frac by int, float or frac"
        return (x // self, x % self)
    
    # math.ceil(self)
    def __ceil__(self) -> int:
        return int(self.calc()) + 1
    
    # math.floor(self)
    def __floor__(self) -> int:
        assert type(self.num) != complex, \
            "TypeError: can not take floor of complex"
        return int(self.calc())
    
    # comparison
    # !=
    def  __ne__(self, o) -> bool:
        if type(o) in (int, float, frac, complex):
            if type(o) != frac: tmp = frac(o)
            else:               tmp = o
            return self.num != tmp.num or self.den != tmp.den
        else:
            return True

    # ==
    def __eq__(self, o: object) -> bool:
        if type(o) in (int, float, frac, complex):
            if type(o) != frac: tmp = frac(o)
            else:               tmp = o
            return self.num == tmp.num and self.den == tmp.den
        else:
            return False
    
    # >
    def __gt__(self, o: object) -> bool:
        assert type(o) in (int, float, frac), \
            "TypeError: '>' not supported between instances of 'frac' and '{}'".format(type(o))
        assert type(self.num) != complex, \
            "TypeError: '>' not supported between instances of 'frac' with complex and '{}'"\
                .format(type(o))
        if type(o) != frac: tmp = frac(o)
        else:               tmp = o
        return self.num * tmp.den > tmp.num * self.den
    
    # >=
    def __ge__(self, o) -> bool:
        assert type(o) in (int, float, frac), \
            "TypeError: '>=' not supported between instances of 'frac' and '{}'".format(type(o))
        assert type(self.num) != complex, \
            "TypeError: '>=' not supported between instances of 'frac' with complex and '{}'"\
                .format(type(o))
        if type(o) != frac: tmp = frac(o)
        else:               tmp = o
        return self.num * tmp.den >= tmp.num * self.den
    
    # <
    def __lt__(self, o) -> bool:
        assert type(o) in (int, float, frac), \
            "TypeError: '<' not supported between instances of 'frac' and '{}'".format(type(o))
        assert type(self.num) != complex, \
            "TypeError: '<' not supported between instances of 'frac' with complex and '{}'"\
                .format(type(o))
        if type(o) != frac: tmp = frac(o)
        else:               tmp = o
        return self.num * tmp.den < tmp.num * self.den
    
    # <=
    def __le__(self, o) -> bool:
        assert type(o) in (int, float, frac), \
            "TypeError: '<=' not supported between instances of 'frac' and '{}'".format(type(o))
        assert type(self.num) != complex, \
            "TypeError: '<=' not supported between instances of 'frac' with complex and '{}'"\
                .format(type(o))
        if type(o) != frac: tmp = frac(o)
        else:               tmp = o
        return self.num * tmp.den <= tmp.num * self.den
    
    # bit operation
    # &
    def __or__(self, o):
        if type(o) != frac:
            tmp = frac(o)
        else:
            tmp = o
        if type(self.num) == complex:
            if type(tmp.num) == complex:
                return frac((int(self.num.real) | int(tmp.num.real)) + \
                    (int(self.num.imag) | int(tmp.num.imag)) * 1j,
                    self.den | tmp.den
                )
            else:
                return frac((int(self.num.real) | tmp.num) + \
                    int(self.num.imag) * 1j, self.den | tmp.den)
        else:
            if type(tmp.num) == complex:
                return frac((self.num | int(tmp.num.real)) + int(tmp.num.imag) * 1j,
                    self.den | tmp.den
                )
            else:
                return frac(self.num | tmp.num, self.den | tmp.den)
    
    # |
    def __and__(self, o):
        if type(o) == frac:
            tmp = frac(o)
        else:
            tmp = o
        if type(self.num) == complex:
            if type(tmp.num) == complex:
                return frac(int(self.num.real) & int(tmp.num.real) + \
                    (int(self.num.imag) & int(tmp.num.imag)) * 1j,
                    self.den & tmp.den
                )
            else:
                return frac(int(self.num.real) & tmp.num + \
                    int(self.num.imag) * 1j, self.den & tmp.den)
        else:
            if type(tmp.num) == complex:
                return frac(self.num & int(tmp.num.real),
                    self.den & tmp.den
                )
            else:
                return frac(self.num & tmp.num, self.den & tmp.den)
    
    # ^
    def __xor__(self, o):
        assert type(o) in (int, float, complex, frac), \
            "TypeError: unsupported operand type(s) for |: 'frac' and '{}}'".format(type(o))
        if type(o) == frac:
            tmp = frac(o)
        else:
            tmp = o
        if type(self.num) == complex:
            if type(tmp.num) == complex:
                return frac(int(self.num.real) ^ int(tmp.num.real) + \
                    (int(self.num.imag) ^ int(tmp.num.imag)) * 1j,
                    self.den ^ tmp.den
                )
            else:
                return frac(int(self.num.real) ^ tmp.num + \
                    0 ^ int(self.num.imag) * 1j, self.den ^ tmp.den)
        else:
            if type(tmp.num) == complex:
                return frac(self.num ^ int(tmp.num.real) + 0 ^ int(tmp.num.imag) * 1j,
                    self.den ^ tmp.den
                )
            else:
                return frac(self.num ^ tmp.num, self.den ^ tmp.den)

    # other function
    def calc(self) -> float or complex:
        '''Convert to float or complex'''
        return self.num / self.den

    # it works in a complex way
    # please do not modify it if you do not understand how it works
    def reduce(self, nums:tuple):
        '''DO NOT use this method if nothing is wrong'''
        # initialize num
        if type(nums[0]) == frac:
            self.num = nums[0].num
            self.den *= nums[0].den
        elif type(nums[0]) == complex:
            self.den = 1
            if nums[0].imag == 0:
                numstr = str(nums[0].real)
                if str(numstr)[-1] == 0:
                    self.num = int(nums[0].real)
                else:
                    self.num = int(numstr.replace('.', ''))
                    self.den = 10 ** (len(numstr) - numstr.find('.') - 1)
                del numstr
            else:
                numrealstr = str(nums[0].real)
                numimagstr = str(nums[0].imag)
                if numrealstr[-1] == '0':
                    numrealstr = numrealstr[:-1]
                if numimagstr[-1] == '0':
                    numimagstr = numimagstr[:-1]
                if (len(numrealstr) - numrealstr.find('.')) > (len(numimagstr) - numimagstr.find('.')):
                    self.num = int(numrealstr.replace('.', '')) + \
                        int(numimagstr.replace('.', '') + \
                        '0' * (len(numrealstr) - numrealstr.find('.') - \
                        len(numimagstr) + numimagstr.find('.'))) * 1j
                    self.den = 10 ** (len(numrealstr) - numrealstr.find('.') - \
                        len(numimagstr) + numimagstr.find('.'))
                else:
                    self.num = int(numrealstr.replace('.', '')) + \
                        int(numimagstr.replace('.', '') + \
                        '0' * (len(numimagstr) - numimagstr.find('.') - \
                        len(numrealstr) + numrealstr.find('.'))) * 1j
                    self.den = 10 ** (len(numimagstr) - numimagstr.find('.') - \
                        len(numrealstr) + numrealstr.find('.'))
                del numrealstr, numimagstr
        elif type(nums[0]) == float:
            numstr = str(nums[0])
            if str(numstr)[-1] == 0:
                self.num = int(nums[0].real)
            else:
                self.num = int(numstr.replace('.', ''))
                self.den = 10 ** (len(numstr) - numstr.find('.' )- 1)
            del numstr
        else:
            self.num = nums[0]
            self.den = 1
        
        # initialize den
        for num in nums[1:]:
            if type(num) == float:
                if num % 1:
                    numstr = str(num)
                    if numstr[-1] == '0':
                        numstr = numstr[:-1]
                    self.num *= 10 ** (len(numstr) - numstr.find('.') - 1)
                    self.den *= int(numstr.replace('.', ''))
                    del numstr
                else:
                    self.den *= int(numstr)
            elif type(num) == complex:
                # to integer
                if (num.real % 1 or num.imag % 1):
                    numrealstr = str(num.real)
                    numimagstr = str(num.imag)
                    if numrealstr[-1] == '0':
                        numrealstr = numrealstr[:-1]
                    if numimagstr[-1] == '0':
                        numimagstr = numimagstr[:-1]
                    if (len(numrealstr) - numrealstr.find('.')) > (len(numimagstr) - numimagstr.find('.')):
                        self.den *= int(numrealstr.replace('.', '')) + \
                            int(numimagstr.replace('.', '') + \
                            '0' * (len(numrealstr) - numrealstr.find('.') - \
                            len(numimagstr) + numimagstr.find('.'))) * 1j
                        self.num *= 10 ** (len(numrealstr) - numrealstr.find('.') - \
                            len(numimagstr) + numimagstr.find('.'))
                    else:
                        self.den *= int(numrealstr.replace('.', '')) + \
                            int(numimagstr.replace('.', '') + \
                            '0' * (len(numimagstr) - numimagstr.find('.') - \
                            len(numrealstr) + numrealstr.find('.'))) * 1j
                        self.num *= 10 ** (len(numimagstr) - numimagstr.find('.') - \
                            len(numrealstr) + numrealstr.find('.'))
                    del numrealstr, numimagstr
                else:
                    # package den
                    self.den *= num
                # to integer if no longer complex
                if self.den.imag == 0:
                    self.den = int(self.den.real)
            elif type(num) == int:
                self.den *= num
            elif type(num) == frac: # if num is frac
                self.num *= num.den # if is frac, no need to do integer convertion, just multiply is ok
                self.den *= num.num
                # if num.num is complex, check if no longer complex
                if type(num.num) == complex:
                    if self.den.imag == 0: # no longer complex, convert to integer
                        self.den = int(self.den.real)
        
        # realize den
        if type(self.den) == complex:
            self.num *= self.den.real - self.den.imag * 1j
            self.den = int(self.den.real ** 2 + self.den.imag ** 2)
            if self.num.imag == 0: self.num = int(self.num.real)
        
        # positivize den
        if self.den < 0:
            self.num *= -1
            self.den *= -1
        
        # starts reducing
        if self.num == 0:
            self.den = 1
        else:
            if type(self.num) == complex and (1 not in (abs(self.num.real), abs(self.num.imag), self.den)):
                tmpdiv = frac.getmaxdiv((int(abs(self.num.real)), int(abs(self.num.imag)), int(self.den)))
                self.num = self.num.real // tmpdiv + self.num.imag // tmpdiv
                self.den //= tmpdiv
                del tmpdiv
            elif 1 not in (abs(self.num), self.den):
                tmpdiv = frac.getmaxdiv((abs(self.num), self.den))
                self.num //= tmpdiv
                self.den //= tmpdiv
                del tmpdiv
        
        # return
        return self
    
    def getmaxdiv(nums):
        if len(nums) == 1:
            return nums[0]
        else:
            nums = sorted(nums)
            output = [nums[0]]
            for num in nums[1:]:
                num = num % nums[0]
                if num:
                    output.append(num)
            del num
            output = tuple(output)
            return frac.getmaxdiv(output)
 
