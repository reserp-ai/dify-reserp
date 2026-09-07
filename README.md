# Reserp for Dify

## Overview

[Reserp](https://reserp.ai/) is a Google Search API for developers and AI agents. Submit a complete Google Search URL and receive the v2 flat, page-ordered, deduplicated URL-and-text index.

This Dify plugin is deliberately minimal. One tool invocation makes one request to `POST /v2/serp/urls` and emits one JSON message containing the public response. It adds no retries, timeout policy, concurrency management, caching, queues, result conversion, or automatic pagination.

## Configuration

1. Obtain a Reserp API key.
2. Install the plugin in Dify.
3. Open **Tools → Reserp → Authentication** and enter the key.

## Usage

Add **Google Search with Reserp** to an agent or workflow and provide a complete URL such as:

```text
https://www.google.com/search?q=photonic+computing&gl=us&hl=en
```

On success, `urls[]` contains the flattened URL index; `text` is present when visible text is available. `pagination.next_url` can be submitted in a later invocation, but its presence does not guarantee that another page contains results. Do not infer pagination from `len(urls)`.

The surrounding Dify application controls retries and all other operational policy. When the API reports `retryable`, the plugin exposes that field unchanged and takes no action itself.

- [API documentation](https://reserp.ai/docs)
- [OpenAPI definition](https://reserp.ai/openapi.json)
- [Postman collection](https://www.postman.com/reserp-ai/reserp-google-search-api)
- [Source code](https://github.com/reserp-ai/dify-reserp)

## Migrating from 0.1

Version 0.2 replaces the v1 recursive `results[]` response with v2 `urls[]`. Other notable renames are `url` → `request.url`, `finalUrl` → `page.url`, `pagination.nextUrl` → `pagination.next_url`, and `billingSource` → `billing_source`.

For typed result families, SERP features, and explicit positions, call the [structured v2 endpoint](https://reserp.ai/docs/structured) directly or use an official Reserp SDK.

## Connection requirements

Each tool invocation makes one outbound HTTPS request to `https://api.reserp.ai/v2/serp/urls`. The plugin does not contact Google directly.

## Support

For API and plugin questions, contact [support@reserp.ai](mailto:support@reserp.ai).
