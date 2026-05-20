FROM nginx:alpine

# Copy all static website files to Nginx public folder
RUN echo "server { listen 80; server_name localhost; charset utf-8; sendfile off; location / { root /usr/share/nginx/html; index index.html index.htm; } }" > /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html

# Expose port 80 to access the website
EXPOSE 80
