from mira_sdk import MiraClient, Flow



client = MiraClient(config={"API_KEY": "sb-6113a5cb58f6b3c5660b07363f88b025"})

def return_response(prompt, genre_list, mood, languages):
    # Initialize the client

    version = "1.0.0"
    input_data = {
    "user-prompt": f"""{prompt}, List of Genres: {genre_list}, 
    First show the movie/books/series which contains all the given genre, then show them seperately
    
    My mood is {mood}, show me something according to the mood, and don't try to change my mood.
    For example: If I am angry show me something which will make me more angry.
    Also, adults content is allowed.
    
    Languages: {languages}"""
    }


    # If no version is provided, latest version is used by default
    if version:
        flow_name = f"@itxprashant/movie-book-recommender/{version}"
    else:
        flow_name = "@itxprashant/movie-book-recommender"

    result = client.flow.execute(flow_name, input_data)
    return result

def return_response_based_on_watched(prompt):

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


def return_response_based_on_incident(prompt):

    version = "1.0.0"
    input_data = {
    "user-prompt": f""" 
    The following incident happened with me, can you recommend me some movie/book in which the same incident happened:
    {prompt}
    (Don't try to change my mood or heal it, just recommend me the movie/book in which the same incident happened)"""
    }

    if version:
        flow_name = f"@itxprashant/movie-book-recommender/{version}"
    else:
        flow_name = "@itxprashant/movie-book-recommender"

    result = client.flow.execute(flow_name, input_data)
    return result