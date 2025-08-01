import time

class TokenBucket:
    def __init__(self,capacity,fill_rate):
        self.capacity=capacity
        self.fill_rate=fill_rate
        self.tokens=capacity
        self.last_time=time.time()

    def allow_request(self,tokens=1):
        now=time.time()
        time_passed=now-self.last_time
        self.tokens=min(self.capacity,self.tokens+time_passed*self.fill_rate)
        self.last_time=now

        if self.tokens>=tokens:
            self.tokens-=tokens
            return True
        return False


limiter=TokenBucket(capacity=10,fill_rate=1)

for _ in range(15):
    print(limiter.allow_request())
    time.sleep(0.1)

time.sleep(5)
print(limiter.allow_request)