# Set base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Add group and user to run a container
RUN groupadd -r webservice_user && useradd --no-log-init -r -g webservice_user webservice_user

# Copy the dependencies file and application code to the working directory
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

USER webservice_user:webservice_user

# Expose the port on which the application will run
EXPOSE 8080

# Define the command to run the application
CMD ["python", "server.py"]
