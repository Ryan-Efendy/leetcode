"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, destBuf: List[str], n: int) -> int:
        '''
        https://www.youtube.com/watch?v=x7pg4cTHu4g


        '''
        tmpBuf = [''] * 4 # tmpBuf keep fetching and transfer to destBuf
        readSoFar = 0
        EOF = False
        # terminate when reach EOF or meet the number of required chars
        # otherwise keep replenshing tmpBuf & transfer to target/destBuf
        while readSoFar < n and not EOF:
            curr_read = read4(tmpBuf)
            delta = min(curr_read, n-readSoFar) # how many to transfer from tmp to destBuf
            destBuf[readSoFar : readSoFar + delta] = tmpBuf[:delta] # the ACTUAL transfer 
            readSoFar += delta
            if curr_read < 4:
                EOF = True
        return readSoFar

        