import os
import subprocess
import platform

def run_sentinel_scan():
    current_os = platform.system()
    print(f"--- [SENTINEL AGENT] Operating System detected: {current_os} ---")
    
    if current_os == "Windows":
        print("[*] Scanning Windows processes for Python instances...")
        # THIS IS THE CMD LINE INSIDE THE CODE:
        cmd = "tasklist | findstr /i \"python\"" 
    else:
        print("[*] Scanning Linux processes...")
        cmd = "ps -eo pid,%mem,comm --sort=-%mem | head -n 3"

    try:
        output = subprocess.check_output(cmd, shell=True).decode()
        print(f"Current System State:\n{output}")
        
        fix_script = "optimize_system.sh" if current_os != "Windows" else "optimize_system.bat"
        
        with open(fix_script, "w") as f:
            if current_os == "Windows":
                f.write("@echo off\necho Sentinel Agent: Optimizing Windows System...\npause")
            else:
                f.write("#!/bin/bash\necho Sentinel Agent: Optimizing Linux System...\n")

        if current_os != "Windows":
            os.chmod(fix_script, 0o755)
            
        print(f"\n[SUCCESS] Agentic workflow complete. '{fix_script}' created.")
        
    except Exception as e:
        print(f"[ERROR] System scan failed: {e}")

if __name__ == "__main__":
    run_sentinel_scan()