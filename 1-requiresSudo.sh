# copies logs from /var/log and changes owner of file
mkdir rawLogs
chmod 600 rawLogs
sudo cp /var/log/auth.* rawLogs/
sudo chown $(whoami): rawLogs/*
