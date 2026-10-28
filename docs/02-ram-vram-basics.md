# RAM and VRAM Basics

To run AI locally you need two things to understand: **RAM** (your computer's
general working memory) and **VRAM** (memory on your graphics card, if you
have one). This section explains both in plain English and how to tell what
your computer has.

## RAM vs. VRAM

| | What it is | Where it lives | What AI uses it for |
|---|------------|----------------|---------------------|
| **RAM** | Main system memory | On the motherboard / CPU chips | Running the model, your OS, apps |
| **VRAM** | Graphics card memory | On the GPU (graphics card) | Running the model faster, if available |

If your computer has a graphics card with VRAM, AI can use it and run much
faster. If not, AI runs on RAM and the CPU — slower, but still perfectly
usable for small models.

## How to check what you have

### Windows

1. Press `Ctrl + Shift + Esc` to open Task Manager.
2. Click the **Performance** tab.
3. **Memory** shows your total RAM and how much is in use.
4. **GPU** shows your graphics card and its dedicated memory (VRAM).

### macOS

1. Click the Apple menu → **About This Mac** → **More Info** / **System Report**.
2. **Memory** shows total RAM. On Apple Silicon (M1/M2/M3/M4 Macs), RAM and
   VRAM are shared — the system can use RAM for graphics, which is great for
   local AI.
3. Or in Terminal: `sysctl -n hw.memsize` shows total RAM in bytes.

### Linux

1. RAM: `free -h`
2. GPU/VRAM: `lspci | grep -i vga` or `nvidia-smi` if you have an NVIDIA card.

## How much memory do you need?

A rough rule: a model needs about **1 byte per parameter**, plus some overhead.
So a 7B parameter model needs roughly 7–9 GB of free memory to run
comfortably.

| Free memory (RAM or VRAM) | Comfortable model size | What it runs well |
|---------------------------|------------------------|-------------------|
| 4 GB | 1B – 3B (Q4) | Simple chat, rewriting, summaries |
| 8 GB | 7B – 8B (Q4/Q5) | Everyday AI: emails, docs, coding help |
| 16 GB | 13B – 14B (Q4/Q5) | Stronger reasoning, longer documents |
| 24 GB+ | 33B – 70B (Q4) | Advanced reasoning, complex coding |

These are estimates. Your operating system and browser also use RAM, so leave
a couple of gigabytes free.

## What slows things down

- **Not enough free memory:** the computer swaps to disk, and AI gets very
  slow. Close other apps before running a big model.
- **No GPU/VRAM:** CPU-only is fine for small models, but responses take
  longer (seconds to minutes instead of under a second).
- **Large context:** feeding the model very long documents uses more memory.

## Practical tips

1. Close browser tabs and heavy apps before loading a model.
2. Start with a small quantized model (Q4_K_M, 3B–8B).
3. If your computer has 8 GB of RAM, stick to 3B–7B models at first.
4. On a Mac with unified memory, local AI often works better than on a
   Windows PC with the same RAM number, because the graphics chip can share
   the same memory.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `../LICENSE`.
