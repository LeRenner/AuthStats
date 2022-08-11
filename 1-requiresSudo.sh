# copies logs from /var/log and changes owner of file
mkdir rawLogs extracted
sudo cp /var/log/auth.* rawLogs/
sudo chown $(whoami): rawLogs/*
