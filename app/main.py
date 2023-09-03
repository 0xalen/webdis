import sys
import time
from pathlib import Path

import pandas as pd
import streamlit as st

project_dir = Path().cwd()
sys.path.insert(0, str(project_dir))

from app.ui.dissasemble_button import extract_href_links, get_content, extract_js_scripts, extract_headers


def launch():
    st.set_page_config(layout="wide")
    st.container()
    st.title("Web Disassembler")

    col1, _, col2 = st.columns([5, 1, 7])
    with col2:
        st.subheader("Elements to detect")
        c1, c2 = st.columns(2)
        with c1:
            headers = st.checkbox(label="Headers")
            href_links = st.checkbox(label="Links")
            media = st.checkbox(label="Media")
            html_froms = st.checkbox(label="Forms")
            pdf_files = st.checkbox(label="Files (PDF)")
            txt_files = st.checkbox(label="Files (TXT)")

        with c2:
            css_stylesheets = st.checkbox(label="Stylesheets (CSS)")
            js_scripts = st.checkbox(label="Scripts (JS)")
            php_scripts = st.checkbox(label="Scripts (PHP)")
            sql_scripts = st.checkbox(label="Scripts (SQL)")

    with col1:
        st.subheader("Disassemble website")
        website_url = st.text_input(
            label="website_url"
        )
        c1, c2 = st.columns(2)
        with c2:
            disassemble_button = st.button(
                label="Dissasemble :zap:",
                use_container_width=True,
            )
    st.divider()
    if website_url != "" and disassemble_button:
        start_time = time.time()
        with st.spinner("Please, wait while I process your request..."):
            disassembly_output = st.text_area(
                label="WebDis response",
                value=get_content(website_url)
            )

        finish_time = time.time()
        execution_time = round(finish_time - start_time, 6)
        st.success(f"Request processed in {execution_time} seconds.")
    else:
        disassembly_output = st.text_area(
            label="WebDis response",
            disabled=True
        )

    if disassembly_output:
        if headers:
            header_list = extract_headers(disassembly_output)
            st.table(pd.DataFrame(
                header_list,
                columns=["Header"]
                )
            )
        else:
            st.write("No href links found")

        if href_links:
            links_list = extract_href_links(disassembly_output)
            st.table(pd.DataFrame(
                links_list,
                columns=["Link"]
                )
            )
        else:
            st.write("No href links found")

        if js_scripts:
            js_scripts_list = extract_js_scripts(disassembly_output)
            st.table(pd.DataFrame(
                js_scripts_list,
                columns=["Script"]
                )
            )
        else:
            st.write("No js scripts found")


    # media
    # html_froms
    # pdf_files
    # txt_files
    # css_stylesheets
    # js_scripts
    # php_scripts
    # sql_scripts


if __name__ == "__main__":
    launch()

