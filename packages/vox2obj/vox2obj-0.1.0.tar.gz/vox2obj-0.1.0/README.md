# Vox2Obj

Converts .vox files to .obj files. **UNDER ACTIVE DEVELOPMENT so things may change very quickly.** 

## Usage

```python
from vox2obj import convert_to_obj
convert_to_obj(in_file="in.vox", out_file="out.obj", texture_file="texture.png")
```

Where:
- "in.vox" is the input .vox file
- "out.obj" is the output destination
- "texture.png" is the texture that belongs to the .vox file
  - It should be a 1x255 pixel png image.
  - You will probably have to save this separately using your voxel editor. 