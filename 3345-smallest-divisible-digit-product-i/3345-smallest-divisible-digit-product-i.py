class Solution(object):
    def smallestNumber(self, n, t):
        num = n

        while True:
            multiply = 1
            n = num

            while n > 0:
                digit = n % 10
                multiply *= digit

                if multiply == 0:
                    break

                n //= 10

            if multiply % t == 0:
                return num

            num += 1