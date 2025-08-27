flowchart TB
    subgraph Local [Local Operations]
        direction LR
        K[Working Directory] -->|git add| L[Staging Area]
        L -->|git commit| M[Local Repository]
    end
    
    subgraph Remote [Remote Operations]
        direction LR
        M -->|git push| N[GitHub]
        N -->|git fetch| O[Remote Refs]
        O -->|git merge| M
    end
    
    K -->|git status| K
    K -->|git diff| K
    M -->|git log| M