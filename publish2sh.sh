# publicar el repo en odoo.sh
sudo rsync -avz --exclude ".git" /odoo_ar/odoo-13.0e/tatakua/sources/odoo-paraguay/ ~/tmp/tatakua-sh
#git -C ~/tmp/tatakua-sh add .
#git -C ~/tmp/tatakua-sh commit -m "$1"
#git -c ~/tmp/tatakua-sh push
