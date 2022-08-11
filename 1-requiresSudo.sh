# copies logs from /var/log and changes owner of file
sudo cp /var/log/auth.* rawLogs/
sudo chown $(whoami): rawLogs/*
