FROM python:3.7

RUN mkdir -p /app
ADD . /app
# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install OpenAI API
RUN pip install flask openai

EXPOSE 5000

# Run application
CMD ["python", "main.py"]