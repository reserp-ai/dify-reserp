# Reserp for Dify

## Overview

[Reserp](https://reserp.ai/) is a Google Search API for developers. Submit a complete Google Search URL and receive visible result blocks as structured JSON.

This Dify plugin is deliberately minimal. One tool invocation makes one public Reserp request and emits one JSON message containing the response. It adds no retries, timeout policy, concurrency management, caching, queues, result conversion, or automatic pagination.

## Configuration

1. Obtain a Reserp API key.
2. Install the plugin in Dify.
3. Open **Tools → Reserp → Authentication** and enter the key.

## Usage

Add **Google Search with Reserp** to an agent or workflow and provide a complete URL such as:

```text
https://www.google.com/search?q=photonic+computing&gl=us&hl=en
```

The surrounding Dify application controls retries and all other operational policy.

- [API documentation](https://reserp.ai/docs)
- [OpenAPI definition](https://reserp.ai/openapi.json)
- [Source code](https://github.com/reserp-ai/dify-reserp)

## Support

For API and plugin questions, contact [support@reserp.ai](mailto:support@reserp.ai).
