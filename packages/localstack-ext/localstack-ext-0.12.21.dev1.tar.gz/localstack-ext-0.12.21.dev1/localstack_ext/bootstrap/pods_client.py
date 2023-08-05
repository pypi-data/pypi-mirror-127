import json
LQRYA=None
LQRYH=object
LQRYb=Exception
LQRYN=bool
LQRYP=False
LQRYd=int
LQRYo=str
LQRYM=set
LQRYe=property
LQRYn=classmethod
LQRYU=True
LQRYD=staticmethod
LQRYp=open
LQRYl=map
LQRYg=range
LQRYc=len
LQRYK=getattr
LQRYr=type
LQRYS=isinstance
LQRYC=list
import logging
import os
import re
import traceback
from typing import Dict,List,Set
from zipfile import ZipFile
import requests
import yaml
from dulwich import porcelain
from dulwich.client import get_transport_and_path_from_url
from dulwich.repo import Repo
from localstack import config,constants
from localstack.utils.common import(chmod_r,clone,cp_r,disk_usage,download,format_number,is_command_available,load_file,mkdir,new_tmp_dir,new_tmp_file,retry,rm_rf,run,safe_requests,save_file,to_bytes,to_str,unzip)
from localstack.utils.docker_utils import DOCKER_CLIENT
from localstack.utils.testutil import create_zip_file
from localstack_ext import config as ext_config
from localstack_ext.bootstrap.licensing import get_auth_headers
from localstack_ext.bootstrap.state_utils import API_STATES_DIR,api_states_traverse
from localstack_ext.constants import API_PATH_PODS
LOG=logging.getLogger(__name__)
PERSISTED_FOLDERS=["api_states","dynamodb","kinesis"]
MERGE_STRATEGY_TWO_WAY="two way"
MERGE_STRATEGY_THREE_WAY="three way"
MERGE_STRATEGY_DISABLED="disabled"
class PodInfo:
 def __init__(self,name=LQRYA,pod_size=0):
  self.name=name
  self.pod_size=pod_size
  self.pod_size_compressed=0
  self.persisted_resource_names=[]
class CloudPodManager(LQRYH):
 BACKEND="_none_"
 def __init__(self,pod_name=LQRYA,config=LQRYA):
  self.pod_name=pod_name
  self._pod_config=config
 def init(self):
  raise LQRYb("Not implemented")
 def delete(self,remote:LQRYN)->LQRYN:
  raise LQRYb("Not implemented")
 def push(self,comment:LQRYo=LQRYA)->PodInfo:
  raise LQRYb("Not implemented")
 def pull(self,inject_version_state:LQRYN=LQRYP,reset_state_before:LQRYN=LQRYP,fetch_all:LQRYN=LQRYA):
  raise LQRYb("Not implemented")
 def commit(self,message:LQRYo=LQRYA):
  raise LQRYb("Not implemented")
 def inject(self,version:LQRYd,reset_state:LQRYN):
  raise LQRYb("Not implemented")
 def list_versions(self)->List[LQRYo]:
  raise LQRYb("Not implemented")
 def version_info(self,version:LQRYd):
  raise LQRYb("Not implemented")
 def version_metamodel(self,version:LQRYd):
  raise LQRYb("Not implemented")
 def set_version(self,version:LQRYd,inject_version_state:LQRYN,reset_state:LQRYN,commit_before:LQRYN):
  raise LQRYb("Not implemented")
 def list_version_commits(self,version:LQRYd)->List[LQRYo]:
  raise LQRYb("Not implemented")
 def get_commit_diff(self,version:LQRYd,commit:LQRYd)->LQRYo:
  raise LQRYb("Not implemented")
 def register_remote(self,pod_name:LQRYo)->LQRYN:
  raise LQRYb("Not implemented")
 def rename_pod(self,current_pod_name,new_pod_name)->LQRYN:
  raise LQRYb("Not implemented")
 def list_pods(self,fetch_remote:LQRYN)->Set[LQRYo]:
  raise LQRYb("Not implemented")
 def restart_container(self):
  LOG.info("Restarting LocalStack instance with updated persistence state - this may take some time ...")
  data={"action":"restart"}
  url="%s/health"%config.get_edge_url()
  try:
   requests.post(url,data=json.dumps(data))
  except requests.exceptions.ConnectionError:
   pass
  def check_status():
   LOG.info("Waiting for LocalStack instance to be fully initialized ...")
   response=requests.get(url)
   content=json.loads(to_str(response.content))
   statuses=[v for k,v in content["services"].items()]
   assert LQRYM(statuses)=={"running"}
  retry(check_status,sleep=3,retries=10)
 @LQRYe
 def pod_config(self):
  return self._pod_config or PodConfigManager.pod_config(self.pod_name)
 @LQRYn
 def get(cls,pod_name,pre_config=LQRYA):
  pod_config=pre_config if pre_config else PodConfigManager.pod_config(pod_name)
  backend=pod_config.get("backend")
  for clazz in cls.__subclasses__():
   if clazz.BACKEND==backend:
    return clazz(pod_name=pod_name,config=pod_config)
  raise LQRYb('Unable to find Cloud Pod manager implementation type "%s"'%backend)
 def deploy_pod_into_instance(self,pod_path):
  delete_pod_zip=LQRYP
  if os.path.isdir(pod_path):
   tmpdir=new_tmp_dir()
   for folder in PERSISTED_FOLDERS:
    src_folder=os.path.join(pod_path,folder)
    tgt_folder=os.path.join(tmpdir,folder)
    cp_r(src_folder,tgt_folder,rm_dest_on_conflict=LQRYU)
   pod_path=create_zip_file(tmpdir)
   rm_rf(tmpdir)
   delete_pod_zip=LQRYU
  zip_content=load_file(pod_path,mode="rb")
  url=get_pods_endpoint()
  result=requests.post(url,data=zip_content)
  if result.status_code>=400:
   raise LQRYb("Unable to restore pod state via local pods management API %s (code %s): %s"%(url,result.status_code,result.content))
  if delete_pod_zip:
   rm_rf(pod_path)
  else:
   return pod_path
 @LQRYD
 def get_state_zip_from_instance(get_content=LQRYP):
  url=f"{get_pods_endpoint()}/state"
  result=requests.get(url)
  if result.status_code>=400:
   raise LQRYb("Unable to get local pod state via management API %s (code %s): %s"%(url,result.status_code,result.content))
  if get_content:
   return result.content
  zip_file=f"{new_tmp_file()}.zip"
  save_file(zip_file,result.content)
  return zip_file
 def get_pod_info(self,pod_data_dir:LQRYo=LQRYA):
  result=PodInfo(self.pod_name)
  if pod_data_dir:
   result.pod_size=disk_usage(pod_data_dir)
   result.persisted_resource_names=get_persisted_resource_names(pod_data_dir)
  return result
