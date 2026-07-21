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
