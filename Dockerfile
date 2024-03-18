# Use the official Python image
FROM python:3.9

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose the port your Flask app runs on
EXPOSE 50505

# Define the command to run your app
CMD ["gunicorn", "app:app"]