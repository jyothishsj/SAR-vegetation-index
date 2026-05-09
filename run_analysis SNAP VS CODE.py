import rasterio
import matplotlib.pyplot as plt
import numpy as np

file_path = r'SAR 1_VH.TIF.tif' 

try:
    with rasterio.open(file_path) as src:
        # Read the VH band
        data = src.read(1)
        
        # Filter out invalid values and convert to dB
        data = np.where(data <= 0, 1e-6, data)
        data_db = 10 * np.log10(data)
        
        # --- DISPLAY SECTION ---
        plt.figure(figsize=(10, 8))
        # vmin/vmax focus the contrast on the actual terrain
        plt.imshow(data_db, cmap='gray', vmin=-25, vmax=-5) 
        plt.colorbar(label='Intensity (dB)')
        plt.title("Processed Sentinel-1 SAR Output")
        plt.show()

except Exception as e:
    print(f"Error: {e}")

# --- ASSIGNMENT FORMULAS ---
# RVI formula for Sentinel-1: (4 * VH) / (VV + VH)
def calculate_rvi(vv_band, vh_band):
    rvi = (4 * vh_band) / (vv_band + vh_band)
    return rvi