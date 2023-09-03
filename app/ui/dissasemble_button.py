from app.disassembler.managers import DisassemblerManager


def get_content(url):
    site_content = DisassemblerManager.download_content(url)
    return site_content


def extract_headers(site_content):
    element_list = DisassemblerManager.extract_headers(site_content)
    return element_list


def extract_href_links(site_content):
    element_list = DisassemblerManager.extract_href_links(site_content)
    return element_list


def extract_js_scripts(site_content):
    element_list = DisassemblerManager.extract_js_scripts(site_content)
    return element_list


def extract_css_stylesheets(site_content):
    element_list = DisassemblerManager.extract_css_stylesheets(site_content)
    return element_list


def extract_html_form(site_content):
    element_list = DisassemblerManager.extract_html_form(site_content)
    return element_list


def extract_img_media(site_content):
    element_list = DisassemblerManager.extract_img_media(site_content)
    return element_list


def extract_php_scripts(site_content):
    element_list = DisassemblerManager.extract_php_scripts(site_content)
    return element_list


def extract_sql_scripts(site_content):
    element_list = DisassemblerManager.extract_sql_scripts(site_content)
    return element_list


def extract_pdf_files(site_content):
    element_list = DisassemblerManager.extract_pdf_files(site_content)
    return element_list


def extract_txt_files(site_content):
    element_list = DisassemblerManager.extract_txt_files(site_content)
    return element_list


def extract_csv_files(site_content):
    element_list = DisassemblerManager.extract_csv_files(site_content)
    return element_list



