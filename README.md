# Tutorial: Custom YOLOv8 Pose Detection

Welcome to the tutorial on training a custom YOLOv8 pose detection model. In this tutorial, we will guide you through the process of collecting images for your custom dataset using a web crawler and then training your YOLOv8 model for pose detection.

## Step 1: Image Data Collection

In the first step of this tutorial, we'll collect images that we want to use for training our custom pose detection model. You can use images of any category or object that you want to detect poses for. To assist with this step, we provide a simple web crawler script that can download images based on different keywords.

### Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- Python 3.x
- Required Python packages (requests, BeautifulSoup) which can be installed using pip:

```python
pip install requests
pip install beautifulsoup4
```

### Usage

1. Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/custom-yolov8-pose-detection.git 
```

2. Navigate to the project folder:
```bash
cd custom-yolov8-pose-detection
```

3. Modify the `query_list` in the `crawler.py` script with your desired keywords. For example:
```python
query_list = ["violin", 'violinist ', 'play violin', 'violin instrument']
```

4. Run the crawler script to download images:
```python
python crawler.py
```

The script will fetch image URLs based on the provided keywords and download the images to the 'images' folder.

You can use any type of images that match your dataset requirements. These images will be used in the subsequent steps of the tutorial to train your custom YOLOv8 model for pose detection.

This concludes the first step of the tutorial. In the next steps, we will prepare and annotate the dataset, configure YOLOv8, and train the model for pose detection.


## Step 2: Setting Up COCO Annotator

In this step, we will set up the COCO Annotator, which is a powerful tool for annotating images with keypoint detection and visibility options. This tool will be used for annotating the images you collected in the previous step.

### Install Docker

#### -On Ubuntu:
Follow the instructions provided on the page [here](https://docs.docker.com/engine/install/ubuntu/) until the end of the installation step.

<br>(img 1)<br>

#### -On Windows:
1. Download the Docker Desktop installer file from [here](https://hub.docker.com/editions/community/docker-ce-desktop-windows).
2. Install Docker Desktop.
3. Run the Docker Desktop program to ensure it is running properly.

**Note**: If you encounter the "WSL version is too old" error on Windows, follow the tutorial provided [here](https://stackoverflow.com/questions/67168809/docker-desktop-requires-a-newer-wsl-kernel-version-on-windows). After following the steps in the tutorial, open the command prompt (CMD) and run the following command to update WSL:
   ```bash
   wsl --update
   ```

### Install COCO Annotator
1. Download the COCO Annotator GitHub repository from [here](https://github.com/jsbroks/coco-annotator).
2. Open the downloaded folder.
3. a. (For windows) inside that folder open a “cmd” or “terminal” and put this command:
```bash
docker-compose up
```
3. b. (For ubuntu) inside that folder open a “terminal” and put this command:
```bash
sudo docker-compose up
```
4. The output should be something like this on both operating systems.
<br>(img 2) <br>

5. The command above will pull the latest stable image from Docker Hub, which is pre-compiled with all the necessary dependencies. You can access the COCO Annotator instance by opening http://localhost:5000/ in your web browser while steps 3a or 3b are running. The initial page will look like the screenshot below. If it's your first time opening it after installation, you will only see the 'Register' tab. If you have already created an account, you will also have a 'Login' tab.

   
<br>(img 3) <br>

<br><br>

To Do:
- Put the images 1 , 2 and 3
- How to annotate data in coco annotator (In a video maybe)
- Install Yolo
- Yolo config files settings
- Train a model
- Infer
