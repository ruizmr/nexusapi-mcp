# NexusAPI MCP Server

> **18 compute tools for AI agents.** Web scraping, code execution, text analysis, image processing, data tools, ML inference.
> Self-register, 250 free credits, pay with USDC on Base L2.

**Server:** `https://marble-appendix-accurately-mark.trycloudflare.com`

## Try It Now

```bash
curl -s https://marble-appendix-accurately-mark.trycloudflare.com/static/try.sh | bash
```

## Quick Start

```bash
# Register (instant, no approval)
curl -X POST https://marble-appendix-accurately-mark.trycloudflare.com/v1/agent/register \
  -H 'Content-Type: application/json' \
  -d '{"agent_name":"my-agent","contact_email":"you@example.com"}'
# Returns: {"api_key":"nx_...", "credits":250, ...}
```

## High-Value Tools

### Web Scrape (5 credits)
```bash
curl -X POST https://marble-appendix-accurately-mark.trycloudflare.com/v1/web/scrape \
  -H 'Authorization: Bearer YOUR_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com","format":"markdown"}'
```

### Code Execution (20 credits)
```bash
curl -X POST https://marble-appendix-accurately-mark.trycloudflare.com/v1/exec/python \
  -H 'Authorization: Bearer YOUR_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"code":"print(sum(range(100)))","timeout":10}'
```

### ML Inference (10 credits)
```bash
curl -X POST https://marble-appendix-accurately-mark.trycloudflare.com/v1/ml/infer \
  -H 'Authorization: Bearer YOUR_KEY' \
  -H 'Content-Type: application/json' \
  -d '{"task":"sentiment-analysis","text":"This tool is incredible"}'
```

## All 18 Tools

| Tool | Endpoint | Credits |
|------|----------|---------|
| **Web Scrape** | `POST /v1/web/scrape` | **5** |
| **Batch Scrape (10 URLs)** | `POST /v1/web/scrape/batch` | **25** |
| **Python Execution** | `POST /v1/exec/python` | **20** |
| **ML Inference** | `POST /v1/ml/infer` | **10** |
| Sentiment Analysis | `POST /v1/text/sentiment` | 1 |
| Summarization | `POST /v1/text/summarize` | 2 |
| Keyword Extraction | `POST /v1/text/keywords` | 1 |
| Entity Recognition | `POST /v1/text/entities` | 1 |
| Readability Score | `POST /v1/text/readability` | 1 |
| Image Resize | `POST /v1/image/resize` | 2 |
| Image Optimize | `POST /v1/image/optimize` | 2 |
| Image Watermark | `POST /v1/image/watermark` | 3 |
| JSON Tools | `POST /v1/data/json/*` | 1 |
| CSV to JSON | `POST /v1/data/csv/to-json` | 1 |
| Hash (SHA256, etc.) | `POST /v1/data/hash` | 1 |
| Regex | `POST /v1/data/regex/*` | 1 |
| QR Code | `POST /v1/utility/qr` | 1 |
| UUID/Password/etc. | `POST /v1/utility/*` | 1 |

## Pricing

- **250 free credits** on signup ($0.25)
- 1 credit = $0.001
- Deposit USDC on Base L2 for more

## Discovery

| Endpoint | Description |
|----------|-------------|
| `/.well-known/ai-plugin.json` | OpenAI plugin manifest |
| `/.well-known/mcp.json` | MCP manifest |
| `/v1/agent/tools` | Full tool list |

## License
MIT
