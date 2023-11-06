# Tutorial: Custom YOLOv8 Pose Detection with Web Crawler

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
```python
git clone https://github.com/your-username/custom-yolov8-pose-detection.git 
```

2. Navigate to the project folder:
cd custom-yolov8-pose-detection

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

