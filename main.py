import streamlit as st
from scrape import (scrape_website,extract_body_content,clean_body_content,split_dom_content)


st.title("Ai Web Scrapper")
url = st.text_input("Enter a Website Url")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("View Dom Content"):
        st.text_area("Dom Content", cleaned_content, height = 300)


if "dom_content"  in st.session_state:
    prase_description= st.text_area("Describe what you want to prase?")
    if st.button("Prase Content"):
        if prase_description:
            st.write("Prasing the content")

            dom_chunks  = split_dom_content(st.session_state.dom_content)
            