class CloudPodManagerCPVCS(CloudPodManager):
 BACKEND="cpvcs"
 @LQRYD
 def parse_pod_name_from_qualifying_name(qualifying_name:LQRYo)->LQRYo:
  return qualifying_name.split(PODS_NAMESPACE_DELIM,1)[1]
 @LQRYD
 def _prepare_archives_from_presigned_urls(content):
  zip_path_version_space=new_tmp_file()
  presigned_urls=content.get("presigned_urls")
  version_space_url=presigned_urls.get("presigned_version_space_url")
  download(url=version_space_url,path=zip_path_version_space)
  zip_paths_state_archives={}
  zip_paths_meta_archives={}
  meta_and_state_urls=presigned_urls.get("presigned_meta_state_urls")
  for version_no,meta_and_state_url in meta_and_state_urls.items():
   zip_path_meta_archive=new_tmp_file()
   zip_path_state_archive=new_tmp_file()
   meta_url=meta_and_state_url["meta"]
   state_url=meta_and_state_url["state"]
   download(meta_url,zip_path_meta_archive)
   download(state_url,zip_path_state_archive)
   zip_paths_meta_archives[version_no]=zip_path_meta_archive
   zip_paths_state_archives[version_no]=zip_path_state_archive
  return zip_path_version_space,zip_paths_meta_archives,zip_paths_state_archives
 @LQRYD
 def _get_max_version_for_pod_from_platform(pod_name:LQRYo,auth_headers):
  url=CloudPodManagerCPVCS.create_platform_url(f"{pod_name}/info/max-version")
  response=safe_requests.get(url=url,headers=auth_headers)
  if response.status_code!=200:
   LOG.warning("Failed to get version information from platform... aborting")
   return
  content=json.loads(response.content)
  remote_max_ver=LQRYd(content["max_ver"])
  return remote_max_ver
 @LQRYD
 def _add_state_files_func(**kwargs):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  dir_name=kwargs.get("dir_name")
  file_name=kwargs.get("fname")
  region=kwargs.get("region")
  service_name=kwargs.get("service_name")
  cpvcs_api.create_state_file_from_fs(path=dir_name,file_name=file_name,service=service_name,region=region)
 def _upload_version_and_product_space(self,presigned_urls):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  presigned_version_space_url=presigned_urls.get("presigned_version_space_url")
  version_space_archive=cpvcs_api.create_version_space_archive()
  with LQRYp(version_space_archive,"rb")as version_space_content:
   self.upload_content(presigned_version_space_url,version_space_content.read())
  presigned_meta_state_urls=presigned_urls.get("presigned_meta_state_urls")
  rm_rf(version_space_archive)
  for version_no,urls in presigned_meta_state_urls.items():
   meta_presigned_url=urls["meta"]
   meta_archive=cpvcs_api.get_version_meta_archive(version_no)
   with LQRYp(meta_archive,"rb")as meta_archive_content:
    self.upload_content(meta_presigned_url,meta_archive_content)
   state_presigned_url=urls["state"]
   state_archive=cpvcs_api.get_version_state_archive(version_no)
   with LQRYp(state_archive,"rb")as state_archive_content:
    self.upload_content(state_presigned_url,state_archive_content)
 def _add_state_to_cpvs_store(self):
  from localstack_ext.bootstrap.cpvcs.utils.common import config_context
  if not config_context.is_initialized():
   LOG.debug("No CPVCS instance detected - Could not push")
   return
  zip_file=self.get_state_zip_from_instance()
  tmp_dir=new_tmp_dir()
  with ZipFile(zip_file,"r")as state_zip:
   state_zip.extractall(tmp_dir)
   api_states_path=os.path.join(tmp_dir,API_STATES_DIR)
   api_states_traverse(api_states_path=api_states_path,side_effect=CloudPodManagerCPVCS._add_state_files_func,mutables=LQRYA)
  rm_rf(zip_file)
  rm_rf(tmp_dir)
 def _pull_versions(self,auth_headers,required_versions:LQRYo):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  url=self.create_platform_url(f"{self.pod_name}?versions={required_versions}")
  response=safe_requests.get(url=url,headers=auth_headers)
  if response.status_code!=200:
   LOG.warning("Failed to pull requested versions from platform")
   return
  content=json.loads(response.content)
  archives=CloudPodManagerCPVCS._prepare_archives_from_presigned_urls(content)
  zip_path_version_space=archives[0]
  zip_paths_meta_archives=archives[1]
  zip_paths_state_archives=archives[2]
  cpvcs_api.merge_from_remote(version_space_archive=zip_path_version_space,meta_archives=zip_paths_meta_archives,state_archives=zip_paths_state_archives)
 def _clone_pod(self,auth_headers):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  url=self.create_platform_url(f"{self.pod_name}/clone")
  response=safe_requests.get(url,headers=auth_headers)
  if response.status_code!=200:
   LOG.warning(f"Failed to clone requested pod {self.pod_name}: {response.content}")
   return
  content=json.loads(response.content)
  archives=CloudPodManagerCPVCS._prepare_archives_from_presigned_urls(content)
  zip_path_version_space=archives[0]
  zip_paths_meta_archives=archives[1]
  zip_paths_state_archives=archives[2]
  remote_info={"storage_uuid":content.get("storage_uuid"),"qualifying_name":content.get("pod_name")}
  pod_name=CloudPodManagerCPVCS.parse_pod_name_from_qualifying_name(remote_info["qualifying_name"])
  cpvcs_api.init_remote(pod_name=pod_name,version_space_archive=zip_path_version_space,meta_archives=zip_paths_meta_archives,state_archives=zip_paths_state_archives,remote_info=remote_info)
 def init(self):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.init(pod_name=self.pod_name)
 def delete(self,remote:LQRYN)->LQRYN:
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_dir=cpvcs_api.config_context.cpvcs_root_dir
  pod_dir=os.path.join(cpvcs_dir,self.pod_name)
  if os.path.isdir(pod_dir):
   rm_rf(pod_dir)
   return LQRYU
  if remote:
   pass
  return LQRYP
 def push(self,comment:LQRYo=LQRYA)->PodInfo:
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  self._add_state_to_cpvs_store()
  if cpvcs_api.is_remotely_managed():
   auth_headers=get_auth_headers()
   local_max_ver=cpvcs_api.get_max_version_no()
   remote_max_ver=CloudPodManagerCPVCS._get_max_version_for_pod_from_platform(pod_name=self.pod_name,auth_headers=auth_headers)
   if local_max_ver<remote_max_ver:
    self.pull()
   cpvcs_api.push(comment=comment)
   url=CloudPodManagerCPVCS.create_platform_url(f"push/{self.pod_name}?version={local_max_ver + 1}")
   response=safe_requests.put(url=url,headers=auth_headers)
   if response.status_code!=200:
    LOG.warning("Failed to get presigned urls to upload new version.. abborting")
    return
   content=json.loads(response.content)
   presigned_urls=content.get("presigned_urls")
   self._upload_version_and_product_space(presigned_urls)
  else:
   created_version=cpvcs_api.push(comment=comment)
   LOG.debug(f"Created new version: {created_version}")
  return PodInfo()
 def pull(self,inject_version_state:LQRYN=LQRYP,reset_state_before:LQRYN=LQRYP,fetch_all:LQRYN=LQRYU):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  auth_headers=get_auth_headers()
  if self.pod_name in cpvcs_api.list_locally_available_pods(show_remote_or_local=LQRYP):
   cpvcs_api.set_pod_context(self.pod_name)
   remote_max_ver=CloudPodManagerCPVCS._get_max_version_for_pod_from_platform(self.pod_name,auth_headers)
   if not remote_max_ver:
    return
   current_max_ver=cpvcs_api.get_max_version_no()
   if remote_max_ver==current_max_ver:
    LOG.info("No new version available remotely. Nothing to pull")
    return
   if fetch_all:
    required_versions=",".join(LQRYl(lambda ver:LQRYo(ver),LQRYg(current_max_ver+1,remote_max_ver+1)))
   else:
    required_versions=current_max_ver
   self._pull_versions(auth_headers=auth_headers,required_versions=required_versions)
  else:
   self._clone_pod(auth_headers=auth_headers)
 def commit(self,message:LQRYo=LQRYA):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  self._add_state_to_cpvs_store()
  completed_revision=cpvcs_api.commit(message=message)
  LOG.debug(f"Completed revision: {completed_revision}")
 def inject(self,version:LQRYd,reset_state:LQRYN):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  if version==-1:
   version=cpvcs_api.get_head().version_number
  tmp_pod_path=cpvcs_api.get_version_state_archive(version)
  if not tmp_pod_path:
   LOG.warning(f"Could not find state for pod with version {version}")
   return
  if reset_state:
   reset_local_state(reset_data_dir=LQRYU,exclude_from_reset=["dynamodb","kinesis","stepfunctions"])
  self.deploy_pod_into_instance(tmp_pod_path)
 def list_versions(self)->List[LQRYo]:
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  version_list=cpvcs_api.list_versions()
  return version_list
 def version_info(self,version:LQRYd):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  if version==-1:
   version=cpvcs_api.get_max_version_no()
  version_info=cpvcs_api.get_version_info(version)
  return version_info
 def version_metamodel(self,version:LQRYd):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  if version==-1:
   version=cpvcs_api.get_max_version_no()
  return cpvcs_api.get_version_metamodel(version_no=version)
 def set_version(self,version:LQRYd,inject_version_state:LQRYN,reset_state:LQRYN,commit_before:LQRYN):
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  version_exists=cpvcs_api.set_active_version(version_no=version,commit_before=commit_before)
  if not version_exists:
   LOG.warning(f"Could not find version {version}")
  if inject_version_state:
   self.inject(version=version,reset_state=reset_state)
 def list_version_commits(self,version:LQRYd)->List[LQRYo]:
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  commits=cpvcs_api.list_version_commits(version_no=version)
  return commits
 def get_commit_diff(self,version:LQRYd,commit:LQRYd)->LQRYo:
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(self.pod_name)
  commit_diff=cpvcs_api.get_commit_diff(version_no=version,commit_no=commit)
  return commit_diff
 def register_remote(self,pod_name:LQRYo)->LQRYN:
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  from localstack_ext.bootstrap.cpvcs.utils.remote_utils import register_remote
  cpvcs_api.set_pod_context(pod_name)
  max_ver=cpvcs_api.get_max_version_no()
  if max_ver==0:
   cpvcs_api.push("Init Version")
   max_ver=1
  auth_headers=get_auth_headers()
  url=self.create_platform_url("register")
  data={"pod_name":pod_name,"max_ver":max_ver}
  data=json.dumps(data)
  response=safe_requests.post(url,data,headers=auth_headers)
  content=json.loads(response.content)
  if response.status_code!=200:
   LOG.warning(f"Failed to register pod {pod_name}: {content}")
   return LQRYP
  remote_info={"storage_uuid":content.get("storage_uuid"),"qualifying_name":content.get("pod_name")}
  presigned_urls=content.get("presigned_urls")
  self._upload_version_and_product_space(presigned_urls)
  register_remote(remote_info=remote_info)
  return LQRYU
 def rename_pod(self,current_pod_name,new_pod_name)->LQRYN:
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  cpvcs_api.set_pod_context(current_pod_name)
  if new_pod_name in cpvcs_api.list_locally_available_pods():
   LOG.warning(f"{new_pod_name} already exists locally")
   return LQRYP
  if cpvcs_api.is_remotely_managed():
   auth_headers=get_auth_headers()
   url=self.create_platform_url(f"{current_pod_name}/rename")
   data={"new_pod_name":new_pod_name}
   data=json.dumps(data)
   response=safe_requests.put(url,data,headers=auth_headers)
   if response.status_code!=200:
    LOG.warning(f"Failed to rename {current_pod_name} to {new_pod_name}: {response.content}")
    return LQRYP
  cpvcs_api.rename_pod(new_pod_name)
  return LQRYU
 def list_pods(self,fetch_remote:LQRYN)->Set[LQRYo]:
  from localstack_ext.bootstrap.cpvcs import cpvcs_api
  result=cpvcs_api.list_locally_available_pods()
  if fetch_remote:
   auth_headers=get_auth_headers()
   url=self.create_platform_url("pods")
   response=safe_requests.get(url,headers=auth_headers)
   content=json.loads(response.content)
   for remote_pod in content.get("registered_pods")or[]:
    result.add(f"remote/{remote_pod}")
  return result
 @LQRYn
 def upload_content(cls,presigned_url:LQRYo,zip_data_content):
  res=safe_requests.put(presigned_url,data=zip_data_content)
  if res.status_code>=400:
   raise LQRYb("Unable to upload pod state to S3 (code %s): %s"%(res.status_code,res.content))
  return res
 @LQRYD
 def create_platform_url(request:LQRYo)->LQRYo:
  base_url="%s/cpvcs"%constants.API_ENDPOINT
  return os.path.join(base_url,request)
