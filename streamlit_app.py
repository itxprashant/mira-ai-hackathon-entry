import streamlit as st
import json
from main import return_response, genre_list, return_response_based_on_watched

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

    st.markdown("## Genre List")
    selected_genres = [None for _ in genre_list]
    cols = st.columns(4)
    for i, genre in enumerate(genre_list):
        with cols[i % 4]:
            selected_genres[i] = st.checkbox(genre, value=False)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Describe more... (optional)"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            st.markdown(f"""Genres given: {', '.join([genre_list[i] for i in range(len(genre_list)) if selected_genres[i]])},
                        Mood: {mood}""")

        stream = return_response(prompt, [genre_list[i] for i in range(len(genre_list)) if selected_genres[i]],
                                mood)

        with st.chat_message("assistant"):
            response = st.write(stream["result"])

        if advanced_features:
            st.sidebar.markdown("### Recommendations")
            st.sidebar.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

def previously_watched_based_response():
        st.title("Advanced Features")
        st.markdown("You can customize the recommendations by selecting the following options:")
        st.markdown("### Movies/Books/Web Series I've already watched")
        already_watched = st.text_area("""Enter the movies/books/web series you've already watched similar to 
                                       which you want the recommendation""", height=100)

        if st.button("Get Recommendations"):
            stream = return_response_based_on_watched(already_watched)
            st.write(stream["result"])


page_names_to_funcs = {
    "Basic mode": intro,
    "Previously watched/read based response": previously_watched_based_response,
    # "Mapping Demo": mapping_demo,
    # "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()