import heapq


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.tweets.get(userId):
            self.tweets[userId] = [(self.time, tweetId)]
        else:
            self.tweets[userId].append((self.time, tweetId))

        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        feed_num = 10
        feed = []
        news_feed = []
        for follow in self.follows.get(userId, set()):
            for tweet in self.tweets.get(follow, []):
                feed.append(tweet)

        for tweet in self.tweets.get(userId, []):
            feed.append(tweet)

        heapq.heapify(feed)
        for _ in range(feed_num):
            if not feed:
                break
            news_feed.append(heapq.heappop(feed)[1])

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if not self.follows.get(followerId):
            self.follows[followerId] = {followeeId}
        else:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.follows.get(followerId):
            self.follows[followerId].remove(followeeId)
