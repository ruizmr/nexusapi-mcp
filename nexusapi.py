"""NexusAPI Python SDK — 18 compute tools for AI agents.

Install: pip install nexusapi
Usage:
    from nexusapi import NexusAPI
    api = NexusAPI()  # auto-registers, gets free 250 credits
    result = api.scrape("https://example.com")
    result = api.execute("print(2+2)")
    result = api.sentiment("AI is amazing")
"""

import os
import json
import httpx

DEFAULT_BASE = os.environ.get("NEXUSAPI_URL", "https://marble-appendix-accurately-mark.trycloudflare.com")


class NexusAPI:
    def __init__(self, api_key: str = None, base_url: str = None):
        self.base = (base_url or DEFAULT_BASE).rstrip("/")
        self.key = api_key or os.environ.get("NEXUSAPI_KEY")
        self._client = httpx.Client(timeout=30)
        if not self.key:
            self._auto_register()

    def _auto_register(self):
        r = self._client.post(f"{self.base}/v1/agent/register", json={
            "agent_name": f"sdk-{os.getpid()}",
            "contact_email": "sdk@auto.register"
        })
        r.raise_for_status()
        d = r.json()
        self.key = d.get("api_key", "")
        print(f"NexusAPI: registered with {d.get('credits', 250)} free credits")

    def _headers(self):
        return {"Authorization": f"Bearer {self.key}", "Content-Type": "application/json"}

    def _post(self, path, **kwargs):
        r = self._client.post(f"{self.base}{path}", headers=self._headers(), json=kwargs)
        r.raise_for_status()
        return r.json()

    def _get(self, path, **params):
        r = self._client.get(f"{self.base}{path}", headers=self._headers(), params=params)
        r.raise_for_status()
        return r.json()

    # --- Web Tools ---
    def scrape(self, url: str, format: str = "text", extract_links: bool = False, max_length: int = 50000):
        return self._post("/v1/web/scrape", url=url, format=format, extract_links=extract_links, max_length=max_length)

    def scrape_batch(self, urls: list[str], **kwargs):
        return self._post("/v1/web/scrape/batch", urls=urls, **kwargs)

    # --- Code Execution ---
    def execute(self, code: str, timeout: int = 10):
        return self._post("/v1/exec/python", code=code, timeout=timeout)

    # --- ML / NLP ---
    def sentiment(self, text: str):
        return self._post("/v1/text/sentiment", text=text)

    def summarize(self, text: str, max_length: int = 150):
        return self._post("/v1/text/summarize", text=text, max_length=max_length)

    def keywords(self, text: str, top_n: int = 10):
        return self._post("/v1/text/keywords", text=text, top_n=top_n)

    def entities(self, text: str):
        return self._post("/v1/text/entities", text=text)

    def classify(self, text: str, labels: list[str]):
        return self._post("/v1/ml/zero-shot", text=text, candidate_labels=labels)

    # --- Data Tools ---
    def hash(self, data: str, algorithm: str = "sha256"):
        return self._post("/v1/data/hash", data=data, algorithm=algorithm)

    def encode_base64(self, data: str):
        return self._post("/v1/data/encode", data=data, encoding="base64")

    # --- Utility ---
    def qr(self, data: str):
        return self._post("/v1/util/qr", data=data)

    def uuid(self):
        return self._get("/v1/util/uuid")

    # --- Account ---
    def usage(self):
        return self._get("/v1/agent/usage")

    def balance(self):
        return self.usage().get("credits_remaining", 0)
