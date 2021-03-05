import streamlit as st
from errors import FailedToDownloadException, EmptyStringException, InvalidURL
from utils import download_image, run_detector


st.title("Image classifier")
image_url = st.text_input("Image URL")
error = ""

if st.button("Classify!", key="enter"):
    try:
        img = download_image(image_url)
        st.image(img, width=200)
        error = ""
        image_with_bounding_boxes = run_detector(img)
        st.image(image_with_bounding_boxes, width=200)

    except FailedToDownloadException:
        error = "Oops, something went wrong"
    except InvalidURL:
        error = "Invalid URL"
    except EmptyStringException:
        error = ""

if error:
    st.error(error)
