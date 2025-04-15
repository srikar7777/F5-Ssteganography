For each pixel component (R,G,B) in same order:
    Generate random bit (0 or 1) using key
    If random bit == 1:
        Read LSB as message bit
    Else:
        Skip this pixel
    Combine bits to reconstruct message
