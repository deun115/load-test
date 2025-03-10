from locust import task, run_single_user
from locust import FastHttpUser


class github(FastHttpUser):
    host = "https://github.com"
    default_headers = {
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/blob/main/tests/inputs/apple-buy-a-mac.har",
            headers={
                "Referer": "https://github.com/SvenskaSpel/har2locust?tab=readme-ov-file",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/security/overall-count",
            headers={
                "Accept": "text/fragment+html",
                "Referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/inputs/apple-buy-a-mac.har",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/latest-commit/main/tests/inputs/apple-buy-a-mac.har",
            headers={
                "Accept": "application/json",
                "GitHub-Verified-Fetch": "true",
                "Referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/inputs/apple-buy-a-mac.har",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/deferred-metadata/main/tests/inputs/apple-buy-a-mac.har",
            headers={
                "Accept": "application/json",
                "GitHub-Verified-Fetch": "true",
                "Referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/inputs/apple-buy-a-mac.har",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/notifications/indicator",
            headers={
                "Accept": "application/json",
                "Referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/inputs/apple-buy-a-mac.har",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/github-copilot/chat?skip_anchor=true",
            headers={
                "Accept": "text/html",
                "Referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/inputs/apple-buy-a-mac.har",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/github-copilot/chat/entitlement",
            headers={
                "Accept": "application/json",
                "GitHub-Verified-Fetch": "true",
                "Referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/inputs/apple-buy-a-mac.har",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://github.githubassets.com/assets/apple-touch-icon-144x144-b882e354c005.png",
            headers={
                "Referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/inputs/apple-buy-a-mac.har",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/tree/main/tests/inputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "if-none-match": 'W/"681ffbeff5d75a6df72539f71834720e"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/inputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-github-target": "dotcom",
                "x-react-router": "json",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/latest-commit/main/tests/inputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"c0a4e9b3b18c10f204796479fca2cf06"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/inputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/tree-commit-info/main/tests/inputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"17b6fb7f4221e366c8af4e15f372744c"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/inputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/deferred-metadata/main/tests/inputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"5560652144165da5a1819615e6d20d62"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/inputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/tree/main/tests",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "if-none-match": 'W/"d23293588d8df2d8d5f86e2ab04a61b9"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-github-target": "dotcom",
                "x-react-router": "json",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/latest-commit/main/tests",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"c0a4e9b3b18c10f204796479fca2cf06"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/tree-commit-info/main/tests",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"9d64b7cc5c99a97684c9ac8b9fe82462"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/deferred-metadata/main/tests",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"5560652144165da5a1819615e6d20d62"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/tree/main/tests/outputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/outputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-github-target": "dotcom",
                "x-react-router": "json",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/latest-commit/main/tests/outputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "github-verified-fetch": "true",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/outputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/tree-commit-info/main/tests/outputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "github-verified-fetch": "true",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/outputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/deferred-metadata/main/tests/outputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "github-verified-fetch": "true",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/outputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/blob/main/tests/outputs/apple-buy-a-mac.py",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/outputs/apple-buy-a-mac.py",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-github-target": "dotcom",
                "x-react-router": "json",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/latest-commit/main/tests/outputs/apple-buy-a-mac.py",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "github-verified-fetch": "true",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/outputs/apple-buy-a-mac.py",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.client.request(
            "PUT",
            "/repos/preferences",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryNobcHG1srVkTdnKK",
                "github-verified-fetch": "true",
                "origin": "https://github.com",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/outputs/apple-buy-a-mac.py",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            data='------WebKitFormBoundaryNobcHG1srVkTdnKK\r\nContent-Disposition: form-data; name="tree_view_expanded_preference"\r\n\r\n\r\n------WebKitFormBoundaryNobcHG1srVkTdnKK\r\nContent-Disposition: form-data; name="symbols_view_expanded_preference"\r\n\r\n\r\n------WebKitFormBoundaryNobcHG1srVkTdnKK\r\nContent-Disposition: form-data; name="code_line_wrap_enabled"\r\n\r\nfalse\r\n------WebKitFormBoundaryNobcHG1srVkTdnKK--\r\n',
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/deferred-metadata/main/tests/outputs/apple-buy-a-mac.py",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "github-verified-fetch": "true",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/outputs/apple-buy-a-mac.py",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/SvenskaSpel/har2locust/deferred-ast/main/tests/outputs/apple-buy-a-mac.py",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "github-verified-fetch": "true",
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/blob/main/tests/outputs/apple-buy-a-mac.py",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/latest-commit/main/tests/outputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"c0a4e9b3b18c10f204796479fca2cf06"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/outputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/tree-commit-info/main/tests/outputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"897a26c414324004abce519d865bd8d5"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/outputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/SvenskaSpel/har2locust/deferred-metadata/main/tests/outputs",
            headers={
                "accept": "application/json",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/json",
                "github-verified-fetch": "true",
                "if-none-match": 'W/"5560652144165da5a1819615e6d20d62"',
                "priority": "u=1, i",
                "referer": "https://github.com/SvenskaSpel/har2locust/tree/main/tests/outputs",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(github)
