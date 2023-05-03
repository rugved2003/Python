import speedtest

st = speedtest.speedtest()
print("download speed: ",st.download)
print("upload speed: ",st.upload)