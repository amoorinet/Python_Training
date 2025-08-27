flowchart LR
    A[Working Folder] -->|git add| B[Staging Area]
    B -->|git commit| C[Local Repository]
    C -->|git push| D[Remote GitHub]
    D -->|git fetch| E[Origin Branch]
    E -->|git pull| A

flowchart TD
    A[Untracked Files] -->|git add| B[Staged Changes]
    B -->|git commit| C[Committed]
    C -->|git push| D[On GitHub]
    D -->|git fetch| E[Updates Available]
    E -->|git pull| A

flowchart TB
    subgraph Local [Local Operations]
        direction LR
        A[Working Directory] -->|git add| B[Staging Area]
        B -->|git commit| C[Local Repository]
    end
    
    subgraph Remote [Remote Operations]
        direction LR
        C -->|git push| D[GitHub]
        D -->|git fetch| E[Remote Refs]
        E -->|git merge| C
    end
    
    A -->|git status| A
    A -->|git diff| A
    C -->|git log| C