import rasterio
import matplotlib.pyplot as plt
import numpy as np

file_path = r'SAR 1_VH.TIF.tif' 

try:
    with rasterio.open(file_path) as src:
        # We read at 1/5th resolution to prevent the white screen lag
        data = src.read(1, out_shape=(1, int(src.height // 5), int(src.width // 5)))
        
        # Filter out invalid values
        data = np.where(data <= 0, 1e-6, data)
        
        # Convert to dB
        data_db = 10 * np.log10(data)
        
        # Display with a high-contrast theme
        plt.figure(figsize=(10, 8))
        # 'vmin' and 'vmax' help focus on the actual ground data
        plt.imshow(data_db, cmap='gray', vmin=-25, vmax=-5) 
        plt.colorbar(label='Intensity (dB)')
        plt.title("Processed Sentinel-1 SAR Output")
        plt.show()

except Exception as e:
    print(f"Error: {e}")