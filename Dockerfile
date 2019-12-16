FROM python:3.7.3-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN useradd -g 100 --uid 99 -ms /bin/bash nobody

RUN chown -R 99:100 .
RUN chmod -R 777 .
RUN chmod -R g+s .

USER nobody

# Install the dependencies
RUN pip install -r requirements.txt

# Run the program with unbuffered argument
CMD ["python3", "-u", "main.py"]