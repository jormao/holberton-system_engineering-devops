# automate the task of creating a custom 
# HTTP header response, but with Puppet.
exec {'configure HTTP':
  command => "apt-get update && apt-get -y install nginx && echo -e 'Holberton School' > /var/www/html/index.html && sed -i '43i rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default && sed -i '12i add_header X-Served-By $hostname;' /etc/nginx/nginx.conf && service nginx start",
  provider => 'shell',
}
