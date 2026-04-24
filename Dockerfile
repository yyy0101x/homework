# Use the lightweight Nginx image
FROM nginx:alpine

# Copy your static folder content into the default Nginx web directory
COPY ./static /usr/share/nginx/html

# Nginx serves on port 80 by default
EXPOSE 80