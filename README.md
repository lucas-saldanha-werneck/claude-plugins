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
- **[idea-shelf](https://github.com/lucas-saldanha-werneck/idea-shelf)**: a side shelf for ideas that come up mid-task. Jot them down without sidetracking Claude, then send the list in one click.
- **[plan-checklist](https://github.com/lucas-saldanha-werneck/plan-checklist)**: a plain checklist of Claude's plan beside the chat. Claude lists the steps first and ticks them off as it works.
- **[quiet-tools](https://github.com/lucas-saldanha-werneck/quiet-tools)**: one switch that hides the tool-call rows, so you read only Claude's answers and the plan.
- **[side-stack](https://github.com/lucas-saldanha-werneck/side-stack)**: one side pane that stacks the four above one under the other. Without it, each one opens its own tab.
- **[self-improve](https://github.com/lucas-saldanha-werneck/self-improve)**: reads your recent sessions, finds where you corrected Claude more than once, and proposes the change in `CLAUDE.md`, a skill or memory. Small fixes are applied alone; the rest wait for your OK.
- **[session-keeper](https://github.com/lucas-saldanha-werneck/session-keeper)**: restart your Mac, iTerm2 or a single Claude Code session without losing windows or conversations. It takes a snapshot, then reopens and resumes each session. macOS.
- **[remote-sessions](https://github.com/lucas-saldanha-werneck/remote-sessions)**: from the phone, open or resume a Claude Code session in another project folder in a new terminal window with Remote Control on, or fork the current session.
- **[session-archive](https://github.com/lucas-saldanha-werneck/session-archive)**: copies your conversations (a readable digest plus the full transcript) to a folder you choose, before Claude Code deletes old ones.

## Verification

- **[give-up-guard](https://github.com/lucas-saldanha-werneck/give-up-guard)**: when Claude ends a turn with "I didn't check X", hands the task back, or asks you for data it could find, it is sent back to check first.
- **[wait-loop-guard](https://github.com/lucas-saldanha-werneck/wait-loop-guard)**: blocks Bash `until`/`while` wait loops that have no deadline, so Claude can't hang forever.
- **[polish](https://github.com/lucas-saldanha-werneck/polish)**: a simplicity review of an app, page or code in the style of Linear or Apple Notes. It lists every change it would make with the gain and the risk, and changes nothing until you pick.

## Research

- **[llm-council](https://github.com/lucas-saldanha-werneck/llm-council)**: asks several LLMs from different vendors through OpenRouter. They answer in parallel, rank each other's answers anonymously, and a chairman model writes the final answer. Uses your OpenRouter credits. Its cross-review skill sends the same plan to the council and to Codex at the same time.

## Web

- **[web-unlock](https://github.com/lucas-saldanha-werneck/web-unlock)**: what to do when a normal fetch is blocked: steps by type of site, a record of what worked on each site, and rules before saying something does not exist.
- **[web-unlock-guard](https://github.com/lucas-saldanha-werneck/web-unlock-guard)**: stops Claude from retrying a blocked site with the same method, from using a headless browser on Cloudflare pages, and from opening a browser debug port without a separate profile.

## Desktop app

- **[handoff-terminal](https://github.com/lucas-saldanha-werneck/handoff-terminal)**: when the desktop app refuses a sign-in or personal-data step in the browser, a hidden terminal session does it and hands the result back.
- **[rc-auto](https://github.com/lucas-saldanha-werneck/rc-auto)**: turns Remote Control on for a desktop-app session when you type in it, and off again after 24 hours without a message from you.

## Mac

- **[mac-remote](https://github.com/lucas-saldanha-werneck/mac-remote)**: lets Claude see and control your Mac through Screen Sharing, even with the screen locked. Useful when you are away from the Mac. Read its warning before you install. It can also restart a Mac with FileVault without stopping at the disk password.
- **[launchd-agenda](https://github.com/lucas-saldanha-werneck/claude-agenda)**: schedule Claude Code sessions with launchd, so they run on your Mac with your own skills and hooks.

## Secrets

- **[op-secrets](https://github.com/lucas-saldanha-werneck/Claude-1Password)**: save and load secrets through 1Password without the values entering the chat.

## Command-line tools

These are not plugins. Each repo has an `install.sh`.

- **[stable-sync](https://github.com/lucas-saldanha-werneck/stable-sync)**: keeps a fixed-path copy of the `claude` and `op` programs, so macOS privacy permissions survive every update.
- **[meeting-copilot](https://github.com/lucas-saldanha-werneck/meeting-copilot)**: while the Muesli app records a meeting, shows suggestions, corrections and facts from Claude on a local page. macOS.

## License

Every plugin listed here is MIT licensed.

Built with Claude Code
