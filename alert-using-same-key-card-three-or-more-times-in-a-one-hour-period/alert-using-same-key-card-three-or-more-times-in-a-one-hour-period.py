class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times = defaultdict(list)

        for i in range(len(keyName)):
            name = keyName[i]
            time = keyTime[i]
            t = time.split(':')
            h = int(t[0])
            m = int (t[1])
            times[name].append(h*60+m)

        res = []

        for name in times:
            time_list = sorted(times[name])
            queue = collections.deque()
            
            for time in time_list:
                queue.append(time)
                
                while time - queue[0] > 60:
                    queue.popleft()

                if len(queue) >= 3:
                    res.append(name)
                    break

        return sorted(res)
