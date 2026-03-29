# NexusAPI — 18 Compute Tools for AI Agents

Web scraping, sandboxed code execution, ML inference, and 15 more tools. **250 free credits on signup.**

## Install the SDK

```bash
pip install git+https://github.com/ruizmr/nexusapi-mcp.git
```

## Quick Start (3 lines)

```python
from nexusapi import NexusAPI

api = NexusAPI()  # auto-registers, instant API key, 250 free credits

# Scrape any URL → clean text
page = api.scrape("https://news.ycombinator.com")

# Execute Python safely
result = api.execute("import math; print(math.factorial(20))")

# ML inference
sentiment = api.sentiment("Agent-to-agent commerce is the future")
```

## Zero-Auth Demo (try before registering)

```bash
# Scrape — no API key needed
curl "https://marble-appendix-accurately-mark.trycloudflare.com/v1/try/scrape?url=https://example.com"

# Sentiment — no API key needed
curl "https://marble-appendix-accurately-mark.trycloudflare.com/v1/try/sentiment?text=AI+agents+are+amazing"
```

## Agent Self-Registration (one call)

```bash
curl -X POST https://marble-appendix-accurately-mark.trycloudflare.com/v1/agent/register \
  -H "Content-Type: application/json" \
  -d '{"agent_name": "my-agent", "contact_email": "agent@example.com"}'
```

Returns: `{"api_key": "nx_...", "credits": 250}`

## All 18 Tools

| Category | Endpoint | Credits | Description |
|----------|----------|---------|-------------|
| **Web** | `/v1/web/scrape` | 5 | Fetch URL → clean text/markdown/links |
| **Web** | `/v1/web/scrape/batch` | 25 | Batch scrape up to 5 URLs |
| **Code** | `/v1/exec/python` | 20 | Sandboxed Python execution |
| **Code** | `/v1/exec/python/batch` | 80 | Batch execute up to 5 scripts |
| **NLP** | `/v1/text/sentiment` | 10 | Sentiment analysis |
| **NLP** | `/v1/text/summarize` | 10 | Text summarization |
| **NLP** | `/v1/text/keywords` | 5 | Keyword extraction |
| **NLP** | `/v1/text/entities` | 10 | Named entity recognition |
| **NLP** | `/v1/text/readability` | 1 | Readability scoring |
| **ML** | `/v1/ml/zero-shot` | 10 | Zero-shot text classification |
| **Image** | `/v1/image/resize` | 5 | Image resize/optimize |
| **Image** | `/v1/image/blur` | 3 | Image blur/effects |
| **Data** | `/v1/data/hash` | 1 | SHA256/MD5/etc hashing |
| **Data** | `/v1/data/encode` | 1 | Base64/URL encoding |
| **Data** | `/v1/data/regex` | 1 | Regex matching |
| **Util** | `/v1/util/qr` | 2 | QR code generation |
| **Util** | `/v1/util/uuid` | 1 | UUID generation |
| **Util** | `/v1/util/timestamp` | 1 | Timestamp conversion |

## MCP Integration

```json
{
  "mcpServers": {
    "nexusapi": {
      "url": "https://marble-appendix-accurately-mark.trycloudflare.com/.well-known/mcp.json"
    }
  }
}
```

## Payment

- **Free tier**: 250 credits on signup
- **Top up**: Deposit USDC on Base L2 to treasury address (auto-credited in 30s)
- **Pricing**: 1 credit = $0.001

## Why NexusAPI?

- **Zero friction**: One POST to register, instant API key
- **Agent-native**: MCP manifest, machine-readable schemas, no human auth flows
- **Sovereign compute**: Runs on dedicated hardware, no cloud vendor lock-in
- **Crypto payments**: USDC on Base L2, sub-cent transaction fees
