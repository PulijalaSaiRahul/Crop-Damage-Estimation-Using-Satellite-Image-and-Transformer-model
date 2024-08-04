import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Loading a png mask image for inspection using PIL
test_mask_pil = Image.open("output/00599.png")
test_mask_np = np.array(test_mask_pil)

plt.imshow(test_mask_np, cmap='gray')
plt.show()

print(np.unique(test_mask_np))  # This is not a true binary image.

# # Binarizing the image using numpy operations
# binary_mask = np.where(test_mask_np > 0, 1, test_mask_np)
# print(np.unique(binary_mask))

# plt.imshow(binary_mask, cmap='gray')
# plt.show()


# import os
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

# def binarize_and_save_images(input_directory, output_directory):
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     # Loop through each file in the input directory
#     for filename in os.listdir(input_directory):
#         if filename.endswith(".png"):  # Process only PNG files (you can modify the extension as needed)
#             file_path = os.path.join(input_directory, filename)
#             output_path = os.path.join(output_directory, filename)

#             # Loading a png mask image for inspection using PIL
#             test_mask_pil = Image.open(file_path)
#             test_mask_np = np.array(test_mask_pil)

#             # Binarizing the image using numpy operations
#             binary_mask = np.where(test_mask_np > 0, 255, test_mask_np)

#             # Saving the binarized image
#             img = Image.fromarray(binary_mask)  # Convert back to 0-255 range for PIL
#             img.save(output_path)

#             print(f"Processed and saved: {filename}")

# # Example usage:
# input_folder = 'input'  # Replace with your input folder containing PNG images
# output_folder = 'output'  # Replace with your output folder to save processed images

# binarize_and_save_images(input_folder, output_folder)
