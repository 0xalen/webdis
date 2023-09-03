from app.dissasembler.managers import DisassemblerManager


def get_content(url):
    href_list = DisassemblerManager.download_content(url)
    return href_list


def extract_headers(site_content):
    header_list = DisassemblerManager.extract_headers(site_content)
    return header_list


def extract_href_links(site_content):
    links_list = DisassemblerManager.extract_href_links(site_content)
    return links_list


def extract_js_scripts(site_content):
    js_scripts_list = DisassemblerManager.extract_js_scripts(site_content)
    return js_scripts_list


