import streamlit as st
from errors import FailedToDownloadException, EmptyStringException, InvalidURL
from utils import download_image


st.title("Image classifier")
image_url = st.text_input("Image URL")

if st.button("Classify!", key="enter"):
    try:
        img = download_image(image_url)
        st.image(img)
        error = ""

    except FailedToDownloadException:
        error = "Oops, something went wrong"
    except InvalidURL:
        error = "Invalid URL"
    except EmptyStringException:
        error = ""

if error:
    st.error(error)
