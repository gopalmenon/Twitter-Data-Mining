hours = c(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)
trump.tweets.by.hour = c(261, 241, 179, 182, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 201, 36, 24, 241, 244, 66, 64, 228, 265, 268)
clinton.tweets.by.hour = c(235, 250, 113, 245, 262, 262, 235, 222, 188, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 14, 13, 8, 201, 246)
plot(hours, trump.tweets.by.hour, type='l', xlab='Hour of the day', ylab='Number of tweets', col='red', main='Number of tweets by hour of the day', ylim=c(0, 350))
lines(hours, clinton.tweets.by.hour, col='blue')
legend(x=18, y=350, legend=c('Trump', 'Clinton'),col=c('red','blue'), lwd=3, lty=1)

