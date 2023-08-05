import os.path
OIyzC=bytes
OIyzr=None
OIyzw=isinstance
OIyzu=list
OIyzN=getattr
OIyzX=open
OIyzT=property
OIyzm=Exception
OIyzk=setattr
OIyzF=True
import sys
import traceback
from importlib.abc import MetaPathFinder,SourceLoader
from importlib.util import spec_from_file_location
import pyaes
class DecryptionHandler:
 decryption_key:OIyzC
 def __init__(self,decryption_key:OIyzC):
  self.decryption_key=decryption_key
 def decrypt(self,content)->OIyzC:
  cipher=pyaes.AESModeOfOperationCBC(self.decryption_key,iv="\0"*16)
  decrypter=pyaes.Decrypter(cipher)
  decrypted=decrypter.feed(content)
  decrypted+=decrypter.feed()
  decrypted=decrypted.partition(b"\0")[0]
  return decrypted
class EncryptedFileFinder(MetaPathFinder):
 decryption_handler:DecryptionHandler
 def __init__(self,decryption_handler:DecryptionHandler):
  self.decryption_handler=decryption_handler
 def find_spec(self,fullname,path,target=OIyzr):
  if path and not OIyzw(path,OIyzu):
   path=OIyzu(OIyzN(path,"_path",[]))
  if not path:
   return OIyzr
  name=fullname.split(".")[-1]
  file_path=os.path.join(path[0],name+".py")
  enc=file_path+".enc"
  if not os.path.isfile(enc):
   return OIyzr
  if os.path.isfile(file_path):
   return OIyzr
  return spec_from_file_location(fullname,enc,loader=DecryptingLoader(enc,self.decryption_handler))
class DecryptingLoader(SourceLoader):
 decryption_handler:DecryptionHandler
 def __init__(self,encrypted_file,decryption_handler:DecryptionHandler):
  self.encrypted_file=encrypted_file
  self.decryption_handler=decryption_handler
 def get_filename(self,fullname):
  return self.encrypted_file
 def get_data(self,filename):
  with OIyzX(filename,"rb")as f:
   data=f.read()
  data=self.decryption_handler.decrypt(data)
  return data
def init_source_decryption(decryption_handler:DecryptionHandler):
 sys.meta_path.insert(0,EncryptedFileFinder(decryption_handler))
 patch_traceback_lines()
def patch_traceback_lines():
 if OIyzN(traceback.FrameSummary,"_ls_patch_applied",OIyzr):
  return
 @OIyzT
 def line(self):
  try:
   return line_orig.fget(self)
  except OIyzm:
   self._line=""
   return self._line
 line_orig=traceback.FrameSummary.line
 OIyzk(traceback.FrameSummary,"line",line)
 traceback.FrameSummary._ls_patch_applied=OIyzF
# Created by pyminifier (https://github.com/liftoff/pyminifier)
