# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:41:57 2026

@author: bejir
"""

import time  # Gives us time.time() = seconds since 1970

# NEW STRUCTURE: { ip: [timestamp, timestamp, ...] }
ssh_attempts = {}  
TIME_WINDOW = 300  # 300 seconds = 5 minutes

def check_ssh_login(ip_address, port, success):
    if port != 22:
        return "INFO: Not SSH"
    
    current_time = time.time()  # Get "now" as a big number
    
    if success == True:
        # RESET LOGIC: successful login wipes the history
        if ip_address in ssh_attempts:
            del ssh_attempts[ip_address]  # forget this IP completely
        return "INFO: SSH Login OK"
    
    # success == False from here down
    
    # Step 1: Make sure IP has a list. If not, create empty list.
    if ip_address not in ssh_attempts:
        ssh_attempts[ip_address] = []
    
    # Step 2: Add current timestamp to this IP's list
    ssh_attempts[ip_address].append(current_time)
    
    # Step 3: Remove old timestamps outside the 5-min window
    # Keep only times where: current_time - old_time <= 300
    ssh_attempts[ip_address] = [t for t in ssh_attempts[ip_address] if current_time - t <= TIME_WINDOW]
    
    # Step 4: Count how many fails are left in the window
    fail_count = len(ssh_attempts[ip_address])
    
    if fail_count > 5:
        return f"HIGH: SSH Brute-Force - {fail_count} fails in 5min"
    else:
        return f"INFO: SSH fail count {fail_count} in 5min"

# Test: Simulate 7 fails all at once
for i in range(7):
    print(check_ssh_login("192.168.1.5", 22, False))

print("\nFinal dict:", ssh_attempts)
