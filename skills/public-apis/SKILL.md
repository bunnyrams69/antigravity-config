---
name: public-apis
description: Discover, search, evaluate, and integrate free and public APIs across 50+ categories (finance, weather, crypto, geocoding, sports, AI/ML, open data, test data) and community MCP servers. Use when the user needs an API for external data, wants mock or test data, asks for third-party integrations, or wants to find a free API service.
---

# Public APIs Skill

Discover, evaluate, and integrate free, community-curated public APIs and MCP servers into your applications. Sourced from [public-apis/public-apis](https://github.com/public-apis/public-apis), covering 1,950+ APIs across 51 categories.

---

## 1. Fast API Search Tool

This skill comes with an offline CLI search tool for instant querying of the API catalog:

```bash
# General keyword search
python "C:\Users\WELCOME\.gemini\config\skills\public-apis\scripts\search_api.py" --query "exchange rate"

# Filter for completely free APIs with NO authentication required
python "C:\Users\WELCOME\.gemini\config\skills\public-apis\scripts\search_api.py" --query "weather" --no-auth

# Filter by category and ensure CORS support (critical for browser/frontend code)
python "C:\Users\WELCOME\.gemini\config\skills\public-apis\scripts\search_api.py" --category "Geocoding" --cors yes

# Output in JSON format for automated tooling
python "C:\Users\WELCOME\.gemini\config\skills\public-apis\scripts\search_api.py" --query "jokes" --json

# List all 51 categories
python "C:\Users\WELCOME\.gemini\config\skills\public-apis\scripts\search_api.py" --list-categories

# List available community MCP servers
python "C:\Users\WELCOME\.gemini\config\skills\public-apis\scripts\search_api.py" --list-mcp
```

---

## 2. API Selection & Evaluation Checklist

Before integrating any public API, verify these 4 requirements:

1. **Authentication Mode**:
   - `No`: Ideal for quick prototypes, frontend demos, and educational projects. No API key needed.
   - `apiKey`: Requires signing up on the provider's portal for a free key. Keep in `.env`.
   - `OAuth`: Requires authorization flow (best for user-specific data like GitHub, Spotify).
2. **CORS (Cross-Origin Resource Sharing)**:
   - If calling directly from a **frontend/browser** (React, Vue, plain JS), the API **MUST** support CORS (`CORS: Yes`).
   - If `CORS: No` or `Unknown`, the API must be called from a **backend server** (Node/Express, Python/FastAPI) or via a server-side proxy to prevent browser CORS errors.
3. **Transport Security (HTTPS)**:
   - Always choose `HTTPS: Yes` for production security and to avoid mixed-content blocking on HTTPS web apps.
4. **Rate Limits & Health**:
   - Verify rate limits (e.g. 100 req/day vs unlimited).
   - Test endpoints with a simple `curl` check before writing complex logic.

---

## 3. Integration Patterns

### Python (`requests` / `httpx`)
```python
import os
import requests

API_KEY = os.getenv("SERVICE_API_KEY") # If required
headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}

response = requests.get("https://api.example.com/v1/data", headers=headers, timeout=10)
response.raise_for_status()
data = response.json()
```

### TypeScript / JavaScript (`fetch`)
```typescript
async function fetchPublicData(): Promise<any> {
  const response = await fetch("https://api.example.com/v1/data", {
    headers: {
      "Accept": "application/json"
    }
  });
  if (!response.ok) {
    throw new Error(`API error: ${response.status} ${response.statusText}`);
  }
  return await response.json();
}
```

---

## 4. References & Documentation

* **[references/categories.md](references/categories.md)**: Full list of all 51 categories with counts and featured APIs.
* **[references/mcp-servers.md](references/mcp-servers.md)**: Model Context Protocol servers enabling agents to call tools.
* **Original Repository**: Cloned in workspace at [`e:\common folder\public-apis`](file:///e:/common%20folder/public-apis).
