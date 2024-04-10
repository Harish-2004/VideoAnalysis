import streamlit as st
import json
import pandas as pd
from moviepy.editor import VideoFileClip
from main2 import main2
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def main():
    st.title("Upload a Video File and Display JSON Output")

    uploaded_file = st.file_uploader("Upload video file", type=["mp4"])

    if uploaded_file is not None:
        # Process the uploaded file
        video_info = main2(uploaded_file)
        print("video_info",video_info)
        if video_info is not None:
            st.success("Video processed successfully!")
            # Convert JSON data to DataFrame
            flat_video_info = flatten_dict(video_info)
            # Convert flattened dictionary to DataFrame
            df = pd.DataFrame.from_dict(flat_video_info, orient='index', columns=['Value'])
            # Display DataFrame as a table
            #df = pd.DataFrame.from_dict(video_info, orient='index', columns=['Value'])
            # Display DataFrame as a table
            st.table(df)
        else:
            st.error("Please upload a file.")

if __name__ == "__main__":
    main()
