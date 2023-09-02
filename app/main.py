import sys
import time
from pathlib import Path

import streamlit as st

project_dir = Path().cwd()
sys.path.insert(0, str(project_dir))


def launch():
    st.set_page_config(layout="wide")
    st.container()
    st.title("Web Disassembler")

    col1, _, col2 = st.columns([5, 1, 7])
    with col2:
        st.subheader("Elements to detect")

    with col1:
        st.subheader("Disassemble website")
        website_url = st.text_area(
            label="website_url"
        )
        c1, c2 = st.columns(2)
        with c2:
            dissasemble_button = st.button(
                label="Dissasemble :zap:",
                use_container_width=True,
            )
        st.divider()
        if website_url != "" and dissasemble_button:
            start_time = time.time()
            with st.spinner("Please, wait while I process your request..."):
                dissasembly_output = st.text_area(
                    label="WebDis response",
                    value=dissasemble_website(website_url, element_list),
                )
            finish_time = time.time()
            execution_time = round(finish_time - start_time, 6)
            st.success(f"Request processed in {execution_time} seconds.")
        else:
            dissasembly_output = st.text_area(
                label="WebDis response",
                disabled=True
            )


if __name__ == "__main__":
    launch()

