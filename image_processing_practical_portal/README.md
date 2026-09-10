# Image Processing Practical Portal

## Requirements
- Python 3.10+
- Flask
- OpenCV
- NumPy

## Install
```bash
pip install -r requirements.txt
```

## Run
```bash
python app.py
```

Open:
http://127.0.0.1:5000

## Notes
- The frontend lets the user choose an input image.
- Flask sends it to the corresponding OpenCV backend routine.
- The generated output is returned and displayed immediately.
- Practical 06 additionally requires a mask image.
- Practical 09 additionally requires a template image.
- Practical 02 bitwise AND/OR/XOR additionally requires a second image.
- Practical 07 demonstrates lossless PNG compression and compares sizes.