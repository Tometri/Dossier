# Obsidian Vault (Dossier)

This is the Obsidian vault tracked in the Dossier GitHub repository for cross-device note-taking.

## Usage

### Sync between devices

There is no sync script in this repo — sync with plain git from the repo root:

```bash
cd ~/Documents/GitHub/Dossier
git pull
git add ObsidianVault
git commit -m "notes: <what changed>"
git push
```

### Daily Notes
Daily Notes: there is no Daily Notes folder in this repo yet — if the plugin is enabled, create one before relying on it.

## Structure
- `ComputerForensics/` - Computer forensics notes and labs

## Git Notes
- Always pull before starting work
- Commit and push after making changes
- Use meaningful commit messages

## Sync Script
The `~/scripts/dev/obsidian-sync.sh` script handles:
1. Pulling latest changes
2. Staging all changes
3. Committing with timestamp
4. Pushing to remote

Add to your shell profile:
```bash
alias hsync '~/scripts/dev/obsidian-sync.sh'
```