from locust import task, run_single_user
from locust import FastHttpUser


class vience(FastHttpUser):
    host = "https://vience.io:11040"
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

    @task
    def t(self):
        with self.rest(
            "GET",
            "/smc_proofreading/check_account/esy14@vience.co.kr",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/smc_proofreading/check_account/esy14@vience.co.kr",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/smc_proofreading/check_account/esy14@vience.co.kr",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/workspace/list/all",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/workspace/list/all",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/smc_proofreading/check_account/esy14@vience.co.kr",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/tag/tagging_progress/",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/deep_learning/model_list",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/pipe/list/",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/tag/tag_list",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/scheduler/task_list/",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/pipe/list",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/smc_proofreading/check_account/esy14@vience.co.kr",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/workspace/list/all",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/workspace/list/all",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/workspace/new",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "0",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/smc_proofreading/check_account/esy14@vience.co.kr",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/workspace/share_list/4ZR38jV6",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/workspace/4ZR38jV6",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "431",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":0,"y":0}}],"connections":[]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "810",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-218,"y":-382.4921875}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{}}},"position":{"x":0,"y":0}}],"connections":[]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "824",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-218,"y":-382.4921875}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{}}},"position":{"x":-218,"y":-198.4921875}}],"connections":[]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "965",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-218,"y":-382.4921875}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{}}},"position":{"x":-218,"y":-198.4921875}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1069",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-218,"y":-382.4921875}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "untitled",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "POST",
            "/module/custom_code",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "133",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "node_id": "821292cc1bb0ad3f",
                "title": "",
                "input_layout": "Single",
                "input_type": "Image",
                "output_layout": "Single",
                "output_type": "Image",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://cdn.jsdelivr.net/npm/monaco-editor@0.43.0/min/vs/base/worker/workerMain.js",
            headers={"Referer": ""},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://cdn.jsdelivr.net/npm/monaco-editor@0.43.0/min/vs/base/common/worker/simpleWorker.nls.js",
            headers={"Referer": ""},
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1069",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-218,"y":-382.4921875}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "untitled",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1070",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-218,"y":-382.4921875}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1070",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-218,"y":-382.4921875}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1070",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-218,"y":-382.4921875}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1061",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-200,"y":-400}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "untitled",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1062",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-200,"y":-400}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass
        with self.rest(
            "PUT",
            "/workspace/save",
            headers={
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "1061",
                "Host": "vience.io:11040",
                "Origin": "https://vience.io",
                "Referer": "https://vience.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
            },
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-200,"y":-400}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "untitled",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(vience)
