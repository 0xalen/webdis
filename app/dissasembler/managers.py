from app.services.http.rest import ApiService
import re

TAGS_REGEX = r"<.+>(.*?)</.+>"
HEADERS_REGEX = r"<head\s+(.*?)</head>"
A_HREF_REGEX = r"<a\s+(.*?)(\/a|\/)>"
LINK_HREF_REGEX = r"<link(.*?)href=(.*?)\/>"
SCRIPT_REGEX = r"<script(\s|>)+(.*?)\/(script|.*)>"


class DisassemblerManager:

    @classmethod
    def download_content(cls, url):
        api_service = ApiService(url)
        response = api_service.get("/", {})
        result = response.text

        return result

    @classmethod
    def get_result_as_list(cls, search_result):
        if search_result:
            result = search_result.groups()
        else:
            result = None

        return result

    @classmethod
    def extract_headers(cls, site_content):
        head_block = re.search(HEADERS_REGEX, site_content, re.DOTALL)
        head_block = head_block[0]
        search_result = re.search(TAGS_REGEX, head_block, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_href_links(cls, site_content):
        search_result = re.search(f"({A_HREF_REGEX}|{LINK_HREF_REGEX})", site_content, re.DOTALL)
        result = cls.get_result_as_list(search_result)

        return result

    @classmethod
    def extract_js_scripts(cls, site_content):
        search_result = re.finditer(SCRIPT_REGEX, site_content, re.DOTALL)
        # result = cls.get_result_as_list(search_result)
        result = [i.group() for i in search_result]

        return result
