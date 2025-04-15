# F5 Steganography Algorithm

## Overview
The F5 algorithm is a steganography technique that hides a secret message within an image by subtly modifying the least significant bits (LSB) of the image pixels. These modifications are imperceptible to the human eye, making the hidden message virtually undetectable without the proper decoding key.

## How F5 Works

### Key Concepts
- **Least Significant Bit (LSB) Modification**: Changes the final bit of pixel color values (0-255) to store hidden data
- **Randomized Embedding**: Uses a key-based random number generator to determine which pixels get modified
- **Visual Preservation**: Maintains the original image's appearance while hiding data

### Example: Hiding "HI"
The message "HI" in binary (ASCII):
- "H" = `01001000`
- "I" = `01001001`

## Encoding Process (Hiding the Message)

1. **Image Preparation**:
   - Open the cover image and convert to pixel grid
   - Convert secret message to binary representation

2. **Message Embedding**:
   ```python
   For each pixel component (R,G,B) in image:
       Generate random bit (0 or 1) using secret key
       If random bit == 1:
           Replace LSB of pixel with message bit
       Else:
           Keep original LSB
       Move to next message bit
