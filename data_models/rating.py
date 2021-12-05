class Rating:
    def __init__(self, userId, movieId, rating, timestamp) -> None:
        self.__userId = userId
        self.__movieId = movieId
        self.__rating = rating
        self.__timestamp = timestamp
