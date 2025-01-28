import sys
from PIL import Image
from math import ceil
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

def convert_image_to_pdf(image_path, output_pdf):
    img = Image.open(image_path)
    img_width, img_height = img.size
    print(f"Original image dimensions: {img_width}x{img_height}")

    # Calculate dimensions for 2-column layout
    page_width, page_height = A4
    pdf_col_width = page_width / 2

    # Calculate scaling factor to fit image in one column
    scale_factor = pdf_col_width / img_width
    new_width = int(img_width * scale_factor)
    new_height = int(img_height * scale_factor)

    # Resize image to fit column width
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Calculate segment height (use full page height)
    segment_height = int(page_height)
    num_segments = ceil(new_height / segment_height)
    print(f"Splitting into {num_segments} segments of approximately {segment_height} pixels height")

    # Create segments
    segments = []
    for i in range(num_segments):
        y_start = i * segment_height
        y_end = min((i + 1) * segment_height, new_height)
        segment = img.crop((0, y_start, new_width, y_end))
        segments.append(segment)

    # Calculate number of pages needed (2 segments per page)
    num_pages = ceil(len(segments) / 2)
    print(f"Creating {num_pages} pages with 2 segments per page")

    c = canvas.Canvas(output_pdf, pagesize=A4)

    for page in range(num_pages):
        c.setPageSize(A4)
        
        # Process two segments for this page
        for col in range(2):
            segment_idx = page * 2 + col
            if segment_idx < len(segments):
                segment = segments[segment_idx]
                x_pos = col * pdf_col_width
                
                # Draw segment
                c.drawImage(
                    ImageReader(segment),
                    x_pos,
                    0,
                    width=pdf_col_width,
                    height=page_height,
                    preserveAspectRatio=True,
                    mask='auto'
                )
        
        c.showPage()

    c.save()
    print(f"Created PDF with {num_pages} pages ({len(segments)} segments in 2x2 grid layout)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python screenshot_to_pdf.py <input_image> <output_pdf>")
        sys.exit(1)
    
    convert_image_to_pdf(sys.argv[1], sys.argv[2])