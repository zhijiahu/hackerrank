
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        x = 1
        for i in range(n-1):
            x = self.count(x)

        return str(x)

    def count(self, n):
        k = str(n)
        count = 0
        prev_c = k[0]

        result = ''

        for i, curr_c in enumerate(k):
            if prev_c != curr_c:
                result += self.say(count, prev_c)
                count = 1
            else:
                count += 1

            prev_c = curr_c

        # compute the last repetition
        result += self.say(count, prev_c)

        return int(result)

    def say(self, count, number):
        return str(count) + number

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);

            ret = Solution().countAndSay(n)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
