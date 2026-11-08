# claude-plugins

The Claude Code plugins I use every day, in one catalog. Each plugin lives in its own repo with its own README; this repo only lists them, so you can add them all with one command.

## Install

Add the catalog once:

```
/plugin marketplace add lucas-saldanha-werneck/claude-plugins
```

Then install the ones you want, for example:

```
/plugin install save-clear@lucas-plugins
```

## Session

- **[save-clear](https://github.com/lucas-saldanha-werneck/save-clear)**: saves decisions and next steps to a snapshot, clears the session, and the next session starts from the snapshot. You stop managing context by hand.
- **[assumptions-pane](https://github.com/lucas-saldanha-werneck/assumptions-pane)**: a side pane where Claude logs each assumption it makes. You mark each one right or wrong, so a wrong guess gets caught early.

## Verification

- **[give-up-guard](https://github.com/lucas-saldanha-werneck/give-up-guard)**: when Claude ends a turn with "I didn't check X", hands the task back, or asks you for data it could find, it is sent back to check first.
- **[wait-loop-guard](https://github.com/lucas-saldanha-werneck/wait-loop-guard)**: blocks Bash `until`/`while` wait loops that have no deadline, so Claude can't hang forever.

## Web

- **[web-unlock-guard](https://github.com/lucas-saldanha-werneck/web-unlock-guard)**: stops Claude from retrying a blocked site with the same method, from using a headless browser on Cloudflare pages, and from opening a browser debug port without a separate profile.

## Desktop app

- **[handoff-terminal](https://github.com/lucas-saldanha-werneck/handoff-terminal)**: when the desktop app refuses a sign-in or personal-data step in the browser, a hidden terminal session does it and hands the result back.

## Secrets

- **[op-secrets](https://github.com/lucas-saldanha-werneck/Claude-1Password)**: save and load secrets through 1Password without the values entering the chat.

## License

Every plugin listed here is MIT licensed.

Built with Claude Code
