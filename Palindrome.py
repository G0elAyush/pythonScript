class Palindrome:
    def next_smallest_palindrome(self,number):
        print('Given number = %d'  %(number))
        if not isinstance(number,int):
            return print('Input must be number')
        number = str(number)
        if number =='0':
            number ='00'
        size = len(number)
        center = number[(size//2)] if size%2 else ''
        left = number[:size//2]
        right = left[::-1]
        palindrome= left + center + right
        if palindrome > number:
            return print('next palindrome = %s ' %(palindrome))
        else:
            if center:
                if center < '9':
                    center = str(int(center) + 1)
                    palindrome = left + center + right
                    return print('next palindrome = %s ' %(palindrome))
                else:
                    center = '0'

            if left == len(left) * '9':
                palindrome = '1' + '0' *(len(number)-1) +'1'
                return print('next palindrome = %s ' %(palindrome))
            else:
                left = self.inc(left)
                palindrome = left + center + left[::-1]
                return print('next palindrome = %s ' %(palindrome))

    def inc(self,left):
        leftlist = list(left)
        last = len(leftlist)-1
        while leftlist[last] == '9':
            leftlist[last] = '0'
            last -= 1
        leftlist[last] = str(int(leftlist[last])+1)
        return "".join(leftlist)
if __name__=='__main__':
    p=Palindrome()
    p.next_smallest_palindrome(12912)
    p.next_smallest_palindrome(000)
    p.next_smallest_palindrome(999999999)
    p.next_smallest_palindrome(99)
    p.next_smallest_palindrome(123456)
    p.next_smallest_palindrome(12345)
    p.next_smallest_palindrome(12321)
    p.next_smallest_palindrome(12312)
    p.next_smallest_palindrome(11)
    p.next_smallest_palindrome(9900)
    p.next_smallest_palindrome(12921)
    p.next_smallest_palindrome(12921)
