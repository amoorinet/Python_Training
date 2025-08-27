# Git Flow – One Page

> Both diagrams below render on GitHub. Each diagram is in its own `mermaid` block.

## 1) Local ↔ Remote (Add → Commit → Push)

```mermaid
flowchart TD
    A[Your Working Folder on PC] -->|git add .| B[Staging Area (local index)]
    B -->|git commit -m "msg"| C[Local Git Repository (history on your PC)]
    C -->|git push| D[Remote Repository (GitHub)]
```

## 2) Getting Updates from GitHub (Fetch → Pull)

```mermaid
flowchart TD
    D[Remote Repository (GitHub)] -->|git fetch| E[Remote Tracking Branch (origin/main)]
    E -->|git pull (fetch + merge)| C[Local Git Repository + Working Folder updated]
```

---

### Quick Reference
- `git add .` → stage changes  
- `git commit -m "msg"` → save snapshot locally  
- `git push` → upload commits to GitHub  
- `git fetch` → download updates without changing files  
- `git pull` → fetch + merge (apply updates)
