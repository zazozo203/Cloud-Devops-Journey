import os
import sys
from pypdf import PdfReader, PdfWriter
from PIL import Image

def get_desktop_path():
    """Detect Windows Desktop path when running inside WSL or standard environments."""
    # WSL path to Windows Desktop
    wsl_desktop_lower = "/mnt/c/Users/zazozo/desktop"
    wsl_desktop_upper = "/mnt/c/Users/zazozo/Desktop"
    
    if os.path.exists(wsl_desktop_upper):
        return wsl_desktop_upper
    elif os.path.exists(wsl_desktop_lower):
        return wsl_desktop_lower
    
    # Standard home desktop fallback
    home_desktop = os.path.expanduser("~/Desktop")
    if os.path.exists(home_desktop):
        return home_desktop
        
    # Current folder fallback
    return os.getcwd()

def compress_pdf_to_target(input_path, output_filename="Birth_compressed.pdf", target_kb=260):
    target_bytes = target_kb * 1024
    desktop_dir = get_desktop_path()
    output_path = os.path.join(desktop_dir, output_filename)
    
    # Starting parameters
    quality = 70
    scale_factor = 1.0

    print(f"Targeting file size: <= {target_kb} KB...")
    print(f"Output destination: {output_path}")

    for attempt in range(1, 10):
        reader = PdfReader(input_path)
        writer = PdfWriter()

        # Step 1: Transfer pages
        for page in reader.pages:
            writer.add_page(page)

        # Step 2: Compress streams and downsample images
        for page in writer.pages:
            page.compress_content_streams(level=9)
            
            try:
                for img_obj in page.images:
                    pil_img = img_obj.image
                    
                    if pil_img.mode != "RGB":
                        pil_img = pil_img.convert("RGB")
                    
                    if scale_factor < 1.0:
                        new_width = int(pil_img.width * scale_factor)
                        new_height = int(pil_img.height * scale_factor)
                        pil_img = pil_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    
                    img_obj.replace(pil_img, quality=quality)
            except Exception:
                pass

        # Step 3: Strip unreferenced objects and save
        writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)

        with open(output_path, "wb") as f:
            writer.write(f)

        current_size = os.path.getsize(output_path)
        print(f"Attempt {attempt}: Size = {current_size / 1024:.2f} KB (Quality={quality}, Scale={scale_factor:.2f})")

        if current_size <= target_bytes:
            print(f" Success! Saved compressed file ({current_size / 1024:.2f} KB) to Desktop.")
            return

        # Lower quality and scale factor dynamically
        quality = max(10, quality - 15)
        if quality <= 25:
            scale_factor *= 0.75

    print(f" Done! Saved to Desktop at {os.path.getsize(output_path) / 1024:.2f} KB.")

if __name__ == "__main__":
    compress_pdf_to_target("CamScanner 07-21-2026 11.39.pdf", "localgvt.pdf", target_kb=260)