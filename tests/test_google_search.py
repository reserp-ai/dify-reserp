"""Contract tests for the Dify Reserp transport."""

from __future__ import annotations

import io
import json

import pytest

from tools.google_search import request_reserp


class FakeResponse(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_args):
        self.close()


def test_one_request_and_unchanged_payload() -> None:
    payload = {
        "ok": True,
        "request": {"url": "https://www.google.com/search?q=test"},
        "page": {"url": "https://www.google.com/search?q=test"},
        "results": [{"url": "https://example.com", "text": "Example"}],
        "pagination": {"next_url": "https://www.google.com/search?q=test&start=10"},
        "billed": True,
        "billing_source": "prepaid",
    }
    calls = []

    def opener(request):
        calls.append(request)
        return FakeResponse(json.dumps(payload).encode())

    result = request_reserp(
        url="https://www.google.com/search?q=test",
        api_key="test-key",
        opener=opener,
    )

    assert result == payload
    assert len(calls) == 1
    assert calls[0].full_url == "https://api.reserp.ai/v2/serp/search"
    assert calls[0].get_header("Authorization") == "Bearer test-key"
    assert json.loads(calls[0].data) == {
        "url": "https://www.google.com/search?q=test"
    }


def test_failure_propagates_without_retry() -> None:
    failure = RuntimeError("transport failure")
    calls = 0

    def opener(_request):
        nonlocal calls
        calls += 1
        raise failure

    with pytest.raises(RuntimeError) as caught:
        request_reserp(
            url="https://www.google.com/search?q=test",
            api_key="test-key",
            opener=opener,
        )

    assert caught.value is failure
    assert calls == 1
