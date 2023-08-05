import logging
Kjcqu=None
KjcqP=str
Kjcqn=True
Kjcqx=int
KjcqW=open
KjcqR=bool
KjcqS=classmethod
import os
from typing import List
from localstack import config as localstack_config
from localstack_ext.bootstrap.cpvcs.constants import(COMPRESSION_FORMAT,CPVCS_DIR,DEFAULT_POD_DIR,DELTA_LOG_DIR,HEAD_FILE,KNOWN_VER_FILE,MAX_VER_FILE,META_ZIP,OBJ_STORE_DIR,REFS_DIR,REMOTE_FILE,REV_SUB_DIR,STATE_ZIP,VER_LOG_FILE,VER_LOG_STRUCTURE,VER_SUB_DIR,VERSION_SPACE_DIRS,VERSION_SPACE_FILES)
LOG=logging.getLogger(__name__)
class CPVCSConfigContext:
 default_instance=Kjcqu
 def __init__(self,pod_root_dir:KjcqP):
  self.cpvcs_root_dir=pod_root_dir
  self.pod_root_dir=pod_root_dir
  self.user=Kjcqu
 def get_pod_context(self)->KjcqP:
  return os.path.basename(self.pod_root_dir)
 def get_context_user(self)->KjcqP:
  return self.user
 def get_pod_root_dir(self)->KjcqP:
  return self.pod_root_dir
 def get_head_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,HEAD_FILE)
 def get_max_ver_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,MAX_VER_FILE)
 def get_known_ver_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,KNOWN_VER_FILE)
 def get_ver_log_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,VER_LOG_FILE)
 def get_obj_store_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,OBJ_STORE_DIR)
 def get_rev_obj_store_path(self)->KjcqP:
  return os.path.join(self.get_obj_store_path(),REV_SUB_DIR)
 def get_ver_obj_store_path(self)->KjcqP:
  return os.path.join(self.get_obj_store_path(),VER_SUB_DIR)
 def get_ver_refs_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,REFS_DIR,VER_SUB_DIR)
 def get_rev_refs_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,REFS_DIR,REV_SUB_DIR)
 def get_version_ref_file_path(self,version_ref:KjcqP)->KjcqP:
  return os.path.join(self.get_ver_refs_path(),version_ref)
 def get_delta_log_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,self.get_obj_store_path(),DELTA_LOG_DIR)
 def get_version_meta_archive_path(self,version_no,with_format:KjcqR=Kjcqn)->KjcqP:
  version_meta_path=os.path.join(self.get_pod_root_dir(),META_ZIP.format(version_no=version_no))
  if not with_format:
   return version_meta_path
  return f"{version_meta_path}.{COMPRESSION_FORMAT}"
 def get_version_state_archive_path(self,version_no,with_format:KjcqR=Kjcqn)->KjcqP:
  version_state_path=os.path.join(self.get_pod_root_dir(),STATE_ZIP.format(version_no=version_no))
  if not with_format:
   return version_state_path
  return f"{version_state_path}.{COMPRESSION_FORMAT}"
 def update_ver_log(self,author:KjcqP,ver_no:Kjcqx,rev_id:KjcqP,rev_no:Kjcqx):
  with KjcqW(self.get_ver_log_path(),"a")as fp:
   fp.write(f"{VER_LOG_STRUCTURE.format(author=author, ver_no=ver_no, rev_rid_no=f'{rev_id}_{rev_no}')}\n")
 def create_version_symlink(self,name:KjcqP,key:KjcqP=Kjcqu)->KjcqP:
  return self._create_symlink(name,key,self.get_ver_refs_path())
 def create_revision_symlink(self,name:KjcqP,key:KjcqP=Kjcqu)->KjcqP:
  return self._create_symlink(name,key,self.get_rev_refs_path())
 def is_initialized(self)->KjcqR:
  return self.pod_root_dir and os.path.isdir(self.pod_root_dir)
 def _create_symlink(self,name:KjcqP,key:KjcqP,path:KjcqP)->KjcqP:
  rel_path=os.path.relpath(path,start=self.get_pod_root_dir())
  rel_symlink=os.path.join(rel_path,name)
  if key:
   symlink=os.path.join(path,name)
   with KjcqW(symlink,"w")as fp:
    fp.write(key)
  return rel_symlink
 def _get_head_key(self)->KjcqP:
  return self._get_key(self.get_head_path())
 def get_max_ver_key(self)->KjcqP:
  return self._get_key(self.get_max_ver_path())
 def _get_key(self,path:KjcqP)->KjcqP:
  with KjcqW(path,"r")as fp:
   rel_key_path=fp.readline().strip()
  key_path=self.get_pod_absolute_path(rel_key_path)
  with KjcqW(key_path,"r")as fp:
   key=fp.readline()
   return key
 def get_pod_absolute_path(self,rel_path):
  return os.path.join(self.get_pod_root_dir(),rel_path)
 def get_obj_file_path(self,key:KjcqP)->KjcqP:
  return os.path.join(self.get_obj_store_path(),key)
 def get_remote_info_path(self)->KjcqP:
  return os.path.join(self.pod_root_dir,REMOTE_FILE)
 def is_remotly_managed(self,pod_name:KjcqP=Kjcqu)->KjcqR:
  if pod_name:
   return os.path.isfile(os.path.join(self.cpvcs_root_dir,pod_name,REMOTE_FILE))
  else:
   return os.path.isfile(self.get_remote_info_path())
 def set_pod_context(self,pod_name:KjcqP):
  configs=localstack_config.load_config_file()
  login_info=configs.get("login",{})
  user=login_info.get("username","unknown")
  self.pod_root_dir=os.path.join(self.cpvcs_root_dir,pod_name)
  self.user=user
 def pod_exists_locally(self,pod_name:KjcqP)->KjcqR:
  return os.path.isdir(os.path.join(self.cpvcs_root_dir,pod_name))
 def rename_pod_name(self,new_pod_name:KjcqP):
  curr_name=self.get_pod_root_dir()
  new_name=os.path.join(self.cpvcs_root_dir,new_pod_name)
  os.rename(curr_name,new_name)
  self.set_pod_context(new_name)
 def get_pod_name(self)->KjcqP:
  return os.path.basename(self.get_pod_root_dir())
 def get_version_space_dir_paths(self)->List[KjcqP]:
  return[os.path.join(self.get_pod_root_dir(),directory)for directory in VERSION_SPACE_DIRS]
 def get_version_space_file_paths(self)->List[KjcqP]:
  return[os.path.join(self.get_pod_root_dir(),filename)for filename in VERSION_SPACE_FILES]
 @KjcqS
 def get(cls):
  if not cls.default_instance:
   pod_root_dir=os.environ.get("POD_DIR")
   if not pod_root_dir:
    pod_root_dir=os.path.join(localstack_config.TMP_FOLDER,DEFAULT_POD_DIR)
   pod_root_dir=os.path.join(pod_root_dir,CPVCS_DIR)
   cls.default_instance=CPVCSConfigContext(pod_root_dir)
  return cls.default_instance
config_context=CPVCSConfigContext.get()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
