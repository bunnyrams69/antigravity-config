# Community MCP Servers (Model Context Protocol)

| Name | Description | Auth | Transport | Install |
| :--- | :--- | :--- | :--- | :--- |
| [OpenSwissData](https://github.com/cammac-creator/openswissdata/tree/main/sdks/mcp-server) | Swiss customs tariff (TARES), FINMA register and warnings, NOGA/NACE/ISIC code crosswalks | No | stdio, HTTP | [Glama](https://glama.ai/mcp/connectors/io.github.cammac-creator/openswissdata) |
| [IPstack MCP](https://ipstack.com/mcp) | IP geolocation, threat and timezone lookups for agents | apiKey | stdio, HTTP | [Cursor](https://cursor.directory/plugins/apilayer-mcp-adapter) · [Glama](https://glama.ai/mcp/connectors/com.apilayer.mcp/apilayer-mcp-adapter) |
| [corpusAI Cloud Pricing](https://cloud.trycorpus.ai/docs#quick-start-for-agents) | Cloud, GPU and LLM token prices for agents, free discovery tools and paid per-call data | No | stdio, HTTP | [npm](https://www.npmjs.com/package/corpus-cloud-pricing-mcp) · [MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=corpus-cloud-pricing) |
| [GitHub](https://github.com/github/github-mcp-server) | Repos, issues, PRs, code search | OAuth | stdio, HTTP | [Glama](https://glama.ai/mcp/servers/@github/github-mcp-server) |
| [Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Read/write local files | No | stdio | – |
| [Twinbay](https://docs.twinbay.ai/mcp-server) | Spin up stateful API twins, read request logs and grade agent runs | OAuth | HTTP | – |
