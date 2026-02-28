# 🛡️ OMEGA SYSTEM BACKUP REGISTRY

**Backups are handled remotely to keep this workspace lightweight.**

### 🌐 GitHub Repository
[https://github.com/edsworld27/omega-backup](https://github.com/edsworld27/omega-backup)

### ⚙️ Automation Strategy
- **Interval**: Every 5 minutes (300 seconds).
- **Process**: 
    1. System generates a fractal snapshot.
    2. Snapshot is committed to the GitHub repository.
    3. Local `.zip` is instantly purged to save disk space.
- **Daemon**: Managed by `omega-ignite.py` -> `omega-backup.py watch`.

---
*This directory is managed by the Omega Backup Protocol. Manual zips should not be stored here.*
