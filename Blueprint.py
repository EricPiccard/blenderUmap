import bpy
bpy.ops.import_scene.gltf(filepath="D:\\files\\HT_Trident-StairPod_C.gltf")
XL = float(-2033.6592) / 100
print(XL)
YL = float(-3030.5093)/(-100) 
ZL = float(226.55573)/100
XR = 0 / (57.2958)
YR = 0 /57.2958
ZR = 90.000046/57.2958
XS = 1
YS = 1
ZS = 1

bpy.ops.transform.translate(value = (XL, YL, ZL))
bpy.ops.transform.resize(value = (XS, YS, ZS))
bpy.ops.transform.rotate(value = XR, orient_axis='X')
bpy.ops.transform.rotate(value = YR, orient_axis='Y')
bpy.ops.transform.rotate(value = ZR, orient_axis='Z')