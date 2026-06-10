# SSH Brute-Force Monitor

A Python script that detects SSH brute-force attacks using a sliding time window,
tracking failed login attempts per IP address in real-time.

## How it works

Unlike simple attempt counters, this script uses a **5-minute sliding window**.
Each failed login attempt is timestamped, and only attempts within the last
300 seconds are counted. This means:

- Old attempts automatically expire and fall out of the window
- Detection stays accurate over long-running sessions
- A successful login from an IP clears its entire history

## Detection logic

- Monitors port 22 only
- Tracks failed attempts per source IP with timestamps
- Flags brute-force when multiple failures occur within a 5-minute window
- Resets an IP's history on successful login

## Requirements

- Python 3.x
- No additional packages needed

## Usage

```bash
python ssh_monitor.py
```

## Related project

For a version that monitors the Windows OpenSSH event log in real-time,
see [ssh-intrusion-detection-homelab](https://github.com/Beji239/ssh-intrusion-detection-homelab)
