# Harbor Terminal-Bench Task Fix

This repository contains the repaired version of the **Dynamo - Fix the Broken Terminal-Bench Task**.

## Changes Made

- Fixed `task.toml` to use the correct Harbor format.
- Corrected the Docker environment and removed the leaked solution.
- Rewrote `instruction.md` with clear success criteria.
- Improved the verifier to validate actual output values.
- Updated `test.sh` to generate `reward.txt` and `ctrf.json`.
- Verified:
  - Oracle agent returns **Reward = 1.0**
  - NOP agent returns **Reward = 0.0**

## Repository Structure

```
environment/
solution/
tests/
instruction.md
task.toml
```

This repository was created as part of the Project Dynamo Harbor task repair assessment.