class CloudPodManagerFilesystem(CloudPodManager):
 BACKEND="file"
 def push(self,comment:LQRYo=LQRYA)->PodInfo:
  local_folder=self.target_folder()
  print('Pushing state of cloud pod "%s" to local folder: %s'%(self.pod_name,local_folder))
  mkdir(local_folder)
  zip_file=self.get_state_zip_from_instance()
  unzip(zip_file,local_folder)
  chmod_r(local_folder,0o777)
  result=self.get_pod_info(local_folder)
  print("Done.")
  return result
 def pull(self,inject_version_state:LQRYN=LQRYP,reset_state_before:LQRYN=LQRYP,fetch_all:LQRYN=LQRYA):
  local_folder=self.target_folder()
  if not os.path.exists(local_folder):
   print('WARN: Local path of cloud pod "%s" does not exist: %s'%(self.pod_name,local_folder))
   return
  print('Pulling state of cloud pod "%s" from local folder: %s'%(self.pod_name,local_folder))
  self.deploy_pod_into_instance(local_folder)
 def target_folder(self):
  local_folder=re.sub(r"^file://","",self.pod_config.get("url",""))
  return local_folder
class CloudPodManagerManaged(CloudPodManager):
 BACKEND="managed"
 def push(self,comment:LQRYo=LQRYA)->PodInfo:
  zip_data_content=self.get_state_zip_from_instance(get_content=LQRYU)
  print('Pushing state of cloud pod "%s" to backend server (%s KB)'%(self.pod_name,format_number(LQRYc(zip_data_content)/1000.0)))
  self.push_content(self.pod_name,zip_data_content)
  print("Done.")
  result=self.get_pod_info()
  result.pod_size_compressed=LQRYc(zip_data_content)
  return result
 def pull(self,inject_version_state:LQRYN=LQRYP,reset_state_before:LQRYN=LQRYP,fetch_all:LQRYN=LQRYA):
  presigned_url=self.presigned_url(self.pod_name,"pull")
  print('Pulling state of cloud pod "%s" from managed storage'%self.pod_name)
  zip_path=new_tmp_file()
  download(presigned_url,zip_path)
  self.deploy_pod_into_instance(zip_path)
  rm_rf(zip_path)
 @LQRYD
 def presigned_url(pod_name:LQRYo,mode:LQRYo)->LQRYo:
  data={"pod_name":pod_name,"mode":mode}
  data=json.dumps(data)
  auth_headers=get_auth_headers()
  url="%s/cloudpods/data"%constants.API_ENDPOINT
  if ext_config.SYNC_POD_VERSION:
   url=f"{url}?version={ext_config.SYNC_POD_VERSION}"
  response=safe_requests.post(url,data,headers=auth_headers)
  content=response.content
  if response.status_code>=400:
   raise LQRYb("Unable to get cloud pod presigned URL (code %s): %s"%(response.status_code,content))
  content=json.loads(to_str(content))
  return content["presignedURL"]
 @LQRYn
 def push_content(cls,pod_name,zip_data_content):
  presigned_url=cls.presigned_url(pod_name,"push")
  res=safe_requests.put(presigned_url,data=zip_data_content)
  if res.status_code>=400:
   raise LQRYb("Unable to push pod state to API (code %s): %s"%(res.status_code,res.content))
  return res
