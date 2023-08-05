import logging
zuHmX=False
zuHmi=True
zuHms=Exception
import os
import traceback
import localstack
from localstack.utils.common import(download,in_docker,is_command_available,is_debian,now,rm_rf,run)
from localstack_ext.constants import ARTIFACTS_REPO
LOG=logging.getLogger(__name__)
RULE_ENGINE_INSTALL_URL="https://github.com/whummer/serverless-iot-offline"
H2_DOWNLOAD_URL="http://www.h2database.com/h2-2019-10-14.zip"
SSL_CERT_URL="%s/raw/master/local-certs/server.key"%ARTIFACTS_REPO
INFRA_DIR=os.path.join(os.path.dirname(localstack.__file__),"infra")
LOCALSTACK_DIR=os.path.dirname(localstack.__file__)
POSTGRES_LIB_FOLDER="/usr/lib/postgresql/11/lib"
def install_libs():
 install_iot_rule_engine()
 install_postgres()
 install_timescaledb()
 install_redis()
 install_mqtt()
def install_iot_rule_engine():
 target_dir=LOCALSTACK_DIR
 main_file=os.path.join(target_dir,"node_modules","serverless-iot-offline","query.js")
 if not os.path.exists(main_file):
  LOG.info("Installing IoT rule engine. This may take a while.")
  run("cd %s; npm install %s"%(target_dir,RULE_ENGINE_INSTALL_URL))
 return main_file
def install_postgres():
 if not in_docker():
  return
 check_or_install("psql","postgresql-11","RDS")
 check_or_install("pg_config","postgresql-server-dev-11 libpq-dev","RDS")
 if not is_debian():
  return
 plpython_lib=f"{POSTGRES_LIB_FOLDER}/plpython3.so"
 if os.path.exists(plpython_lib):
  return
 install_package("postgresql-plpython3-11","RDS")
def install_timescaledb():
 if not in_docker():
  return
 if os.path.exists(f"{POSTGRES_LIB_FOLDER}/timescaledb.so"):
  return
 check_or_install("gcc","cmake gcc git","Timestream")
 ts_dir="/tmp/timescaledb"
 tag="2.0.0-rc4"
 run("cd /tmp; git clone https://github.com/timescale/timescaledb.git")
 run("cd %s; git checkout %s; ./bootstrap -DREGRESS_CHECKS=OFF; cd build; make; make install"%(ts_dir,tag))
 rm_rf("/tmp/timescaledb")
def install_redis():
 check_or_install("redis-server","redis-server","ElastiCache")
 return "redis-server"
def install_mqtt():
 check_or_install("mosquitto","mosquitto","IoT")
 return "mosquitto"
def install_package(package,api_name):
 if not is_debian():
  LOG.info("Your platform is currently not supported for installing %s dependencies",api_name)
  return
 LOG.info("Downloading dependencies for %s API. This may take a while."%api_name)
 run(["apt-get","update"],shell=zuHmX)
 run(["apt-get","install","-y",package],shell=zuHmX)
def check_or_install(command,package,api):
 if not is_command_available(command):
  install_package(package,api)
def setup_ssl_cert():
 from localstack.services import generic_proxy
 target_file=generic_proxy.get_cert_pem_file_path()
 cache_duration_secs=6*60*60
 if os.path.exists(target_file):
  mod_time=os.path.getmtime(target_file)
  if mod_time>(now()-cache_duration_secs):
   return
 download_github_artifact(SSL_CERT_URL,target_file)
def download_github_artifact(url,target_file):
 def do_download(url,print_error=zuHmX):
  try:
   download(url,target_file)
   return zuHmi
  except zuHms as e:
   if print_error:
    LOG.info("Unable to download local test SSL certificate from %s to %s: %s %s"%(url,target_file,e,traceback.format_exc()))
 result=do_download(url)
 if not result:
  url=url.replace("https://github.com","https://cdn.jsdelivr.net/gh")
  url=url.replace("/raw/master/","@master/")
  do_download(url,zuHmi)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
