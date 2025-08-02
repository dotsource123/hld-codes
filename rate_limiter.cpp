#include <bits/stdc++.h>
using namespace std;

class rateLimiter{
    public:
    int maxRequestsAllowed;
    int timeWindow;
    int count=0;
    int prevTime=0;

    rateLimiter(int m,int t){
        maxRequestsAllowed=m;
        timeWindow=t;
    }

    bool isAllowed(int user_Id,int timeStamp){
        if(timeStamp>=prevTime+timeWindow){
            count=1;
        }
        else{
            count++;
            if(count>maxRequestsAllowed){
                return false;
            }
        }
        return true;
    }
};