class CloudPodManagerGit(CloudPodManager):
 BACKEND="git"
 def push(self,comment:LQRYo=LQRYA):
  repo=self.local_repo()
  branch=to_bytes(self.pod_config.get("branch"))
  remote_location=self.pod_config.get("url")
  try:
   porcelain.pull(repo,remote_location,refspecs=branch)
  except LQRYb as e:
   if self.has_git_cli():
    run("cd %s; git checkout %s; git pull"%(to_str(branch),self.clone_dir))
   else:
    LOG.info("Unable to pull repo: %s %s",e,traceback.format_exc())
  zip_file=self.get_state_zip_from_instance()
  tmp_data_dir=new_tmp_dir()
  unzip(zip_file,tmp_data_dir)
  is_empty_repo=b"HEAD" not in repo or repo.refs.allkeys()=={b"HEAD"}
  if is_empty_repo:
   LOG.debug("Initializing empty repository %s"%self.clone_dir)
   init_file=os.path.join(self.clone_dir,".init")
   save_file(init_file,"")
   porcelain.add(repo,init_file)
   porcelain.commit(repo,message="Initial commit")
  if branch not in repo:
   porcelain.branch_create(repo,branch,force=LQRYU)
  self.switch_branch(branch)
  for folder in PERSISTED_FOLDERS:
   LOG.info("Copying persistence folder %s to local git repo %s"%(folder,self.clone_dir))
   src_folder=os.path.join(tmp_data_dir,folder)
   tgt_folder=os.path.join(self.clone_dir,folder)
   cp_r(src_folder,tgt_folder)
   files=tgt_folder
   if os.path.isdir(files):
    files=[os.path.join(root,f)for root,_,files in os.walk(tgt_folder)for f in files]
   if files:
    porcelain.add(repo,files)
  porcelain.commit(repo,message="Update cloud pod state")
  try:
   porcelain.push(repo,remote_location,branch)
  except LQRYb:
   if not self.has_git_cli():
    raise
   run("cd %s; git push origin %s"%(self.clone_dir,to_str(branch)))
  result=self.get_pod_info(tmp_data_dir)
  return result
 def pull(self,inject_version_state:LQRYN=LQRYP,reset_state_before:LQRYN=LQRYP,fetch_all:LQRYN=LQRYA):
  repo=self.local_repo()
  client,path=self.client()
  remote_refs=client.fetch(path,repo)
  branch=self.pod_config.get("branch")
  remote_ref=b"refs/heads/%s"%to_bytes(branch)
  if remote_ref not in remote_refs:
   raise LQRYb('Unable to find branch "%s" in remote git repo'%branch)
  remote_location=self.pod_config.get("url")
  self.switch_branch(branch)
  branch_ref=b"refs/heads/%s"%to_bytes(branch)
  from dulwich.errors import HangupException
  try:
   porcelain.pull(repo,remote_location,branch_ref)
  except HangupException:
   pass
  self.deploy_pod_into_instance(self.clone_dir)
 def client(self):
  client,path=get_transport_and_path_from_url(self.pod_config.get("url"))
  return client,path
 def local_repo(self):
  self.clone_dir=LQRYK(self,"clone_dir",LQRYA)
  if not self.clone_dir:
   pod_dir_name=re.sub(r"(\s|/)+","",self.pod_name)
   self.clone_dir=os.path.join(config.TMP_FOLDER,"pods",pod_dir_name,"repo")
   mkdir(self.clone_dir)
   if not os.path.exists(os.path.join(self.clone_dir,".git")):
    porcelain.clone(self.pod_config.get("url"),self.clone_dir)
    self.switch_branch(self.pod_config.get("branch"))
  return Repo(self.clone_dir)
 def switch_branch(self,branch):
  repo=self.local_repo()
  if self.has_git_cli():
   return run("cd %s; git checkout %s"%(self.clone_dir,to_str(branch)))
  branch_ref=b"refs/heads/%s"%to_bytes(branch)
  if branch_ref not in repo.refs:
   branch_ref=b"refs/remotes/origin/%s"%to_bytes(branch)
  repo.reset_index(repo[branch_ref].tree)
  repo.refs.set_symbolic_ref(b"HEAD",branch_ref)
 def has_git_cli(self):
  return is_command_available("git")
