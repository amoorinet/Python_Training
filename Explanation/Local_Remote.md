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

