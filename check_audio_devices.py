import pyaudio


p = pyaudio.PyAudio()
print("===================================================")
for i in range(p.get_device_count()):
   info = p.get_device_info_by_index(i)
   print("Device index {} name is: {}".format(i, info["name"]))
   print("Device info by index: ", info)


