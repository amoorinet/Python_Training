flowchart LR
  %% Grouping for clarity
  subgraph Local_PC[Local PC]
    A[Working Folder]
    B[Staging Area]
    C[Local Repository]
    E[Remote Tracking Branch<br>origin/main]
  end

  subgraph Remote[GitHub Remote]
    D[Remote Repository]
  end

  %% Upwards: create & publish
  A -- git add --> B
  B -- git commit --> C
  C -- git push --> D

  %% Downwards: preview & update
  D -- git fetch --> E
  E -- git pull<br>merge/rebase --> C
  C -- checkout --> A