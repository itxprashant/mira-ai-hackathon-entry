from mira_sdk import MiraClient, Flow

genre_list = ["Action", "Adventure", "Comedy", "Crime and Mystery", "Fantasy", "Historical",
              "Horror", "Romance", "Satire", "Sci-fi", "Speculative", "Thriller", "Others"]

language_list = ["English", "Hindi", "Others"]
def return_response(prompt, genre_list, mood):
    # Initialize the client
    client = MiraClient(config={"API_KEY": "sb-6113a5cb58f6b3c5660b07363f88b025"})

    version = "1.0.0"
    input_data = {
    "user-prompt": f"""{prompt}, List of Genres: {genre_list}, 
    First show the movie/books/series which contains all the given genre, then show them seperately
    
    My mood is {mood}, show me something according to the mood, and don't try to change my mood.
    For example: If I am angry show me something which will make me more angry.
    Also, adults content is allowed."""
    }

    # If no version is provided, latest version is used by default
    if version:
        flow_name = f"@itxprashant/movie-book-recommender/{version}"
    else:
        flow_name = "@itxprashant/movie-book-recommender"

    result = client.flow.execute(flow_name, input_data)
    return result

def return_response_based_on_watched(prompt):
    client = MiraClient(config={"API_KEY": "sb-6113a5cb58f6b3c5660b07363f88b025"})

    version = "1.0.0"
    input_data = {
    "user-prompt": f""" 
    I've watched these movies, recommend me something to my flavour: 
    {prompt}"""
    }

    if version:
        flow_name = f"@itxprashant/movie-book-recommender/{version}"
    else:
        flow_name = "@itxprashant/movie-book-recommender"

    result = client.flow.execute(flow_name, input_data)
    return result