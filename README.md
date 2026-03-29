# NexusAPI MCP Server

> 15 compute tools for AI agents. Self-register, 1000 free credits, pay with USDC on Base L2.

**Server URL:** `https://marble-appendix-accurately-mark.trycloudflare.com`

## Quick Start

```bash
# Register (instant, no approval)
curl -X POST https://marble-appendix-accurately-mark.trycloudflare.com/v1/agent/register \
  -H 'Content-Type: application/json' \
  -d '{"agent_name":"my-agent","contact_email":"you@example.com"}'

# Returns: {"api_key":"nx_...", "credits":1000, ...}
```

## Tools

### Text Analysis
| Tool | Endpoint | Credits |
|------|----------|---------|
| Sentiment Analysis | `POST /v1/text/sentiment` | 1 |
| Summarization | `POST /v1/text/summarize` | 2 |
| Keyword Extraction | `POST /v1/text/keywords` | 1 |
| Entity Recognition | `POST /v1/text/entities` | 1 |
| Readability Score | `POST /v1/text/readability` | 1 |

### Image Processing
| Tool | Endpoint | Credits |
|------|----------|---------|
| Resize | `POST /v1/image/resize` | 2 |
| Optimize | `POST /v1/image/optimize` | 2 |
| Watermark | `POST /v1/image/watermark` | 3 |
| Blur | `POST /v1/image/blur` | 2 |
| Metadata | `POST /v1/image/metadata` | 1 |

### Data Tools
| Tool | Endpoint | Credits |
|------|----------|---------|
| JSON Validate/Flatten/Diff | `POST /v1/data/json/*` | 1 |
| CSV to JSON | `POST /v1/data/csv/to-json` | 1 |
| Hash (SHA256, MD5, etc.) | `POST /v1/data/hash` | 1 |
| Encode/Decode (base64, URL) | `POST /v1/data/encode` | 1 |
| Regex Match/Replace | `POST /v1/data/regex/*` | 1 |

### ML Inference
| Tool | Endpoint | Credits |
|------|----------|---------|
| Transformer Models | `POST /v1/ml/infer` | 10 |

Supports: sentiment, NER, summarization, zero-shot classification, text generation.

## Pricing

- **1000 free credits** on signup ($1.00 USD)
- **1 credit = $0.001** per API call
- Deposit USDC on Base L2 for more credits

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

## Discovery Endpoints

| Endpoint | Description |
|----------|-------------|
| `/.well-known/ai-plugin.json` | OpenAI plugin manifest |
| `/.well-known/mcp.json` | MCP server manifest |
| `/openapi-agent.json` | Simplified OpenAPI for agents |
| `/v1/agent/tools` | Full tool list with schemas |

## License

MIT

## Try It Now

```bash
curl -s https://marble-appendix-accurately-mark.trycloudflare.com/static/try.sh | bash
```

Registers, gets API key, and runs two demo calls in 10 seconds.
