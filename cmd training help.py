python
import os
import os.path
import cv2
from Katna.video import Video
import multiprocessing
vd = Video()
for subdir, dirs, files in os.walk('G:/FAZAL/New/mp'):
    for file in files:
        print(os.path.join(subdir, file))
        imgs = vd.extract_frames_as_images(no_of_frames=200, file_path=os.path.join(subdir, file))
        for counter, img in enumerate(imgs):
            vd.save_frame_to_disk(img, file_path=subdir,
                                  file_name=file + str(counter), file_ext=".jpeg", )




FOR /F "tokens=*" %G IN ('dir /b *.h264') DO ffmpeg -framerate 24 -i "%G" -c copy "%~nG.mp4"

ffmpeg -framerate 24 -i input.264 -c copy output.mp4

for /f "tokens=1 delims=." %a in ('dir /B *.h264') do ffmpeg -i "%a.h264" "%a.mp4"


imgs = vd.extract_frames_as_images(no_of_frames=8000, file_path='G:/FAZAL/1-23/test/output.mp4')