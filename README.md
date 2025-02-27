# LipSync-Wav2Lip

## 🔧 Setup and Execution

Follow these steps to set up and run the project:

### 1**Generate Audio**
Run `generate.py` to create the required audio files for lip-syncing.

### 2**Clone the Wav2Lip Repository**
```sh
git clone https://github.com/Rudrabha/Wav2Lip.git
cd Wav2Lip
```

### 3**Download and Place Model Checkpoints**
- Download the pre-trained model from the official Wav2Lip repository.
- Move the model file (`wav2lip.pth`) to the `checkpoints/` directory.

### 4**Create a Virtual Environment**
```sh
python -m venv wav2lip_env
```
Activate the virtual environment:  
- **Windows**: `wav2lip_env\Scripts\activate`  

### 5**Install Dependencies**
```sh
pip install -r requirements.txt
```

### 6**Prepare Input Files**
- Place the generated audio and images in the **Wav2Lip** directory.
- Make required changed to audio.py and inference.py

### 7**Run the Inference Script**
Execute the following command to generate the lip-synced video:  
```sh
python inference.py --checkpoint_path checkpoints/wav2lip.pth --face image.jpg --audio audio.wav --outfile output_video_new.mp4
```

## 📌 Notes
- Ensure that `image.jpg` and `audio.wav` exist in the working directory.
- If you face dependency issues, check the correct versions of `torch`, `torchvision`, and `numpy`.
- For GPU support, install `torch` and `torchvision` versions compatible with your CUDA version.

