<img src="assets/coding-desk.webp" width="100%" alt="Ayush CV coding in VS Code with black coffee and philosophy books on the desk. A white Real Madrid Benzema number 9 shirt hangs on the wall.">

<h1 align="center">Hi, I’m Ayush.</h1>

<p align="center">
  <img src="assets/hello.svg" width="412" alt="I build agents and test their limits.">
</p>

<p align="center">
  <a href="mailto:ayushcv.tech@gmail.com"><img src="assets/contact/email.svg" alt="Email ayushcv.tech@gmail.com"></a>
  <a href="https://www.linkedin.com/in/ayush-cv-6a68a233b/"><img src="assets/contact/linkedin.svg" alt="Connect on LinkedIn"></a>
  <img src="https://komarev.com/ghpvc/?username=Ayushcv-46&amp;label=Profile%20views&amp;style=for-the-badge&amp;color=17685f" alt="Profile views counted by Komarev">
</p>

## About me

I write Python systems that search documents, coordinate agents, and route requests between models. My favorite part is figuring out where they go wrong. Sometimes I trace a bad answer back to a missing passage. Other times I take a provider offline to see how the gateway handles the next request.

I study **Computer Science & Information Technology at REVA University** (B.Tech, 2027). I’m looking for **AI and GenAI internships** and I’m also interested in **backend software engineering**. I practice data structures and algorithms in C++.

## Selected work

### [Fin Research Agent](https://github.com/Ayushcv-46/fin-research-agent)

I built an assistant that cites passages from SEC filings. Adding a retrieval pass sounded promising, so I tested it against a fixed baseline.

Across 12 tickers, adaptive retrieval showed no measurable improvement in my experiment. [Inspect the recorded runs →](https://github.com/Ayushcv-46/fin-research-agent/blob/main/results/retrieval_comparison.json)

### [ModelMux](https://github.com/Ayushcv-46/ModelMux)

One chat API for Groq, Gemini, and local models through Ollama. I gave retries and provider fallback a shared deadline. If a circuit breaker is open, the gateway skips that provider and uses the remaining time to try a compatible one. [Read the fallback logic →](https://github.com/Ayushcv-46/ModelMux/blob/main/app/reliability/fallback.py)

### [RAG PDF Chatbot](https://github.com/Ayushcv-46/rag-pdf-chatbot)

A question can use different words from the PDF that answers it. I combine keyword and vector search, merge their rankings, then rerank the passages before the model answers across documents.

### [5-Agent Autonomous Research System](https://github.com/Ayushcv-46/5-Agent-Autonomous-Research-System)

Five agents turn a topic into a cited report. The part I like most is the handoff between critic and writer. The critic can send a draft back with specific issues, and the writer gets up to two revisions.

**More projects**

- [Intrusion Detection System](https://github.com/Ayushcv-46/intrusion-detection-system-ml) — I combined classifiers with soft voting and used SHAP to inspect their network-traffic predictions.
- [InterviewPal](https://github.com/Ayushcv-46/InterviewPal) — Mock interviews, technical trivia, and flashcards for interview practice.
- [Personal Expense Tracker](https://github.com/Ayushcv-46/Personal-Expense-tracker-) — An app for tracking transactions, category budgets, and monthly spending.

## Tech arsenal

**Agents & retrieval-augmented generation (RAG)**<br>
<img src="assets/tech/langgraph.svg" alt="LangGraph"> <img src="assets/tech/llamaindex.svg" alt="LlamaIndex"> <img src="assets/tech/chroma.svg" alt="Chroma"> <img src="assets/tech/hugging-face.svg" alt="Hugging Face">

**Backend & databases**<br>
<img src="assets/tech/fastapi.svg" alt="FastAPI"> <img src="assets/tech/postgresql.svg" alt="PostgreSQL"> <img src="assets/tech/redis.svg" alt="Redis"> <img src="assets/tech/sqlite.svg" alt="SQLite">

**Languages**<br>
<img src="assets/tech/python.svg" alt="Python"> <img src="assets/tech/cpp.svg" alt="C++"> <img src="assets/tech/javascript.svg" alt="JavaScript">

**Evaluation, testing & CI**<br>
<img src="assets/tech/ragas.svg" alt="Ragas"> <img src="assets/tech/pytest.svg" alt="pytest"> <img src="assets/tech/github-actions.svg" alt="GitHub Actions"> <img src="assets/tech/git.svg" alt="Git">

<details>
<summary><strong>Inside ModelMux · stack and 60-day roadmap</strong></summary>

- **In the gateway today** — Python, async FastAPI, Uvicorn, Pydantic, HTTPX, YAML routing, and provider adapters for Mock, Ollama, Gemini, and Groq. I use SQLAlchemy with SQLite for request and attempt records, and pytest for provider contracts and outage scenarios.
- **On the roadmap** — Redis token buckets with Lua, tenant-scoped response caching with expiry, PostgreSQL, a Chart.js metrics dashboard, Locust load tests, and a GitHub Actions pipeline with Ruff, pytest, and container checks.
- **After the core build** — The roadmap leaves room for OpenTelemetry traces, server-sent event streams, shared circuit-breaker state, performance-aware routing, and experiments with semantic caching.

</details>

## GitHub activity

<p>
  <a href="https://github.com/Ayushcv-46?tab=repositories"><img src="assets/activity/github.svg" width="354" alt="Public repositories, active days in the last 365 days, and contributions by week"></a>
  <a href="https://github.com/Ayushcv-46#contribution-activity"><img src="assets/activity/streak.svg" width="354" alt="Total Contributions, Current Streak, and Longest Streak from my public GitHub calendar"></a>
</p>

Both cards refresh daily from GitHub. Streaks count consecutive contribution dates since I joined. Today can still extend a streak that ran through yesterday. [View my contribution calendar →](https://github.com/Ayushcv-46#contribution-activity)

## Away from the keyboard

I drink black coffee every day and watch Real Madrid whenever I can. I also read philosophy, especially Albert Camus, Friedrich Nietzsche, and Swami Vivekananda.

> The fastest way for me to understand something is to build it.

If you’re building agents, evaluating language models, or hiring a backend intern, I’d love to hear from you. [Email me](mailto:ayushcv.tech@gmail.com) · [LinkedIn](https://www.linkedin.com/in/ayush-cv-6a68a233b/)
