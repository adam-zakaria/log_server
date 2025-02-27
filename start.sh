cd /home/ubuntu/Code/log_server/frontend
pm2 start 'npm run dev' --name 'log_server_front'
cd /home/ubuntu/Code/log_server/backend
pm2 start 'DEBUG=0 python3 -m flask run --host=0.0.0.0 --port=1337' --name 'log_server_back'