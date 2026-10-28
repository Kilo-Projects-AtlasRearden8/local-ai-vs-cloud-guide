# Ollama Setup

Ollama is a free, open-source tool that downloads and runs AI models on your
computer. It works from the command line, needs no account, and needs no API
key. This section walks you through installing it, running your first model,
and a few everyday commands.

## What Ollama does

- Downloads models from its public library
- Runs them locally on your computer
- Keeps your conversations on your machine — nothing is sent to Ollama's
  servers when you chat with a local model

## Step 1: Install Ollama

### Windows

1. Go to [ollama.com](https://ollama.com) and click **Download**.
2. Run the installer and follow the prompts.
3. Open a new Command Prompt or PowerShell window and type `ollama`. If you see
   usage text, you're ready.

### macOS

1. Go to [ollama.com](https://ollama.com) and click **Download** (or in
   Terminal: `brew install ollama` if you use Homebrew).
2. Follow the installer prompts.
3. Open Terminal and type `ollama`.

### Linux

1. Run the install script:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
2. Start the service:
   ```bash
   systemctl start ollama
   systemctl enable ollama
   ```
3. Type `ollama` in the terminal to verify.

## Step 2: Run your first model

```bash
ollama run llama3.2:3b
```

The first time, Ollama downloads the model (a few hundred megabytes to a few
gigabytes depending on size). After that, it starts instantly.

Type a message and press Enter. Type `/bye` to exit.

## Step 3: Try a smarter model

If your computer has 8–16 GB of RAM:

```bash
ollama run llama3.1:8b
```

This model is larger and more capable but still runs on most laptops.

## Useful everyday commands

| Command | What it does |
|---------|--------------|
| `ollama list` | Shows models downloaded on your computer |
| `ollama pull <model>` | Downloads a model without starting a chat |
| `ollama run <model>` | Starts a chat with a model |
| `ollama rm <model>` | Deletes a model to free disk space |
| `ollama ps` | Shows models currently loaded in memory |
| `ollama stop <model>` | Unloads a model from memory |

Example:

```bash
ollama list
ollama pull llama3.1:8b
ollama run llama3.1:8b "Write a short bedtime story for a nurse."
```

## Running Ollama in the background

Ollama runs as a background service after installation, so models stay
available. You can close the terminal; Ollama keeps running. Use
`ollama serve` only if you need to run it manually.

## Uninstalling

- Windows: uninstall Ollama from Settings → Apps.
- macOS: drag Ollama from Applications to the Trash.
- Linux: remove the package you installed (e.g. `sudo apt remove ollama`).

Models are stored in `~/.ollama` and can be deleted separately to free space.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `../LICENSE`.
