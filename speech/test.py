import pyaudio

p = pyaudio.PyAudio()

# Try all host APIs and their input devices
for api_index in range(p.get_host_api_count()):
    api = p.get_host_api_info_by_index(api_index)
    print(f"\n=== Host API {api_index}: {api['name']} ===")

    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        if info["hostApi"] == api_index and int(info["maxInputChannels"]) > 0:
            print(f"  Index {i}: {info['name']} | rate: {info['defaultSampleRate']}")
            try:
                stream = p.open(
                    format=pyaudio.paInt16,
                    channels=1,
                    rate=int(info["defaultSampleRate"]),
                    input=True,
                    input_device_index=i,
                    frames_per_buffer=1024,
                )
                stream.read(1024)
                stream.stop_stream()
                stream.close()
                print(f"    WORKS!")
            except Exception as e:
                print(f"    Failed: {e}")

p.terminate()
