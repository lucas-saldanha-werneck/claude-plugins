# claude-plugins

The Claude Code plugins I use every day. Each one lives in its own repo with its own README; this repo lists them.

## Install

Add the catalog once:

```
/plugin marketplace add lucas-saldanha-werneck/claude-plugins
```

Then install the ones you want, for example:

```
/plugin install save-clear@lucas-plugins
```

## Sessions

- **[save-clear](https://github.com/lucas-saldanha-werneck/save-clear)**: saves decisions and next steps, clears the context, and the next session starts from them. You stop managing context by hand.
- **[session-keeper](https://github.com/lucas-saldanha-werneck/session-keeper)**: restart your Mac, iTerm2 or one Claude Code session without losing windows or conversations. It takes a snapshot, then reopens and resumes each session. macOS.
- **[remote-sessions](https://github.com/lucas-saldanha-werneck/remote-sessions)**: open, resume or fork Claude Code sessions on your computer from your phone, each in a new terminal window with Remote Control on.
- **[session-archive](https://github.com/lucas-saldanha-werneck/session-archive)**: copies each Claude Code conversation (a readable digest plus the full transcript) to an archive before Claude Code deletes old ones.
- **[rc-auto](https://github.com/lucas-saldanha-werneck/rc-auto)**: turns Remote Control on when you type in a desktop-app session, and off after 24 idle hours.

## Side panes

- **[assumptions-pane](https://github.com/lucas-saldanha-werneck/assumptions-pane)**: a side pane that lists each assumption Claude makes, so you can mark it right or wrong and catch a wrong guess early.
- **[idea-shelf](https://github.com/lucas-saldanha-werneck/idea-shelf)**: a side pane to park ideas mid-task without stopping Claude, then send them in one click.
- **[plan-checklist](https://github.com/lucas-saldanha-werneck/plan-checklist)**: Claude's plan as a checklist in a side pane, ticked off as it works.
- **[clean-view](https://github.com/lucas-saldanha-werneck/clean-view)**: one switch (`/quiet`) that hides the tool rows, so you read only the conversation.
- **[side-stack](https://github.com/lucas-saldanha-werneck/side-stack)**: one side pane where the four above stack, one under the other, instead of one tab each.

## Checks

- **[give-up-guard](https://github.com/lucas-saldanha-werneck/give-up-guard)**: sends Claude back to check when it ends with "didn't check", gives up, or asks you for data it could find.
- **[wait-loop-guard](https://github.com/lucas-saldanha-werneck/wait-loop-guard)**: blocks Bash wait loops with no deadline, so Claude can't hang forever.
- **[self-improve](https://github.com/lucas-saldanha-werneck/self-improve)**: finds where you corrected Claude more than once and proposes the fix in `CLAUDE.md`, a skill or memory. Small fixes apply alone; the rest wait for your OK.
- **[polish](https://github.com/lucas-saldanha-werneck/polish)**: a simplicity review in the style of Linear or Apple Notes: every change with its UX, DX and AX gain, applied only after you pick.
- **[llm-council](https://github.com/lucas-saldanha-werneck/llm-council)**: asks several LLMs through OpenRouter; they rank each other's answers and one writes the final answer. Uses your OpenRouter credits.
- **[plugin-dev-guard](https://github.com/lucas-saldanha-werneck/plugin-dev-guard)**: stops Claude from editing the installed copy of a plugin, where the next update would wipe the change, and points it to your source repo, or to a fork and a pull request to the author. `plugin-dev-check` lists your repos next to their installed copies.

## Web

- **[web-unlock](https://github.com/lucas-saldanha-werneck/web-unlock)**: what Claude does when a web fetch is blocked: steps per site type and a record of what worked on each site.
- **[web-unlock-guard](https://github.com/lucas-saldanha-werneck/web-unlock-guard)**: stops Claude from retrying a blocked site the same way.

## Sign-in and secrets

- **[op-secrets](https://github.com/lucas-saldanha-werneck/op-secrets)**: save and load secrets through 1Password without the values entering the chat.
- **[handoff-terminal](https://github.com/lucas-saldanha-werneck/handoff-terminal)**: a terminal session does the sign-in steps the desktop app refuses, and hands the result back.

## Mac

- **[mac-remote](https://github.com/lucas-saldanha-werneck/mac-remote)**: lets Claude see and control your Mac through Screen Sharing, even when it is locked. Read its warning before you install.
- **[launchd-agenda](https://github.com/lucas-saldanha-werneck/launchd-agenda)**: schedules Claude Code sessions on your Mac with launchd, with your local skills and hooks.

## Command-line tools

These are not plugins. Each repo has an `install.sh`.

- **[stable-sync](https://github.com/lucas-saldanha-werneck/stable-sync)**: keeps a fixed-path copy of `claude` and `op` so macOS permissions survive updates.
- **[meeting-copilot](https://github.com/lucas-saldanha-werneck/meeting-copilot)**: suggestions, corrections and facts from Claude while Muesli records a meeting. macOS.

## License

Every plugin listed here is MIT licensed.

Built with Claude Code
