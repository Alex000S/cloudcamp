1. При выполнении данной команды: docker run -it --rm ubuntu -- bash 
получаем ошибку: docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "--": executable file not found in $PATH: unknown

Run 'docker run --help' for more information 

Следовательно делаем вывод что данная команда неправильная либо она предназначена для другой более старой версии docker.

2. При выполнении данной команды: docker run -it --rm ubuntu bash 
мы успешно заходим в контейнер

3. Делаем команду apt-get update и видим что наша команда успешно отработала.

4. Вводим команду: echo "nameserver 127.0.0.1" > /etc/resolv.conf

Данная команда выполняет перезапись содержимого файла /etc/resolv.conf, устанавливая единственный DNS-сервер с адресом 127.0.0.1 (localhost). Это означает, что система будет пытаться разрешать доменные имена, обращаясь к DNS-серверу, работающему на той же машине.

5. Меняем его обратно и пытаемся вновь запустить обновление пакетов и видим что пакеты больше не обновляются и доступа к интернету больше нет. 
