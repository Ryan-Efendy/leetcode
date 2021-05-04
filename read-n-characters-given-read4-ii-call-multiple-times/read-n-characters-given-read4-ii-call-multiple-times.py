# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.tmpBuf = [''] * 4
        self.curr_used = 0 # last used location/ptr from prev read call
        self.curr_read = 0
        self.EOF = False
    
    def read(self, destBuf: List[str], n: int) -> int:
        '''
        same as Read N Characters Given Read4 except it needs to resume for multiple calls
        '''
        readSoFar = 0
        
        while readSoFar < n and not self.EOF:
            if self.curr_used == self.curr_read:
                self.curr_read = read4(self.tmpBuf)
                self.curr_used = 0
                if self.curr_read == 0:
                    self.EOF = True
            else:
                delta = min(self.curr_read - self.curr_used, n - readSoFar)
                destBuf[readSoFar : readSoFar + delta] = self.tmpBuf[self.curr_used : self.curr_used + delta]
                readSoFar += delta
                self.curr_used += delta
        return readSoFar