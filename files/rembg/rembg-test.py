from rembg import remove
from PIL import Image

input_path = r'D:\workspaces\pythonspaces\code-segment\files\rembg\animal-1.jpg'
output_path = 'output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)