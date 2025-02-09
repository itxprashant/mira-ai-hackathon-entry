import streamlit as st
import json
from main import return_response, return_response_based_on_watched, return_response_based_on_incident

st.sidebar.success("Select The method")

def intro():
    st.title("💬 Movie, Web Series and Book Recommender")
    st.write(
        "Hi, I am an AI-based movie/book recommender. "
        "Just let me know you better so that I can personalize the recommendations.😉"
    )


    st.markdown("## Mood? 🤔")
    mood = st.selectbox(
        "Select your mood",
        ["No mood preference", "😊 Happy", "😢 Sad", "😃 Excited", "😡 Angry", "😲 Surprised", "😨 Fearful", "🤢 Disgusted"],
    )


    genre_list = ["Action", "Adventure", "Comedy", "Crime and Mystery", "Fantasy", "Historical",
              "Horror", "Romance", "Satire", "Sci-fi", "Speculative", "Thriller", "Others"]
    st.markdown("## Genre List")
    selected_genres = [None for _ in genre_list]
    cols = st.columns(4)
    for i, genre in enumerate(genre_list):
        with cols[i % 4]:
            selected_genres[i] = st.checkbox(genre, value=False)
    

    language_list = ["English", "Hindi", "Korean", "Japanese", "French", "Spanish", "Others"]
    languages = [None for _ in language_list]
    st.markdown("## Language")
    lang_cols = st.columns(4)
    for i, language in enumerate(language_list):
        with lang_cols[i % 4]:
            languages[i] = st.checkbox(language, value=False, key=language)


    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.text_input("Describe more... (optional)")
    if st.button("Submit"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            st.markdown(f"""Genres given: {', '.join([genre_list[i] for i in range(len(genre_list)) if selected_genres[i]])},
                        Mood: {mood}""")
            st.markdown(f"""Languages:{', '.join([language_list[i] for i in range(len(language_list)) if languages[i]])}""")

        stream = return_response(prompt, [genre_list[i] for i in range(len(genre_list)) if selected_genres[i]],
                                mood,
                                [language_list[i] for i in range(len(language_list)) if languages[i]])

        with st.chat_message("assistant"):
            response = st.write(stream["result"])

        st.session_state.messages.append({"role": "assistant", "content": response})


def previously_watched_based_response():
        st.title("Previously watched/read based response")
        already_watched = st.text_area("""Enter the movies/books/web series you've already watched similar to 
                                       which you want the recommendation""", height=100)

        if st.button("Get Recommendations"):
            stream = return_response_based_on_watched(already_watched)
            st.write(stream["result"])


def incident_based_response():
        st.title("Incident based response")
        st.markdown("Any incident happened with you? Let me know and I will recommend you the movie/book based on that.😉")
        already_watched = st.text_area("""Enter the incident""", height=100)

        if st.button("Get Recommendations"):
            stream = return_response_based_on_watched(already_watched)
            st.write(stream["result"])


page_names_to_funcs = {
    "Basic mode": intro,
    "Previously watched/read based response": previously_watched_based_response,
    "Recommend based on incident": incident_based_response,
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()