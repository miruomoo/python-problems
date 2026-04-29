class Twitter:

    def __init__(self):
        self.users = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list) #(time, tweetId)
        self.time = 0 #negative

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.users[userId].add(userId)

        for following in self.users[userId]:
            if following in self.tweets:

                i = len(self.tweets[following]) - 1
                time, tweetId = self.tweets[following][i]

                minHeap.append([time, tweetId, following, i - 1])
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:

            time, tweetId, following, i = heapq.heappop(minHeap)
            res.append(tweetId)
            if i >= 0:
                time, tweetId = self.tweets[following][i]
                heapq.heappush(minHeap, [time, tweetId, following, i - 1])

        return res

            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
