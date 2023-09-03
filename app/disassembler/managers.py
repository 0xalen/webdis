from app.disassembler.patterns import TAGS_REGEX, HEADERS_REGEX, A_HREF_REGEX, LINK_HREF_REGEX, SCRIPT_REGEX, \
    CSS_STYLESHEETS_REGEX, HTML_FORM_REGEX, IMG_MEDIA_REGEX, PHP_SCRIPTS_REGEX, SQL_SCRIPTS_REGEX, PDF_FILES_REGEX, \
    TXT_FILES_REGEX, CSV_FILES_REGEX
from app.services.http.rest import ApiService
import re

EMPTY_CONTENT = "Unable to get content from {url}"


class DisassemblerManager:

    @classmethod
    def download_content(cls, url):
        api_service = ApiService(url)
        response = api_service.get("/", {})
        result = response.text if response else EMPTY_CONTENT.format(url)

        return result

    @classmethod
    def get_result_as_list(cls, search_result):
        if search_result:
            result = [i.group() for i in search_result]
        else:
            result = None

        return result

    @classmethod
    def extract_headers(cls, site_content):
        head_block = re.search(HEADERS_REGEX, site_content, re.DOTALL)
        head_block = head_block.group()
        search_result = re.finditer(TAGS_REGEX, head_block, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_href_links(cls, site_content):
        search_result = re.finditer(f"({A_HREF_REGEX}|{LINK_HREF_REGEX})", site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_js_scripts(cls, site_content):
        search_result = re.finditer(SCRIPT_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_css_stylesheets(cls, site_content):
        search_result = re.finditer(CSS_STYLESHEETS_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_html_form(cls, site_content):
        search_result = re.finditer(HTML_FORM_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_img_media(cls, site_content):
        search_result = re.finditer(IMG_MEDIA_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_php_scripts(cls, site_content):
        search_result = re.finditer(PHP_SCRIPTS_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_sql_scripts(cls, site_content):
        search_result = re.finditer(SQL_SCRIPTS_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_pdf_files(cls, site_content):
        search_result = re.finditer(PDF_FILES_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_txt_files(cls, site_content):
        search_result = re.finditer(TXT_FILES_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_csv_files(cls, site_content):
        search_result = re.finditer(CSV_FILES_REGEX, site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result



