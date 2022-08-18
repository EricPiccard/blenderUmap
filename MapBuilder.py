import bpy
#file location
file = open("D:\\files\\Palace.txt")
while True:
    line = file.readline()
    line = line.strip()
    XL = 0
    YL = 0
    ZL = 0
    XR = 0
    YR = 0
    ZR = 0
    XS = 1
    YS = 1
    ZS = 1
    path
    path_intial = "D:\\models\\chec2\\"
    path = 0
    if "Properties" in line and "{" in line:
        line = file.readline()
        line = line.strip()
        while True:
            if "StaticMesh" in line and "{" in line:
                line = file.readline()
                line = line.strip()
                line = file.readline()
                line = line.strip()
                line = line.strip('"ObjectPath": "')
                hold = line.split('.')
                line = hold[0]
                line = line.replace('/', "\\ ")
                line = line.replace(' ', "")
                line = path_intial + line + ".gltf"
                path = line
                #print(line)
                if "Playable" in path or "Levels" in path:
                    #print(path)
                    #print(1)
                    path = 0
                    break
                #print(line)
            line = file.readline()
            line = line.strip()  
            if "RelativeLocation" in line and path != 0:
                #print(path)
                line = file.readline()
                line = line.strip()
                line = line.strip('"X": ')  
                line = line.strip(',')
                line = line.strip()
                line = line.replace(' ', '')
                #print(line)
                XL = float(line) /(100)
                line = file.readline()
                line = line.strip()
                line = line.strip('"Y": ')  
                line = line.strip(',')
                line = line.strip()
                line = line.replace(' ', '')
                #print(line)
                YL = float(line) /-100
                line = file.readline()
                line = line.strip()
                line = line.strip('"Z": ')  
                line = line.strip(',')
                line = line.strip()
                line = line.replace(' ', '')
                line = line.strip()
                #print(line)
                ZL = float(line) / 100
                create = 1
                line = file.readline()
                line = line.strip()
                line = file.readline()
                line = line.strip()
                print(line)
                if "RelativeScale" in line:
                    line = file.readline()
                    line = line.strip()
                    line = line.strip('"X": ')  
                    line = line.strip(',')
                    print(line)
                    XS = float(line) *1
                    line = file.readline()
                    line = line.strip()
                    line = line.strip('"Y": ')  
                    line = line.strip(',')
                    #print(line)
                    YS = float(line) * 1
                    line = file.readline()
                    line = line.strip()
                    line = line.strip('"Z": ')  
                    line = line.strip(',')
                    #print(line)
                    ZS = float(line)* 1
                    create = 1
                    line = file.readline()
                    line = line.strip()
                    break
                if "RelativeRotation" in line:
                    line = file.readline()
                    line = line.strip()
                    line = line.strip('"Pitch": ')  
                    line = line.strip(',')
                    #print(line)
                    YR = float(line)/57.2958
                    line = file.readline()
                    line = line.strip()
                    line = line.strip('"Yaw": ')  
                    line = line.strip(',')
                    #print(line)
                    ZR = float(line)/57.2958
                    line = file.readline()
                    line = line.strip()
                    line = line.strip('"Roll": ')  
                    line = line.strip(',')
                    #print(line)
                    XR = float(line)/-57.2958
                    create = 1
                    line = file.readline()
                    line = line.strip()   
                    line = file.readline()
                    line = line.strip()
                    if "RelativeScale3D" in line:
                        line = file.readline()
                        line = line.strip()
                        line = line.strip('"X": ')  
                        line = line.strip(',')
                     #   print(line)
                        XS = float(line)
                        line = file.readline()
                        line = line.strip()
                        line = line.strip('"Y": ')  
                        line = line.strip(',')
                      #  print(line)
                        YS = float(line)
                        line = file.readline()
                        line = line.strip()
                        line = line.strip('"Z": ')  
                        line = line.strip(',')
                       # print(line)
                        ZS = float(line)
                        create = 1
                        line = file.readline()
                        line = line.strip()
                        break
                    else:
                        break
                break
            if not line: 
                break
       # print(path)
    if path != 0:
        #print()
        print(path)
        bpy.ops.import_scene.gltf(filepath= path)  
        #print(XL)
        #print(YL)
        #print(ZL)
        print(XS)
        bpy.ops.transform.translate(value = (XL, YL, ZL))
        bpy.ops.transform.resize(value = (XS, YS, ZS))
        bpy.ops.transform.rotate(value = XR, orient_axis='X')
        bpy.ops.transform.rotate(value = YR, orient_axis='Y')
        bpy.ops.transform.rotate(value = ZR, orient_axis='Z')
        create = 0
    if not line:
        break