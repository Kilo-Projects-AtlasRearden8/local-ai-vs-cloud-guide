# Privacy Benefits

One of the best reasons to run AI locally is privacy: your conversations,
documents, and questions stay on your computer. This section explains what
that means, what it doesn't mean, and how to stay safe.

## What "local" means for privacy

When you run a model with Ollama or LM Studio:

- Your text never leaves your computer to reach the model.
- No company reads your chats to train their models.
- No account is tied to your conversations.
- No internet connection is needed after the model is downloaded.
- You can delete a model or a chat anytime, and it's gone from your machine.

This makes local AI a good fit for personal journals, draft business letters,
client notes, health-related questions (for education, not medical advice),
and anything you wouldn't want posted online.

## What local AI does NOT protect you from

Local AI is private, but it is not magic security:

- **Malware:** only download models from trusted sources (Ollama's library,
  Hugging Face, LM Studio's built-in browser). Don't run random model files
  from strangers.
- **Your computer's security:** if someone else can log into your computer,
  they can read your local chat history. Use a login password and lock your
  screen.
- **Backups:** if you back up your computer to a cloud service, your chat
  history may be included in that backup. Check what your backup tool saves.
- **Outputs you choose to share:** copying an AI answer into an email or
  website sends it wherever that email or website goes.

## Cloud AI: the trade-off

Cloud AI services are convenient and often more powerful, but they usually:

- Require an account and sometimes a credit card.
- Send your text to the provider's servers.
- May use your inputs to train future models (check their settings; many let
  you opt out).
- Keep logs of your conversations for some period of time.

Cloud is fine for public information and casual use. For personal, client, or
business-sensitive material, local-first is the safer default.

## A simple privacy rule

> If you wouldn't read it out loud in a public place, run it locally.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `../LICENSE`.
