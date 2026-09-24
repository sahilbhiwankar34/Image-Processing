import cv2
import os


# ---------- Function to calculate compression ratio ----------
def compression_ratio(original_file, compressed_file):
    """
    Compression Ratio = Original Size / Compressed Size
    """
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)

    ratio = original_size / compressed_size if compressed_size != 0 else 0

    return ratio, original_size / 1024, compressed_size / 1024  # sizes in KB


# ---------- Load the image ----------
image_path = "gill.jpeg"  # Replace with your actual image file

image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Image not found. Check the path.")


# ---------- LOSSY COMPRESSION (JPEG) ----------
jpeg_quality = 30  # Lower = higher compression

lossy_output = "compressed_lossy.jpg"

cv2.imwrite(
    lossy_output,
    image,
    [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality]
)


# ---------- LOSSLESS COMPRESSION (PNG) ----------
png_compression = 9  # 0 = no compression, 9 = maximum compression

lossless_output = "compressed_lossless.png"

cv2.imwrite(
    lossless_output,
    image,
    [cv2.IMWRITE_PNG_COMPRESSION, png_compression]
)


# ---------- Calculate Compression Ratios ----------
lossy_ratio, original_kb, lossy_kb = compression_ratio(
    image_path, lossy_output
)

lossless_ratio, _, lossless_kb = compression_ratio(
    image_path, lossless_output
)


# ---------- Print Results ----------
print(f"Original Size: {original_kb:.2f} KB")

print(
    f"Lossy JPEG Size: {lossy_kb:.2f} KB "
    f"(Quality={jpeg_quality})"
)

print(
    f"Lossless PNG Size: {lossless_kb:.2f} KB "
    f"(Compression={png_compression})"
)

print(f"Lossy Compression Ratio: {lossy_ratio:.2f}:1")

print(f"Lossless Compression Ratio: {lossless_ratio:.2f}:1")


# ---------- Display Images ----------
cv2.imshow("CS24086 Original", image)

cv2.imshow(
    "CS24086 Lossy JPEG",
    cv2.imread(lossy_output)
)

cv2.imshow(
    "CS24086 Lossless",
    cv2.imread(lossless_output)
)

cv2.waitKey(0)
cv2.destroyAllWindows()

# #code2
# import cv2
# import os
# from collections import defaultdict


# # -------------------- RUN LENGTH ENCODING (RLE) --------------------
# def rle_encode(data):
#     """Run Length Encode a 1D list of values."""
#     encoding = []

#     prev = data[0]
#     count = 1

#     for pixel in data[1:]:
#         if pixel == prev:
#             count += 1
#         else:
#             encoding.append((prev, count))
#             prev = pixel
#             count = 1

#     encoding.append((prev, count))

#     return encoding


# def rle_decode(encoding):
#     """Run Length Decode back to original data."""
#     data = []

#     for value, count in encoding:
#         data.extend([value] * count)

#     return data


# # -------------------- LZW COMPRESSION --------------------
# def lzw_compress(uncompressed):
#     """Compress a list of integers using LZW."""

#     # Build the dictionary
#     dict_size = 256
#     dictionary = {bytes([i]): i for i in range(dict_size)}

#     w = b""
#     compressed = []

#     for k in uncompressed:
#         c = bytes([k])
#         wc = w + c

#         if wc in dictionary:
#             w = wc
#         else:
#             compressed.append(dictionary[w])
#             dictionary[wc] = dict_size
#             dict_size += 1
#             w = c

#     if w:
#         compressed.append(dictionary[w])

#     return compressed


# def lzw_decompress(compressed):
#     """Decompress LZW output."""

#     if not compressed:
#         return []

#     dict_size = 256
#     dictionary = {i: bytes([i]) for i in range(dict_size)}

#     w = bytes([compressed.pop(0)])
#     result = bytearray(w)

#     for k in compressed:

#         if k in dictionary:
#             entry = dictionary[k]

#         elif k == dict_size:
#             entry = w + w[:1]

#         else:
#             raise ValueError("Bad compressed k: %s" % k)

#         result += entry

#         dictionary[dict_size] = w + entry[:1]
#         dict_size += 1

#         w = entry

#     return list(result)


# # -------------------- MAIN SCRIPT --------------------

# # Load grayscale image
# image_path = "tree.jpeg"  # Replace with your image filename

# img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# if img is None:
#     raise FileNotFoundError("Image not found. Check the path.")


# # Flatten image to 1D for RLE and LZW
# pixels = img.flatten().tolist()


# # -------------------- RLE --------------------
# rle_encoded = rle_encode(pixels)

# # Estimate RLE size:
# # 1 byte for value + 1 byte for count
# rle_size_bytes = len(rle_encoded) * 2

# # Decode to verify
# rle_decoded = rle_decode(rle_encoded)

# assert rle_decoded == pixels, "RLE decompression failed!"


# # -------------------- LZW --------------------
# lzw_encoded = lzw_compress(pixels)

# # Approximate each LZW code as 2 bytes
# lzw_size_bytes = len(lzw_encoded) * 2

# # Decode to verify
# lzw_decoded = lzw_decompress(lzw_encoded.copy())

# assert lzw_decoded == pixels, "LZW decompression failed!"


# # -------------------- Compression Ratios --------------------
# original_size_bytes = len(pixels)

# rle_ratio = (
#     original_size_bytes / rle_size_bytes
#     if rle_size_bytes
#     else 0
# )

# lzw_ratio = (
#     original_size_bytes / lzw_size_bytes
#     if lzw_size_bytes
#     else 0
# )


# # -------------------- Print Results --------------------
# print(
#     "Original Image Size (approx):",
#     original_size_bytes,
#     "bytes"
# )

# print(
#     "RLE Compressed Size (approx):",
#     rle_size_bytes,
#     "bytes"
# )

# print(
#     "LZW Compressed Size (approx):",
#     lzw_size_bytes,
#     "bytes"
# )

# print(f"RLE Compression Ratio: {rle_ratio:.2f}:1")

# print(f"LZW Compression Ratio: {lzw_ratio:.2f}:1")


# # -------------------- Show Original Image --------------------
# cv2.imshow("CS24106 Original Image", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
