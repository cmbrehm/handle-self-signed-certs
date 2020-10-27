FROM httpd:latest
RUN apt-get update && apt-get install openssl
WORKDIR /usr/local/apache2/conf
RUN /usr/bin/openssl genrsa -out server.key 4096
RUN /usr/bin/openssl req -new -subj "/C=/ST=/L=/O=/CN=justme.localdomain" -key server.key -out my.csr
RUN /usr/bin/openssl x509 -req -signkey server.key -days 365 -in my.csr -out server.crt
RUN sed -i \
        -e 's/^#\(Include .*httpd-ssl.conf\)/\1/' \
        -e 's/^#\(LoadModule .*mod_ssl.so\)/\1/' \
        -e 's/^#\(LoadModule .*mod_socache_shmcb.so\)/\1/' \
        httpd.conf
