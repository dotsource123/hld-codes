#include <bits/stdc++.h>
using namespace std;

class rateLimiter{
    public:
    int requestLimit;
    int timeWindow;
    unordered_map<int,int> mp;
    int prevWindowTime;
    rateLimiter(int requestLimit,int timeWindow){
        this->requestLimit=requestLimit;
        this->timeWindow=timeWindow;
        prevWindowTime=timeWindow;
    }

    bool isAllowed(int userId,int timeStamp){
        if(timeStamp<=prevWindowTime){
            if(mp[userId]==requestLimit){
                return false;
            }
            else{
                mp[userId]++;
                return true;
            }
        }
        else{
            while (prevWindowTime<timeStamp)
            {
                prevWindowTime+=timeWindow;
            }
            mp[userId]=1;
            return true;
        }
    }
};