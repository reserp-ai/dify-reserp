"""Minimal Dify tool for the Reserp Google Search API."""

from __future__ import annotations

import json
from collections.abc import Callable, Generator
from typing import Any
from urllib.request import Request, urlopen

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

ENDPOINT = "https://api.reserp.ai/v2/serp/urls"


def request_reserp(
    *,
    url: str,
    api_key: str,
    opener: Callable[[Request], Any] = urlopen,
) -> dict[str, Any]:
    """Make one request and return the public Reserp v2 URL-index payload."""
    request = Request(
        ENDPOINT,
        data=json.dumps({"url": url}).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with opener(request) as response:
        return json.load(response)


class ReserpGoogleSearchTool(Tool):
    def _invoke(
        self,
        tool_parameters: dict[str, Any],
    ) -> Generator[ToolInvokeMessage, None, None]:
        response = request_reserp(
            url=tool_parameters["url"],
            api_key=self.runtime.credentials["reserp_api_key"],
        )
        yield self.create_json_message(response)
