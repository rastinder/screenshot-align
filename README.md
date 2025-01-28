# Screenshot Grid PDF Converter

A Python utility that converts long screenshots into printer-friendly A4 PDFs by splitting them into a 2-column grid layout. Perfect for converting long web pages, chat conversations, or code snippets into printable documents.

## Example Input/Output

### Input: Long Screenshot
```
+------------------+
|                  |
|     Content      |
|       1          |
|                  |
|     Content      |
|       2          |
|                  |
|     Content      |
|       3          |
|                  |
|     Content      |
|       4          |
|                  |
|     Content      |
|       5          |
|                  |
|     Content      |
|       6          |
+------------------+
```

### Output: 2-Column Grid PDF
```
Page 1:
+------------------+------------------+
|                  |                  |
|     Content      |     Content      |
|       1          |       2          |
|                  |                  |
+------------------+------------------+

Page 2:
+------------------+------------------+
|                  |                  |
|     Content      |     Content      |
|       3          |       4          |
|                  |                  |
+------------------+------------------+

Page 3:
+------------------+------------------+
|                  |                  |
|     Content      |     Content      |
|       5          |       6          |
|                  |                  |
+------------------+------------------+
```

The script automatically:
1. Scales your screenshot to fit the column width
2. Splits it into equal segments
3. Arranges segments in a 2-column grid layout across pages

## Features

🖼️ **Smart Screenshot Processing**
- Automatically scales screenshots to fit column width
- Maintains aspect ratio for optimal readability
- Splits content into equal-height segments

📄 **Efficient PDF Layout**
- Arranges segments in a 2-column grid format
- Optimizes page usage (2 segments per page)
- Generates standard A4 size pages
- Preserves image quality using Lanczos resampling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rastinder/screenshot-align.git
cd screenshot-align
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Dependencies
- Python 3.x
- Pillow 10.2.0 (Python Imaging Library)
- ReportLab 4.1.0 (PDF generation)

## Usage

Basic command:
```bash
python screenshot_grid.py input_image.jpg output.pdf
```

Example:
```bash
python screenshot_grid.py Screenshot.jpg output.pdf
```

The script will:
1. Read your screenshot
2. Scale it to fit the column width
3. Split it into equal segments
4. Create a PDF with segments arranged in a 2-column grid

## How It Works

### Input Processing
- Takes any image format supported by Pillow (jpg, png, etc.)
- Automatically scales the image to fit A4 column width
- Preserves aspect ratio during scaling

### Grid Layout
Example with a screenshot of dimensions 358x6381:
```
Original:                    PDF Pages:
+-------------+    Page 1:   +-------+-------+
|    6381px   |             | Seg 1 | Seg 2 |
|     high    |    Page 2:   +-------+-------+
|             |             | Seg 3 | Seg 4 |
|   358px     |    Page 3:   +-------+-------+
|    wide     |             | Seg 5 | Seg 6 |
+-------------+    Page 4:   +-------+
                           | Seg 7 |
                           +-------+
```

- Original screenshot is split into ~7 segments
- Segments are distributed across 4 pages in 2 columns
- Last page contains single segment if total is odd
- Each segment is scaled to fit A4 column width
- Final PDF maintains readability and print quality

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## Support

If you encounter any issues or have questions:
1. Open an issue on GitHub
2. Provide sample images if relevant
3. Include error messages if applicable

## License

This project is open source and available under the MIT License.