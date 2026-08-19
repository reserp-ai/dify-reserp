from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class ReserpProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        """Validate presence only; do not spend a search request."""
        if not credentials.get("reserp_api_key"):
            raise ToolProviderCredentialValidationError("Reserp API key is missing.")