class PodConfigManagerMeta(LQRYr):
 def __getattr__(cls,attr):
  def _call(*args,**kwargs):
   result=LQRYA
   for manager in cls.CHAIN:
    try:
     tmp=LQRYK(manager,attr)(*args,**kwargs)
     if tmp:
      if not result:
       result=tmp
      elif LQRYS(tmp,LQRYC)and LQRYS(result,LQRYC):
       result.extend(tmp)
    except LQRYb:
     if LOG.isEnabledFor(logging.DEBUG):
      LOG.exception("error during PodConfigManager call chain")
   if result is not LQRYA:
    return result
   raise LQRYb('Unable to run operation "%s" for local or remote configuration'%attr)
  return _call
class PodConfigManager(LQRYH,metaclass=PodConfigManagerMeta):
 CHAIN=[]
 @LQRYn
 def pod_config(cls,pod_name):
  pods=PodConfigManager.list_pods()
  pod_config=[pod for pod in pods if pod["pod_name"]==pod_name]
  if not pod_config:
   raise LQRYb('Unable to find config for pod named "%s"'%pod_name)
  return pod_config[0]
class PodConfigManagerLocal(LQRYH):
 CONFIG_FILE=".localstack.yml"
 def list_pods(self):
  local_pods=self._load_config(safe=LQRYU).get("pods",{})
  local_pods=[{"pod_name":k,"state":"Local Only",**v}for k,v in local_pods.items()]
  existing_names=LQRYM([pod["pod_name"]for pod in local_pods])
  result=[pod for pod in local_pods if pod["pod_name"]not in existing_names]
  return result
 def store_pod_metadata(self,pod_name,metadata):
  pass
 def _load_config(self,safe=LQRYP):
  try:
   return yaml.safe_load(to_str(load_file(self.CONFIG_FILE)))
  except LQRYb:
   if safe:
    return{}
   raise LQRYb('Unable to find and parse config file "%s"'%self.CONFIG_FILE)
