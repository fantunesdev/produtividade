server {
        listen      80;
        server_name prod.my-server.com;
        charset     utf-8;

        access_log  /var/log/nginx/prod.my-server.com-access.log;
        error_log   /var/log/nginx/prod.my-server.com-error.log;
        client_max_body_size 75M;

        location / {
                include proxy_params;
                proxy_pass http://unix:/var/www/python/prd/produtividade.sock;
	}

        location /media  {
                alias /var/www/python/prd/media;
        }

        location /static {
                alias /var/www/python/prd/static;
        }
}

