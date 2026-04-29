class Twitter:

    def __init__(self):
        self.users = collections.defaultdict(set) # user -> set(followees)
        self.tweets = collections.defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        for tweet in self.tweets[userId]:
            maxHeap.append(tweet)

        for followee in self.users[userId]:
            for tweet in self.tweets[followee]:
                maxHeap.append(tweet)

        heapq.heapify(maxHeap)
        for i in range(10):
            if not maxHeap:
                break
            res.append(heapq.heappop(maxHeap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
