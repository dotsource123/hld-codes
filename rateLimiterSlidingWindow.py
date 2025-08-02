from collections import deque
from typing import Dict

class RateLimiter:
    def __init__(self,rate_limit:int,window_size:int):
        self.rate_limit=rate_limit
        self.window_size=window_size
        self.user_requests: Dict[int,deque[int]]={}

    def is_allowed(self,user_id:int,timestamp:int)->bool:
        if user_id not in self.user_requests:#if the id is not there
            self.user_requests[user_id]=deque()#initialise with a deque

        q=self.user_requests[user_id]

        while q and q[0]<=timestamp-self.window_size:
            q.popleft()

        if len(q)>=self.rate_limit:
            return False
        
        else:
            q.append(timestamp)
            return True