class PodConfigManagerRemote(LQRYH):
 def list_pods(self):
  result=[]
  auth_headers=get_auth_headers()
  url="%s/cloudpods"%constants.API_ENDPOINT
  response=safe_requests.get(url,headers=auth_headers)
  content=response.content
  if response.status_code>=400:
   raise LQRYb("Unable to fetch list of pods from API (code %s): %s"%(response.status_code,content))
  remote_pods=json.loads(to_str(content)).get("cloudpods",[])
  remote_pods=[{"state":"Shared",**pod}for pod in remote_pods]
  result.extend(remote_pods)
  return result
 def store_pod_metadata(self,pod_name,metadata):
  auth_headers=get_auth_headers()
  metadata["pod_name"]=pod_name
  response=safe_requests.post("%s/cloudpods"%constants.API_ENDPOINT,json.dumps(metadata),headers=auth_headers)
  content=response.content
  if response.status_code>=400:
   raise LQRYb("Unable to store pod metadata in API (code %s): %s"%(response.status_code,content))
  return json.loads(to_str(content))
PodConfigManager.CHAIN.append(PodConfigManagerLocal())
PodConfigManager.CHAIN.append(PodConfigManagerRemote())
def init_cpvcs(pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo],**kwargs):
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 backend.init()
def delete_pod(pod_name:LQRYo,remote:LQRYN,pre_config:Dict[LQRYo,LQRYo])->LQRYN:
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 result=backend.delete(remote=remote)
 return result
