FROM nginx:alpine

# Forward nginx logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

# Copy nginx config file
COPY nginx.conf /etc/nginx

# Expose port 80 for http
EXPOSE 80