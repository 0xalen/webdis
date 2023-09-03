import sys
import time
from pathlib import Path

import pandas as pd
import streamlit as st

project_dir = Path().cwd()
sys.path.insert(0, str(project_dir))

from app.ui.dissasemble_button import extract_href_links, get_content, extract_js_scripts, extract_headers, \
    extract_css_stylesheets, extract_html_form, extract_img_media, extract_php_scripts, extract_sql_scripts, \
    extract_pdf_files, extract_txt_files, extract_csv_files


def launch():
    st.set_page_config(layout="wide")
    st.container()
    st.title("Web Disassembler")

    col1, _, col2 = st.columns([5, 1, 7])
    with col2:
        st.subheader("Elements to detect")
        select_all = st.checkbox(label="Select all")
        st.divider()
        c1, c2 = st.columns(2)
        if select_all:
            with c1:
                headers = st.checkbox(label="Headers", value=True)
                href_links = st.checkbox(label="Links", value=True)
                img_media = st.checkbox(label="Media (IMG)", value=True)
                html_forms = st.checkbox(label="Forms (HTML)", value=True)
                pdf_files = st.checkbox(label="Files (PDF)", value=True)
                txt_files = st.checkbox(label="Files (TXT)", value=True)
                csv_files = st.checkbox(label="Files (CSV)", value=True)

            with c2:
                css_stylesheets = st.checkbox(label="Stylesheets (CSS)", value=True)
                js_scripts = st.checkbox(label="Scripts (JS)", value=True)
                php_scripts = st.checkbox(label="Scripts (PHP)", value=True)
                sql_scripts = st.checkbox(label="Scripts (SQL)", value=True)
        else:
            with c1:
                headers = st.checkbox(label="Headers")
                href_links = st.checkbox(label="Links")
                img_media = st.checkbox(label="Media (IMG)")
                html_forms = st.checkbox(label="Forms (HTML)")
                pdf_files = st.checkbox(label="Files (PDF)")
                txt_files = st.checkbox(label="Files (TXT)")
                csv_files = st.checkbox(label="Files (CSV)")

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
            label="Website content",
            disabled=True
        )

    if disassembly_output:
        if href_links:
            links_list = extract_href_links(disassembly_output)
            if links_list:
                st.table(pd.DataFrame(
                    links_list,
                    columns=["Link"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["Link"]))

        if js_scripts:
            js_scripts_list = extract_js_scripts(disassembly_output)
            if js_scripts_list:
                st.table(pd.DataFrame(
                    js_scripts_list,
                    columns=["JS Script"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["JS Script"]))

        if php_scripts:
            php_scripts_list = extract_php_scripts(disassembly_output)
            if php_scripts_list:
                st.table(pd.DataFrame(
                    php_scripts_list,
                    columns=["PHP Script"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["PHP Script"]))

        if sql_scripts:
            sql_scripts_list = extract_sql_scripts(disassembly_output)
            if sql_scripts_list:
                st.table(pd.DataFrame(
                    sql_scripts_list,
                    columns=["SQL Script"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["SQL Script"]))

        if pdf_files:
            pdf_files_list = extract_pdf_files(disassembly_output)
            if pdf_files_list:
                st.table(pd.DataFrame(
                    pdf_files_list,
                    columns=["PDF Files"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["PDF File"]))

        if txt_files:
            txt_files_list = extract_txt_files(disassembly_output)
            if txt_files_list:
                st.table(pd.DataFrame(
                    txt_files_list,
                    columns=["TXT Files"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["TXT File"]))

        if csv_files:
            csv_files_list = extract_csv_files(disassembly_output)
            if csv_files_list:
                st.table(pd.DataFrame(
                    csv_files_list,
                    columns=["CSV Files"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["CSV File"]))

        if html_forms:
            html_forms_list = extract_html_form(disassembly_output)
            if html_forms_list:
                st.table(pd.DataFrame(
                    html_forms_list,
                    columns=["HTML Form"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["HTML Form"]))

        if img_media:
            img_media_list = extract_img_media(disassembly_output)
            if img_media_list:
                st.table(pd.DataFrame(
                    img_media_list,
                    columns=["IMG Media"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["IMG Media"]))

        if css_stylesheets:
            css_stylesheets_list = extract_css_stylesheets(disassembly_output)
            if css_stylesheets_list:
                st.table(pd.DataFrame(
                    css_stylesheets_list,
                    columns=["Style Sheets"]
                    )
                )
            else:
                st.table(pd.DataFrame([], columns=["Style Sheets"]))

        if headers:
            header_list = extract_headers(disassembly_output)
            if header_list:
                st.table(pd.DataFrame(
                    header_list,
                    columns=["Header"]
                    )
                )

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

