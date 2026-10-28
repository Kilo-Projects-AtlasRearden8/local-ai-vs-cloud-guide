# Choosing Models

Picking an AI model feels like picking a car: there are dozens of options,
they all have numbers nobody explains, and the wrong choice costs you time or
money. This section keeps it simple.

## The big split: local models vs. cloud models

- **Local models** run on your own computer. Nothing leaves your machine.
  Examples: models you download through Ollama or LM Studio.
- **Cloud models** run on someone else's servers. You send your text over the
  internet and get an answer back. Examples: the models behind popular chatbot
  websites and APIs.

This manual focuses on **local-first** because it needs no API key, no
account, and no subscription — but cloud still has its place, and we cover
when to use it later.

## Model sizes, in plain English

Models are sized by "parameters" — roughly, how many adjustable knobs the
model learned during training. You'll see them written with a "B" (billion).

| Size | Rough parameters | What it's good for | Typical RAM/VRAM need |
|------|------------------|--------------------|-----------------------|
| Small | 1B – 3B | Simple Q&A, rewriting, summaries, chat on old laptops | ~2–4 GB |
| Medium | 7B – 9B | Most everyday tasks: emails, docs, coding help, analysis | ~5–8 GB |
| Large | 13B – 35B | Harder reasoning, long documents, better coding | ~9–20 GB |
| Very large | 70B+ | Expert-level reasoning, complex code | ~40 GB+ |

**Beginner advice:** start with a 7B or 8B model (for example, a 7B or 8B
"instruct" or "chat" model). It runs well on most computers with 8–16 GB of
RAM and handles almost everything a beginner needs.

## Quantization: smaller files, almost the same smarts

You'll see names like `Q4_K_M`, `Q5_K_M`, or `fp16`. These describe how the
model is compressed.

- **fp16 / f16**: least compressed, biggest file, highest quality. Needs lots of memory.
- **Q4_K_M / Q4_0**: heavily compressed, much smaller file, quality is usually close enough for everyday use.
- **Q5_K_M / Q6_K**: middle ground — slightly bigger than Q4, slightly better quality.

**Beginner advice:** download `Q4_K_M` or `Q5_K_M` first. If answers feel
dull, try `Q6_K` or a larger model.

## Where to find models

- **Ollama Library** (ollama.com/library) — models ready to run with Ollama.
- **Hugging Face** (huggingface.co/models) — the biggest public model library;
  look for GGUF-format files if you plan to run them locally.
- **LM Studio** has a built-in model browser that downloads Hugging Face models
  for you.

## What to avoid as a beginner

- Don't start with a 70B+ model unless your computer has serious GPU memory
  (24 GB+ VRAM). It will be slow or won't run at all.
- Don't pay for a model subscription before you've tried a free local model.
- Don't worry about "the best" model — any small instruct model will teach you
  how local AI works.

## A first model to try

If you're using Ollama: `ollama run llama3.2:3b` (small, fast, good for
learning) or `ollama run llama3.1:8b` (smarter, still runs on most laptops).

If you're using LM Studio: search the built-in browser for "Llama 3.2 3B
Instruct GGUF" or "Llama 3.1 8B Instruct GGUF" and download a Q4_K_M file.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `../LICENSE`.
