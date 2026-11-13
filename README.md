# lucas-tools

[![validate](https://github.com/lucas-saldanha-werneck/lucas-tools/actions/workflows/test.yml/badge.svg)](https://github.com/lucas-saldanha-werneck/lucas-tools/actions/workflows/test.yml)
[![License](https://img.shields.io/github/license/lucas-saldanha-werneck/lucas-tools)](LICENSE)

26 AI tools for Claude Code (skills, hooks, mods and commands): Claude checks its own work and learns from your corrections; sessions survive restarts and /clear, get archived before deletion, and open from your phone or a terminal; side panes for assumptions and ideas; secrets from password managers; Mac control even when locked; scheduled runs; multi-LLM opinions; blocked-site access.

Four of them in 30 seconds each. Tap a GIF to open the video; every plugin below has a demo link.

<table>
<tr>
<td align="center" width="50%"><a href="https://lucas-saldanha-werneck.github.io/save-clear/demo.mp4"><img src="https://github.com/user-attachments/assets/c69f7507-4d92-49b4-9298-57287662640e" alt="save-clear demo: tap to open the video" width="400"></a><br><b>save-clear</b>: saves and clears the context by itself</td>
<td align="center" width="50%"><a href="https://lucas-saldanha-werneck.github.io/remote-sessions/demo.mp4"><img src="https://github.com/user-attachments/assets/037e8588-4be3-4d88-a0a7-efb8556022c6" alt="remote-sessions demo: tap to open the video" width="400"></a><br><b>remote-sessions</b>: open any project from your phone</td>
</tr>
<tr>
<td align="center" width="50%"><a href="https://lucas-saldanha-werneck.github.io/plan-checklist/demo.mp4"><img src="https://github.com/user-attachments/assets/70d5ab70-c902-49df-be0b-27317ab021e9" alt="plan-checklist demo: tap to open the video" width="400"></a><br><b>plan-checklist</b>: Claude's plan, ticked off as it works</td>
<td align="center" width="50%"><a href="https://lucas-saldanha-werneck.github.io/assumptions-pane/demo.mp4"><img src="https://github.com/user-attachments/assets/3dc2d729-8aae-4bab-b8af-7f08c2ed2fce" alt="assumptions-pane demo: tap to open the video" width="400"></a><br><b>assumptions-pane</b>: mark each guess right or wrong</td>
</tr>
</table>

## Install

Add the catalog once:

```
/plugin marketplace add lucas-saldanha-werneck/lucas-tools
```

Then install the ones you want, for example:

```
/plugin install save-clear@lucas-tools
```

## Sessions

- **[save-clear](https://github.com/lucas-saldanha-werneck/save-clear)** ([demo](https://lucas-saldanha-werneck.github.io/save-clear/demo.mp4)): saves decisions and next steps, clears the context, and the next session starts from them. You stop managing context by hand.
- **[session-keeper](https://github.com/lucas-saldanha-werneck/session-keeper)** ([demo](https://lucas-saldanha-werneck.github.io/session-keeper/demo.mp4)): restart your Mac, iTerm2 or one Claude Code session without losing windows or conversations. It takes a snapshot, then reopens and resumes each session. macOS.
- **[remote-sessions](https://github.com/lucas-saldanha-werneck/remote-sessions)** ([demo](https://lucas-saldanha-werneck.github.io/remote-sessions/demo.mp4)): open, resume or fork Claude Code sessions on your computer from your phone, each in a new terminal window with Remote Control on, and move a session between the desktop app and a terminal.
- **[session-archive](https://github.com/lucas-saldanha-werneck/session-archive)** ([demo](https://lucas-saldanha-werneck.github.io/session-archive/demo.mp4)): copies each Claude Code conversation (a readable digest plus the full transcript) to an archive before Claude Code deletes old ones.
- **[rc-auto](https://github.com/lucas-saldanha-werneck/rc-auto)** ([demo](https://lucas-saldanha-werneck.github.io/rc-auto/demo.mp4)): turns Remote Control on when you type in a desktop-app session, and off after 24 idle hours.

## Side panes

- **[assumptions-pane](https://github.com/lucas-saldanha-werneck/assumptions-pane)** ([demo](https://lucas-saldanha-werneck.github.io/assumptions-pane/demo.mp4)): a side pane that lists each assumption Claude makes, so you can mark it right or wrong and catch a wrong guess early.
- **[idea-shelf](https://github.com/lucas-saldanha-werneck/idea-shelf)** ([demo](https://lucas-saldanha-werneck.github.io/idea-shelf/demo.mp4)): a side pane to park ideas mid-task without stopping Claude, then send them in one click.
- **[plan-checklist](https://github.com/lucas-saldanha-werneck/plan-checklist)** ([demo](https://lucas-saldanha-werneck.github.io/plan-checklist/demo.mp4)): Claude's plan as a checklist in a side pane, ticked off as it works.
- **[clean-view](https://github.com/lucas-saldanha-werneck/clean-view)** ([demo](https://lucas-saldanha-werneck.github.io/clean-view/demo.mp4)): one switch (`/quiet`) that hides the tool rows, so you read only the conversation.
- **[side-stack](https://github.com/lucas-saldanha-werneck/side-stack)** ([demo](https://lucas-saldanha-werneck.github.io/side-stack/demo.mp4)): one side pane where the four above stack, one under the other, instead of one tab each.

## Checks

- **[give-up-guard](https://github.com/lucas-saldanha-werneck/give-up-guard)** ([demo](https://lucas-saldanha-werneck.github.io/give-up-guard/demo.mp4)): sends Claude back to check when it ends with "didn't check", gives up, or asks you for data it could find.
- **[wait-loop-guard](https://github.com/lucas-saldanha-werneck/wait-loop-guard)** ([demo](https://lucas-saldanha-werneck.github.io/wait-loop-guard/demo.mp4)): blocks Bash wait loops with no deadline, so Claude can't hang forever.
- **[self-improve](https://github.com/lucas-saldanha-werneck/self-improve)** ([demo](https://lucas-saldanha-werneck.github.io/self-improve/demo.mp4)): finds where you corrected Claude more than once and proposes the fix in `CLAUDE.md`, a skill or memory. Small fixes apply alone; the rest wait for your OK.
- **[polish](https://github.com/lucas-saldanha-werneck/polish)** ([demo](https://lucas-saldanha-werneck.github.io/polish/demo.mp4)): a simplicity review in the style of Linear or Apple Notes: every change with its UX, DX and AX gain, applied only after you pick.
- **[llm-council](https://github.com/lucas-saldanha-werneck/llm-council)** ([demo](https://lucas-saldanha-werneck.github.io/llm-council/demo.mp4)): asks several LLMs through OpenRouter; they rank each other's answers and one writes the final answer. Uses your OpenRouter credits.
- **[plugin-dev-guard](https://github.com/lucas-saldanha-werneck/plugin-dev-guard)** ([demo](https://lucas-saldanha-werneck.github.io/plugin-dev-guard/demo.mp4)): stops Claude from editing the installed copy of a plugin, where the next update would wipe the change, and points it to your source repo, or to a fork and a pull request to the author. `plugin-dev-check` lists your repos next to their installed copies.
- **[side-notes](https://github.com/lucas-saldanha-werneck/side-notes)** ([demo](https://lucas-saldanha-werneck.github.io/side-notes/demo.mp4)): every few steps a side check looks for one thing you may have missed and shows it as a short note above the prompt.

## Web

- **[web-unlock](https://github.com/lucas-saldanha-werneck/web-unlock)** ([demo](https://lucas-saldanha-werneck.github.io/web-unlock/demo.mp4)): what Claude does when a web fetch is blocked: steps per site type and a record of what worked on each site.
- **[web-unlock-guard](https://github.com/lucas-saldanha-werneck/web-unlock-guard)** ([demo](https://lucas-saldanha-werneck.github.io/web-unlock-guard/demo.mp4)): stops Claude from retrying a blocked site the same way.

## Sign-in and secrets

- **[op-secrets](https://github.com/lucas-saldanha-werneck/op-secrets)** ([demo](https://lucas-saldanha-werneck.github.io/op-secrets/demo.mp4)): save and load secrets through 1Password without the values entering the chat.
- **[handoff-terminal](https://github.com/lucas-saldanha-werneck/handoff-terminal)** ([demo](https://lucas-saldanha-werneck.github.io/handoff-terminal/demo.mp4)): a terminal session does the sign-in steps the desktop app refuses, and hands the result back.

## Mac

- **[mac-remote](https://github.com/lucas-saldanha-werneck/mac-remote)** ([demo](https://lucas-saldanha-werneck.github.io/mac-remote/demo.mp4)): lets Claude see and control your Mac through Screen Sharing, even when it is locked. Read its warning before you install.
- **[launchd-agenda](https://github.com/lucas-saldanha-werneck/launchd-agenda)** ([demo](https://lucas-saldanha-werneck.github.io/launchd-agenda/demo.mp4)): schedules Claude Code sessions on your Mac with launchd, with your local skills and hooks.

## Scripts

- **[api-credit](https://github.com/lucas-saldanha-werneck/api-credit)** ([demo](https://lucas-saldanha-werneck.github.io/api-credit/demo.mp4)): runs `claude -p` scripts on your plan's monthly API credit first, and on the subscription when the API refuses, so the credit is used and no job stops when it ends.

## Command-line tools

These are not plugins. Each repo has an `install.sh`.

- **[stable-sync](https://github.com/lucas-saldanha-werneck/stable-sync)**: keeps a fixed-path copy of `op` (1Password CLI) so macOS permissions survive updates.
- **[meeting-copilot](https://github.com/lucas-saldanha-werneck/meeting-copilot)**: suggestions, corrections and facts from Claude while Muesli records a meeting. macOS.

## License

Every plugin listed here is MIT licensed.

Built with Claude Code
