import streamlit as st
from errors import FailedToDownloadException, EmptyStringException, InvalidURL
from utils import download_image, predict_label


st.title("Image classifier")
image_url = st.text_input("Image URL")

if st.button("Classify!", key="enter"):
    try:
        img = download_image(image_url)
        st.image(img, width=200)
        error = ""
        label = predict_label(img)
        st.info(
            "{object_type}: {confidence_rate}%".format(
                object_type=label[1], confidence_rate=round(label[2] * 100, 2)
            )
        )

    except FailedToDownloadException:
        error = "Oops, something went wrong"
    except InvalidURL:
        error = "Invalid URL"
    except EmptyStringException:
        error = ""

if error:
    st.error(error)
