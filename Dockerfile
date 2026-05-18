FROM nginx:alpine

# Copy all static website files to Nginx public folder
COPY . /usr/share/nginx/html

# Expose port 80 to access the website
EXPOSE 80
