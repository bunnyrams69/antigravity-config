---
name: cloudflare-deploy
description: >-
  Deploy any local project to the public internet via a Cloudflare Quick Tunnel.
  Use when the user asks to deploy, share a live link, make a site public,
  tunnel, expose localhost, or says "give me a link", "deploy this",
  "cloudflare tunnel", or "share this site".
---

# Cloudflare Quick Tunnel Deploy

Deploy any local project to the public internet using `cloudflared` Quick Tunnels.
No Cloudflare account required — generates a temporary public `*.trycloudflare.com` URL.

## Prerequisites

`cloudflared` must be installed. If not, install it:

```powershell
winget install Cloudflare.cloudflared --accept-source-agreements --accept-package-agreements
```

Verify with:

```powershell
cloudflared --version
```

## Steps

### 1. Start a local server

If the project doesn't already have a dev server running, start one.

For **static sites** (HTML/CSS/JS with no build step):

```powershell
python -m http.server 8000
```

For **Node.js projects** with a dev script:

```powershell
npm run dev
```

Pick a port that isn't in use. Common choices: `8000`, `8080`, `5173`, `3000`.
Run the server as a **background daemon** so it stays alive.

### 2. Open the Cloudflare tunnel

Once the local server is confirmed running, start the tunnel:

```powershell
cloudflared tunnel --url http://localhost:<PORT>
```

Run this as a **background daemon**.

### 3. Extract and share the URL

Watch the tunnel's output. Within a few seconds, `cloudflared` prints a line like:

```
+--------------------------------------------------------------------------------------------+
|  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
|  https://XXXXX-XXXXX-XXXXX-XXXX.trycloudflare.com                                        |
+--------------------------------------------------------------------------------------------+
```

Extract the `https://....trycloudflare.com` URL and share it with the user.

### 4. Report to user

Present the URL clearly:

> 🌐 **Your site is live at:** `https://XXXXX.trycloudflare.com`
>
> This is a temporary public URL. It stays active as long as the tunnel process is running.
> To stop sharing, kill the cloudflared tunnel task.

## Stopping the tunnel

Use `manage_task` to kill the cloudflared daemon and (optionally) the local server daemon.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `cloudflared` not found | Run `winget install Cloudflare.cloudflared` and restart the shell or use the full path |
| Port already in use | Pick a different port (8001, 8080, 9000) |
| Tunnel connects but site unreachable | Confirm the local server is actually running on that port |
| Permission errors on Windows | Try a port above 1024 (e.g. 8000) |

## Notes

- Quick Tunnels are **temporary** — the URL changes each time you restart the tunnel.
- No Cloudflare account or login is needed.
- The tunnel supports HTTP, WebSocket, and SSE traffic.
- For persistent URLs, use `cloudflared tunnel create` with a Cloudflare account (not covered by this skill).
