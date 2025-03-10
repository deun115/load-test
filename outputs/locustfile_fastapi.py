from locust import task, run_single_user
from locust import FastHttpUser


class localhost_test(FastHttpUser):
    host = "http://127.0.0.1:8000"
    default_headers = {
        "Referer": "http://127.0.0.1:8000/docs",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "accept": "application/json",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
    }

    @task
    def t(self):
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest(
            "POST", "/items/", headers={}, json={"name": "asdfasdf", "price": 10000}
        ) as resp:
            pass
        with self.rest("GET", "/tokens/") as resp:
            pass
        with self.rest("GET", "/tokens/") as resp:
            pass
        with self.rest("GET", "/tokens/") as resp:
            pass
        with self.rest("GET", "/tokens/") as resp:
            pass
        with self.rest("GET", "/tokens/") as resp:
            pass
        with self.rest("GET", "/tokens/") as resp:
            pass
        with self.rest("GET", "/tokens/") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass
        with self.rest("GET", "/items/123") as resp:
            pass


if __name__ == "__main__":
    run_single_user(localhost_test)
