# Changelog

## 0.3.0 - 2026-09-09

- Adopt the stable `POST /v2/serp/search` endpoint and `results[]` response.
- Remove beta-only `metadata` examples while preserving unchanged-response behavior.

## 0.2.0 - 2026-09-07

- Move the tool from `POST /v1/serp` to the v2 beta URL-index endpoint.
- Document the flat `urls[]` response, `pagination.next_url`, and v1 field migration.
- Preserve the one-call, unchanged-response behavior without adding orchestration policy.

## 0.1.0 - 2026-08-19

- Initial Dify tool plugin for Reserp.
