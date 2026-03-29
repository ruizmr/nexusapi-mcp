#!/usr/bin/env node
const { Server } = require("@modelcontextprotocol/sdk/server/index.js");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio.js");

const BASE = process.env.NEXUSAPI_URL || "https://marble-appendix-accurately-mark.trycloudflare.com";
let API_KEY = process.env.NEXUSAPI_KEY || "";

const server = new Server({ name: "nexusapi", version: "1.0.0" }, {
  capabilities: { tools: {} }
});

async function ensureKey() {
  if (API_KEY) return;
  const r = await fetch(`${BASE}/v1/agent/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ agent_name: "mcp-client", contact_email: "mcp@auto" })
  });
  const d = await r.json();
  API_KEY = d.api_key;
}

async function call(path, body) {
  await ensureKey();
  const r = await fetch(`${BASE}${path}`, {
    method: "POST",
    headers: { "Authorization": `Bearer ${API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  return r.json();
}

server.setRequestHandler("tools/list", async () => ({
  tools: [
    { name: "web_scrape", description: "Scrape a URL and return clean text content", inputSchema: { type: "object", properties: { url: { type: "string", description: "URL to scrape" } }, required: ["url"] } },
    { name: "execute_python", description: "Execute Python code in a sandbox", inputSchema: { type: "object", properties: { code: { type: "string", description: "Python code to run" } }, required: ["code"] } },
    { name: "sentiment", description: "Analyze sentiment of text", inputSchema: { type: "object", properties: { text: { type: "string" } }, required: ["text"] } },
    { name: "summarize", description: "Summarize text", inputSchema: { type: "object", properties: { text: { type: "string" } }, required: ["text"] } },
  ]
}));

server.setRequestHandler("tools/call", async (request) => {
  const { name, arguments: args } = request.params;
  let result;
  switch (name) {
    case "web_scrape": result = await call("/v1/web/scrape", { url: args.url }); break;
    case "execute_python": result = await call("/v1/exec/python", { code: args.code }); break;
    case "sentiment": result = await call("/v1/text/sentiment", { text: args.text }); break;
    case "summarize": result = await call("/v1/text/summarize", { text: args.text }); break;
    default: result = { error: "Unknown tool" };
  }
  return { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] };
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}
main().catch(console.error);
