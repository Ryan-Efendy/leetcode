# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
        
import concurrent,asyncio
class Solution:
    def __init__(self):
        self.ret=set()
        self.start=None
        asyncio.set_event_loop(asyncio.new_event_loop()) # this line is necessary because leetcode reasons?
    async def recursion(self,url):
        if url.split("/")[2]!=self.start or url in self.ret:return
        self.ret.add(url)
        with concurrent.futures.ThreadPoolExecutor() as pool: # we need a new thread here because getUrls is not asynchronus but 'atomic' and blocking.
            urls= await asyncio.get_running_loop().run_in_executor(pool,lambda:self.parserobj.getUrls(url))
        await asyncio.gather(*(self.recursion(url) for url in urls if url not in self.ret))
        
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.parserobj=htmlParser
        self.start=startUrl.split("/")[2]
        asyncio.run(self.recursion(startUrl))
        return self.ret