def register_remote(pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo],**kwargs)->LQRYN:
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 result=backend.register_remote(pod_name=pod_name)
 return result
def rename_pod(current_pod_name:LQRYo,new_pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo],**kwargs):
 backend=CloudPodManager.get(pod_name=current_pod_name,pre_config=pre_config)
 result=backend.rename_pod(current_pod_name=current_pod_name,new_pod_name=new_pod_name)
 return result
def list_pods_cpvcs(remote:LQRYN,pre_config:Dict[LQRYo,LQRYo],**kwargs)->List[LQRYo]:
 backend=CloudPodManager.get(pod_name="",pre_config=pre_config)
 result=backend.list_pods(fetch_remote=remote)
 return result
def commit_state(pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo],message:LQRYo=LQRYA,**kwargs):
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 backend.commit(message=message)
def inject_state(pod_name:LQRYo,version:LQRYd,reset_state:LQRYN,pre_config:Dict[LQRYo,LQRYo],**kwargs):
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 backend.inject(version=version,reset_state=reset_state)
def list_versions(pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo],**kwargs)->List[LQRYo]:
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 versions=backend.list_versions()
 return versions
def get_version_info(version:LQRYd,pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo],**kwargs):
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 info=backend.version_info(version=version)
 return info
def get_version_metamodel(version:LQRYd,pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo],**kwargs):
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 metamodel=backend.version_metamodel(version=version)
 return metamodel
