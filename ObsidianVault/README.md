# Obsidian Vault (Dossier)

This is the Obsidian vault tracked in the Dossier GitHub repository for cross-device note-taking.

## Usage

### Sync between devices
```bash
# From the vault directory
cd ~/Documents/GitHub/Dossier

# Manual sync
./scripts/dev/obsidian-sync.sh

# Or using hermes
hermes -t "Sync Obsidian vault to GitHub"
```

### Daily Notes
The vault has the Daily Notes plugin enabled. Notes are created in the daily notes folder.

## Structure
- `ComputerForensics/` - Computer forensics notes and labs
- `scripts/` - Obsidian-specific scripts

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