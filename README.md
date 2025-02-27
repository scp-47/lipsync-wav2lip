# lipsync-wav2lip


# commands
** 1. First, execute the generate.py for audio generation **
** 2. Clone the wav2lip repo **
** 3. Download the model from the repo and put it in the checkpoints directory **
** 4. Create a virtual environment **
** 5. Install all requirements from requirements **
** 6. Put all the generated audio, images in the wav2lip directory **
** 7. Execute the below commands **

python inference.py --checkpoint_path checkpoints/wav2lip.pth --face image.jpg --audio audio.wav --outfile output_video_new.mp4
