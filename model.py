import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
ratings = pd.read_csv("dataset/ratings.csv")
movies = pd.read_csv("dataset/movies.csv")

# Merge
data = ratings.merge(movies, on="movieId")

# Create user-movie matrix
user_movie_matrix = data.pivot_table(
    index="title",
    columns="userId",
    values="rating"
).fillna(0)

# Similarity matrix
similarity = cosine_similarity(user_movie_matrix)

similarity_df = pd.DataFrame(
    similarity,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)

# Recommendation function
def recommend(movie_name):
    movie_name = movie_name.strip()

    if movie_name not in similarity_df.index:
        return ["Movie not found"]

    scores = similarity_df[movie_name].sort_values(ascending=False)[1:6]
    return list(scores.index)


# TEST BLOCK (IMPORTANT)
if __name__ == "__main__":
    print(recommend("Toy Story (1995)"))