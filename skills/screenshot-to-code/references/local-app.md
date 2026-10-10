# Running the Local screenshot-to-code Application

The fullstack `screenshot-to-code` application has been cloned into your workspace at:
`e:\common folder\screenshot-to-code`

---

## Prerequisites

1. **Python 3.10+ & Poetry**:
   ```bash
   pip install poetry
   ```
2. **Node.js 18+ & pnpm**:
   ```bash
   npm install -g pnpm
   ```
3. **API Keys**:
   At least one multimodal API key (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, or `GEMINI_API_KEY`) is required.
   Create `backend/.env`:
   ```env
   OPENAI_API_KEY=your_key_here
   # OR
   ANTHROPIC_API_KEY=your_key_here
   # OR
   GEMINI_API_KEY=your_key_here
   ```

---

## Starting the App

### 1. Start Backend (FastAPI)
```bash
cd "e:\common folder\screenshot-to-code\backend"
poetry install
poetry run uvicorn main:app --reload --port 7001
```

### 2. Start Frontend (Vite/React)
```bash
cd "e:\common folder\screenshot-to-code\frontend"
pnpm install
pnpm dev
```

Open `http://localhost:5173` in your browser.

---

## Using Docker (Alternative)

You can also run everything using Docker Compose:
```bash
cd "e:\common folder\screenshot-to-code"
echo "OPENAI_API_KEY=your_key" > backend/.env
docker compose up --build
```
