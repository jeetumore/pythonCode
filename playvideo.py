import docker
import webbrowser
import time
import os
import signal
import platform

# Function to run multiple Docker containers
def run_docker_containers(image, container_count):
    client = docker.from_env()
    containers = []
    for i in range(container_count):
        container = client.containers.run(image, detach=True)
        containers.append(container)
        print(f"Started container {container.short_id}")
    return containers

# Function to stop and remove Docker containers
def stop_docker_containers(containers):
    for container in containers:
        print(f"Stopping container {container.short_id}")
        container.stop()
        container.remove()

# Function to open a YouTube video in the browser
def open_youtube_video(video_url):
    webbrowser.open(video_url)
    print(f"Opened YouTube video: {video_url}")

# Function to close the browser (platform dependent)
def close_browser():
    print("Closing the browser...")
    current_os = platform.system()
    if current_os == "Windows":
        os.system("taskkill /F /IM chrome.exe")  # Assumes Chrome browser
    elif current_os == "Darwin":  # macOS
        os.system("pkill -f 'Google Chrome'")
    elif current_os == "Linux":
        os.system("pkill -f 'chrome'")
    else:
        print("Unsupported OS for browser closure")

# Main function
def main():
    # Step 1: Run multiple Docker containers
    containers = run_docker_containers(image='nginx', container_count=2)

    # Step 2: Open a YouTube video in the browser
    video_url = 'https://youtu.be/IPBdjJSm3Kw?si=-K8Gm9zWTmXFM8_G'  # Example video
    open_youtube_video(video_url)

    # Step 3: Wait for 20 seconds while the video plays
    time.sleep(20)

    # Step 4: Close the browser
    close_browser()

    # Step 5: Stop and remove Docker containers
    stop_docker_containers(containers)

if __name__ == "__main__":
    main()
