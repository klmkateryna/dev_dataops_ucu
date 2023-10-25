## Multi-Stage Build Example
This project is an example of building and packaging a simple Python web application using a multi-stage build.
Multi-stage builds are a way to optimize the Docker build process by reducing the size of the final image and improving performance. 
You can also find the Dockerfile and use it to compare the results with the multistage Dockerfile.

### Project structure
 - `templates/` - this folder contains HTML templates 
 - `Dockerfile-multistage-build` - this is a file with multistage instructions to build image
 - `Dockerfile` - this is a file with instructions to build image
 - `server.py` - this is an application code - simple Python web application using the Flask framework
 - `requirements.txt` - this is a dependencies file required by the Flask application

### Build and Run the Docker Image
- using simple Dockerfile:
    ```
    docker build -f Dockerfile -t dockerfile-sample-app . 
    
    docker run -d -p 8080:8080 dockerfile-sample-app
    ```
- using Multi-Stage Dockerfile:
    ```
    docker build -f Dockerfile-multistage-build -t dockerfile-multistage-sample-app .
    
    docker run -d -p 8081:8080 dockerfile-multistage-sample-app
    ```