def set_version(version:LQRYd,inject_version_state:LQRYN,reset_state:LQRYN,commit_before:LQRYN,pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo],**kwargs)->LQRYN:
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 success=backend.set_version(version=version,inject_version_state=inject_version_state,reset_state=reset_state,commit_before=commit_before)
 return success
def list_version_commits(version:LQRYd,pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo])->List[LQRYo]:
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 commits=backend.list_version_commits(version=version)
 return commits
def get_commit_diff(version:LQRYd,commit:LQRYd,pod_name:LQRYo,pre_config:Dict[LQRYo,LQRYo])->LQRYo:
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 commit_diff=backend.get_commit_diff(version=version,commit=commit)
 return commit_diff
def push_state(pod_name,pre_config=LQRYA,squash_commits=LQRYP,comment=LQRYA,**kwargs):
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 pod_config=clone(backend.pod_config)
 pod_info=backend.push(comment=comment)
 pod_config["size"]=pod_info.pod_size or pod_info.pod_size_compressed
 pod_config["available_resources"]=pod_info.persisted_resource_names
 return pod_config
def get_pods_endpoint():
 edge_url=config.get_edge_url()
 return f"{edge_url}{API_PATH_PODS}"
def pull_state(pod_name,inject_version_state=LQRYP,reset_state_before=LQRYP,**kwargs):
 pre_config=kwargs.get("pre_config",LQRYA)
 if not pod_name:
  raise LQRYb("Need to specify a pod name")
 backend=CloudPodManager.get(pod_name=pod_name,pre_config=pre_config)
 backend.pull(inject_version_state=inject_version_state,reset_state_before=reset_state_before)
 print("Done.")
def reset_local_state(reset_data_dir=LQRYP,exclude_from_reset:List[LQRYo]=LQRYA):
 url=f"{get_pods_endpoint()}/state"
 if reset_data_dir:
  url+="/datadir"
 if exclude_from_reset:
  url+=f"?exclude={','.join(exclude_from_reset)}"
 print("Sending request to reset the service states in local instance ...")
 result=requests.delete(url)
 if result.status_code>=400:
  raise LQRYb("Unable to reset service state via local management API %s (code %s): %s"%(url,result.status_code,result.content))
 print("Done.")
def list_pods(args):
 return PodConfigManager.list_pods()
def get_data_dir_from_container()->LQRYo:
 try:
  details=DOCKER_CLIENT.inspect_container(config.MAIN_CONTAINER_NAME)
  mounts=details.get("Mounts")
  env=details.get("Config",{}).get("Env",[])
  data_dir_env=[e for e in env if e.startswith("DATA_DIR=")][0].partition("=")[2]
  try:
   data_dir_host=[m for m in mounts if m["Destination"]==data_dir_env][0]["Source"]
   data_dir_host=re.sub(r"^(/host_mnt)?",r"",data_dir_host)
   data_dir_env=data_dir_host
  except LQRYb:
   LOG.debug(f"No docker volume for data dir '{data_dir_env}' detected")
  return data_dir_env
 except LQRYb:
  LOG.warning('''Unable to determine DATA_DIR from LocalStack Docker container - please make sure $MAIN_CONTAINER_NAME is configured properly''')
def get_persisted_resource_names(data_dir)->List[LQRYo]:
 names=[]
 with os.scandir(data_dir)as entries:
  for entry in entries:
   if entry.is_dir()and entry.name!="api_states":
    names.append(entry.name)
 with os.scandir(os.path.join(data_dir,"api_states"))as entries:
  for entry in entries:
   if entry.is_dir()and LQRYc(os.listdir(entry.path))>0:
    names.append(entry.name)
 LOG.debug(f"Detected state files for the following APIs: {names}")
 return names
PODS_NAMESPACE_DELIM="-"
# Created by pyminifier (https://github.com/liftoff/pyminifier)
