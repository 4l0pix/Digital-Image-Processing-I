# Digital Image Processing I — Academic Project

This repository collects course assignments, example implementations and experiments for an introductory Digital Image Processing course. The project is implemented in Python and includes example scripts, notebooks, sample images (or download helpers), generated results and a short report.



What’s in this repo
- data/                 — (optional) local image samples or placeholders for downloads
- notebooks/            — Jupyter notebooks demonstrating algorithms and experiments
- src/                  — Python modules and scripts implementing algorithms (if present)
- results/              — generated results, visualizations and exported figures
- report/               — academic report(s) in PDF form
- koukosias.py          — interactive script implementing several spatial-domain operations
- requirements.txt      — Python dependencies (please add or update as needed)
- README.md             — this file

k
koukosias.py is a self-contained Python script (author: akoukosias) that implements and demonstrates a number of spatial-domain image processing operators on grayscale images. The script uses OpenCV, NumPy and Matplotlib and exposes a simple text menu (Greek prompts) to interactively apply operations and view results.

### Main features / functions
- display_image(title, image)
  - Shows image with OpenCV (cv2.imshow). Note: requires a GUI-enabled environment.
- negative_image(image)
  - Computes and shows the negative (255 - image).
- apply_average_filter(image, filter_type)
  - Applies mean (box) filtering. Accepts filter_type "soft" (3x3), "medium" (9x9), "hard" (15x15).
- sharpen_image(image)
  - Sharpening using a 3x3 Laplacian-like kernel.
- plot_histogram(image)
  - Plots a styled histogram using Matplotlib (dark theme).
- histogram_matching(input_img, reference_img)
  - Performs histogram matching of an input image to a reference image (using CDF mapping and cv2.LUT).
- Interactive menu
  - Options include: negative, average filter (3 strengths), sharpening, histogram display, histogram matching (choose reference and input variants built from original/blurred/sharpened images).

Important usage notes
- The script expects a grayscale image path. Prompts are in Greek (e.g., "Dose to path tis grayscale eikonas:").
- GUI display: cv2.imshow is used; run on a machine with a display (local desktop or WSL/remote with X forwarding). For headless environments, adapt the script to save images to disk (cv2.imwrite) or use Matplotlib image display.
- Histogram matching uses 256 bins and a LUT. A matched image is displayed and histograms of input, reference and matched images are plotted side-by-side.

Example run
1. Ensure dependencies are installed (see Requirements below).
2. Run the script and follow prompts:
   python koukosias.py
   Then provide the path to a grayscale image when prompted (e.g., data/cameraman.png).

ReportProject1.pdf
- The file report/ReportProject1.pdf is the accompanying project report. It contains descriptions of methods, experiments, figures and discussion. Refer to that PDF for details on the experimental setup and results reproduced by the code in this repository.

## Requirements
Minimum
- Python 3.8+
- numpy
- opencv-python
- matplotlib
Optional (for other notebooks / experiments)
- scipy
- scikit-image
- scikit-learn
- pillow or imageio
Add these to requirements.txt in the root of the repo (I can generate a ready-to-commit requirements.txt if you want).

## Quick start
1. Clone the repo:
   git clone https://github.com/4l0pix/Digital-Image-Processing-I.git
2. Create and activate a virtual environment (recommended):
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
3. Install dependencies:
   pip install -r requirements.txt (or python -m pip install -r requirements.txt)
   If requirements.txt is not present, install:
   pip install numpy opencv-python matplotlib
4. Run the interactive script:
   python koukosias.py
   Provide the path to a grayscale image when requested.

### Reproducibility notes
- Many notebooks and scripts save results to results/. If you want reproducible, scriptable runs (no GUI), modify koukosias.py to write outputs instead of calling cv2.imshow (I can prepare a headless mode).
- The histogram matching implementation uses discrete CDF matching — identical inputs and reference images should reproduce the same matched result across runs.

### Contributing
Contributions are welcome — bug fixes, additional algorithms, conversion of scripts into modules, Jupyter notebooks demonstrating internals, CI for notebooks, or adding test images with clear licensing.

## Authors and contact
- Repository owner / maintainer: 4l0pix (https://github.com/4l0pix)
- For questions, open an issue on the repo.

## License
- The repository currently states MIT in README. Ensure any included datasets follow their licensing terms. Update LICENSE as needed.

### Acknowledgements
- Open-source libraries: NumPy, SciPy, scikit-image, OpenCV, Matplotlib.

