flowchart LR
    A[Working Folder] -->|git add| B[Staging Area]
    B -->|git commit| C[Local Repository]
    C -->|git push| D[Remote GitHub]
    D -->|git fetch| E[Remote Tracking Branch (origin/main)]
    E -->|git pull (merge)| C
    C -->|checkout| A
