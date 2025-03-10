from locust import task, run_single_user
from locust import FastHttpUser


class save_api(FastHttpUser):
    host = "https://vience.io:11040"
    default_headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "1062",
        "Content-Type": "application/json",
        "Host": "vience.io:11040",
        "Origin": "https://vience.io",
        "Referer": "https://vience.io/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    @task
    def t(self):
        with self.rest(
            "PUT",
            "/workspace/save",
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
            json={
                "wor_id": "4ZR38jV6",
                "nodes": '{"nodes":[{"id":"891fa7112438a34f","label":"DataManage","outputs":{"out":{"id":"737af906f9920625","socket":{"name":"Custom"}}},"inputs":{},"controls":{"ctrl":{"type":"DataManageControl","id":"0b869be8bae54687","option":{"path":"","thumbnail":""}}},"position":{"x":-200,"y":-400}},{"id":"821292cc1bb0ad3f","label":"CustomProcessing","outputs":{"out":{"id":"bccf366694e6913f","socket":{"name":"Custom"}}},"inputs":{"in":{"id":"b11070895f41e465","socket":{"name":"Custom"}}},"controls":{"ctrl":{"type":"CustomProcessingControl","id":"a2f726338da2245e","option":{"value":{"img_paths":{"891fa7112438a34f":""},"effector":{"input":["891fa7112438a34f"],"node":{}}}}}},"position":{"x":-200,"y":-200}}],"connections":[{"id":"c4eadfd966809546","source":"891fa7112438a34f","sourceOutput":"out","target":"821292cc1bb0ad3f","targetInput":"in"}]}',
                "title": "undefined",
                "category": "",
                "description": "",
            },
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(save_api)
