# LM Studio Setup

LM Studio is a free desktop app with a visual interface for finding,
downloading, and running AI models locally. It's a great choice if you prefer
clicking buttons over typing commands. No account, no API key required.

## What LM Studio does

- Browses and downloads models from Hugging Face
- Runs models locally on your computer
- Lets you chat with models, compare them side by side, and run a local API
  server for other tools
- Keeps your data on your machine unless you explicitly connect to a cloud
  service

## Step 1: Install LM Studio

1. Go to [lmstudio.ai](https://lmstudio.ai) and download the installer for
   Windows, macOS, or Linux.
2. Install it like any other app.
3. Open LM Studio. The first run may ask to download a small starter model —
   you can accept or skip it.

## Step 2: Download a model

1. Click the **Discover** or search icon in the left sidebar.
2. Search for a beginner-friendly model, for example:
   - `Llama 3.2 3B Instruct`
   - `Llama 3.1 8B Instruct`
3. Pick a result labeled **GGUF** (that's the format LM Studio runs best).
4. Choose a quantization — `Q4_K_M` is a good default — and click **Download**.

While it downloads, you can keep using the app.

## Step 3: Start chatting

1. Click the **Chat** icon in the left sidebar.
2. At the top of the chat pane, choose the model you just downloaded from the
   model dropdown.
3. Type your message and press Enter.

## Step 4: Adjust settings (optional)

- **Context length:** how much text the model remembers. Default is fine for
  most chats; raise it if you're feeding long documents.
- **Temperature:** randomness. Lower (0.3–0.7) for focused answers; higher
  (0.8–1.2) for creative writing.

## Comparing models side by side

LM Studio lets you open two chat panes with different models and send the same
prompt to both — a handy way to see which model you prefer without installing
anything extra.

## Local API server (advanced, optional)

LM Studio can start a local server at `http://localhost:1234` that other
programs can talk to. You don't need this for beginner use, but it's there if
you want to connect other tools later. Turn it on from the **Developer** or
local server section of the app.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `../LICENSE`.
