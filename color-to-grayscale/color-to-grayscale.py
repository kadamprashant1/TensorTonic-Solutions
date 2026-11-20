import numpy as np
def color_to_grayscale(image: list) -> list:
    """
    Returns the luminance value of every RGB pixel.
    """
    # Write code here
    img_array = np.array(image, dtype=np.float64)
    
    # Extract R, G, B from the last axis
    r = img_array[..., 0]
    g = img_array[..., 1]
    b = img_array[..., 2]
    
    gray = 0.299 * r + 0.587 * g + 0.114 * b
    return gray.tolist()