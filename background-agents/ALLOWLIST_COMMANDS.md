# Allowlist Commands and Tools for XFG STARK Project Management

## File & Directory Management
ls, ls -la, find, tree, cp, mv, rm, mkdir, rmdir, cat, head, tail, grep, sed, awk, touch, chmod, chown

## Code & Text Processing
rustc, cargo, rustup, clippy, rustfmt, grep -r, find . -name "*.rs", wc -l, wc -w, diff, patch, sort, uniq, cut, paste, tr, rev

## Git & Version Control
git status, git log, git diff, git add, git commit, git push, git pull, git branch, git checkout, git merge, git stash, git reset, git remote, git fetch

## Package & Dependency Management
pip, pip install, pip list, pip freeze, python, python3, virtualenv, venv, cargo build, cargo test, cargo check, cargo update, cargo tree, cargo doc, cargo clippy

## System & Process Management
ps, top, htop, kill, pkill, killall, nohup, screen, tmux, df, du, free, uname, whoami, hostname, date, time

## Network & API Tools
curl, wget, ping, traceroute, netstat, ssh, scp, rsync, curl -X POST, curl -H "Authorization", jq

## Monitoring & Logging
tail -f, less, more, journalctl, dmesg, watch, inotifywait, iostat, vmstat, sar

## Cryptographic & Security Tools
openssl, gpg, sha256sum, cryptsetup, luks, bandit, safety, cargo audit, rustsec, cargo-geiger

## STARK Proof & Zero-Knowledge Tools
cargo run --bin winterfell, cargo test --features stark, cargo run --bin proof-generator, cargo run --bin proof-verifier

## Code Quality & Analysis
cargo fmt, cargo clippy --fix, cargo test --verbose, cargo bench, black, isort, flake8, pre-commit, pre-commit run --all-files

## Real-time Monitoring
fswatch, inotify-tools, watch -n 1 'ls -la', htop, iotop, nethogs

## Debugging & Profiling
gdb, lldb, cargo build --debug, RUST_BACKTRACE=1 cargo run, perf, valgrind, cargo bench

## Build & Test Automation
make, cmake, cargo build --release, cargo test --all-features, github-cli, gitlab-cli, docker, docker-compose

## Background Process Management
systemctl, supervisor, screen, tmux, nohup, disown

## JSON & Data Processing
jq, jq '.field', jq -r '.field', python -m json.tool, awk '{sum+=$1} END {print sum}', sort | uniq -c | sort -nr

## Reporting & Documentation
cargo doc --open, rustdoc, mdbook, pandoc, markdown-pdf

## Critical Commands (Highest Priority)
cargo, rustc, clippy, rustfmt, git status, git log, git diff, git add, git commit, git push, git pull, ls, find, grep, cat, ps, kill, nohup, tail -f, watch, htop, curl, wget, cargo audit
