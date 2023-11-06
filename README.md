
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
