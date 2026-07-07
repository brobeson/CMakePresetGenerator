# Design

```mermaid
flowchart LR
  release
  debug
  build
  test-ci
  test-dev

  release --> build
  debug --> build

  build --> test-ci
  build --> test-dev

  %% release --> test-ci
  %% release --> test-dev
  %% debug --> test-ci
  %% debug --> test-dev
```

```mermaid
flowchart LR
  release --> build --> test-ci
  release --> build --> test-dev
  debug --> build --> test-ci
  debug --> build --> test-dev
```
