# Cloud-Devops-Journey
A structured journal documenting my hands-on DevOps learning path —  covering Linux, Python scripting, CI/CD pipelines, containerization,  and cloud infrastructure. Updated weekly.



File compression scripts(pdf)
_____________________________________________________________________________________________________________________________

# Python PDF Compressor

A dynamic, automated Python utility built using `pypdf` and `Pillow` to reduce PDF file sizes down to a target limit (e.g., <= 260 KB). 

It progressively optimizes page content streams, downsamples image resolutions, reduces JPEG quality, and strips unreferenced PDF objects until the target threshold is met.

---

##  Features

- **Target-Driven Compression:** Automatically runs iterative passes adjusting quality and scaling down image dimensions until the file fits your desired target size.
- **Cross-Platform & WSL Compatible:** Native support for Windows and Linux environments (WSL), with automated path detection to export compressed files directly to your Windows Desktop.
- **Object Deduplication:** Removes duplicate and unreferenced streams (`compress_identical_objects`) to yield smaller file sizes without corrupting document structure.

---

##  Prerequisites & Environment Setup

This project requires **Python 3.10+** (tested on Python 3.14 under WSL Ubuntu).

### 1. Set Up Virtual Environment

To comply with **PEP 668** (externally managed environment protections in modern Linux/WSL distros), set up a localized virtual environment:

```bash
# Install venv package if not present (Ubuntu/Debian)
sudo apt update && sudo apt install python3-venv -y

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate





### 1. subprocess module
How to run shell commands directly from Python —
replacing bash with cleaner, more controllable Python code.

**Key methods learned:**
- `subprocess.run()` — run a command and wait for it
- `capture_output=True` — grab the command's output
- `result.returncode` — check if command succeeded or failed
- `result.stdout` — read the output as text
- `result.stderr` — read any error messages

**Example I wrote:**
```python
import subprocess

# same as typing: ls -l in terminal
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)  # 0 = success
```

**Real use case:**
Running system commands, automating deployments,
checking server status — all from inside a Python script.

---

### 2. File Operations
Reading, writing, and managing files using Python
instead of manual terminal commands.

**Key concepts learned:**
- `open()` — open a file for reading or writing
- `read()` / `write()` — get or put content in a file
- `with` statement — safely handles closing files automatically
- `os.path.exists()` — check if a file exists before touching it
- `shutil.copy()` / `shutil.move()` — copy and move files

**Example I wrote:**
```python
# Writing to a file
with open('log.txt', 'w') as f:
    f.write('Script started\n')

# Reading from a file
with open('log.txt', 'r') as f:
    print(f.read())
```

**Real use case:**
Reading config files, writing logs,
processing data files — core to any automation script.

---

### 3. Combining Both — subprocess + file ops
```python
import subprocess

# Run a command and save output to a file
result = subprocess.run(['df', '-h'], capture_output=True, text=True)

with open('disk_usage.log', 'w') as f:
    f.write(result.stdout)

print("Disk usage saved to disk_usage.log")
```

---

## Key Takeaways
- subprocess replaces the need to write pure bash scripts
- Always use `capture_output=True` when you need the output
- Always use `with open()` — it closes the file automatically
- Check `returncode` to handle errors properly

## What I Want to Build Next
- [ ] A script that runs system checks and logs results to a file
- [ ] A script that monitors a folder and logs new files added
- [ ] A deployment script using subprocess to pull from GitHub

