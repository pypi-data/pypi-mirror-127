import logging
NIlnA=True
NIlnD=False
NIlnk=None
NIlnT=Exception
NIlnr=open
NIlno=bool
NIlna=str
NIlne=int
NIlnU=dict
NIlnd=list
NIlnO=isinstance
NIlnJ=super
import os
import sys
from typing import Any,Callable,Dict,List
import click
from localstack.cli import LocalstackCli,LocalstackCliPlugin,console
class ProCliPlugin(LocalstackCliPlugin):
 name="pro"
 def should_load(self):
  e=os.getenv("LOCALSTACK_API_KEY")
  return NIlnA if e else NIlnD
 def is_active(self):
  return self.should_load()
 def attach(self,cli:LocalstackCli)->NIlnk:
  group:click.Group=cli.group
  group.add_command(cmd_login)
  group.add_command(cmd_logout)
  group.add_command(daemons)
  group.add_command(pod)
  group.add_command(dns)
  group.add_command(cpvcs)
@click.group(name="daemons",help="Manage local daemon processes")
def daemons():
 pass
@click.command(name="login",help="Log in with your account credentials")
@click.option("--username",help="Username for login")
@click.option("--provider",default="internal",help="OAuth provider (default: localstack internal login)")
def cmd_login(username,provider):
 from localstack_ext.bootstrap import auth
 try:
  auth.login(provider,username)
  console.print("successfully logged in")
 except NIlnT as e:
  console.print("authentication error: %s"%e)
@click.command(name="logout",help="Log out and delete any session tokens")
def cmd_logout():
 from localstack_ext.bootstrap import auth
 try:
  auth.logout()
  console.print("successfully logged out")
 except NIlnT as e:
  console.print("logout error: %s"%e)
@daemons.command(name="start",help="Start local daemon processes")
def cmd_daemons_start():
 from localstack_ext.bootstrap import local_daemon
 console.log("Starting local daemons processes ...")
 local_daemon.start_in_background()
@daemons.command(name="stop",help="Stop local daemon processes")
def cmd_daemons_stop():
 from localstack_ext.bootstrap import local_daemon
 console.log("Stopping local daemons processes ...")
 local_daemon.kill_servers()
@daemons.command(name="log",help="Show log of daemon process")
def cmd_daemons_log():
 from localstack_ext.bootstrap import local_daemon
 file_path=local_daemon.get_log_file_path()
 if not os.path.isfile(file_path):
  console.print("no log found")
 else:
  with NIlnr(file_path,"r")as fd:
   for line in fd:
    sys.stdout.write(line)
    sys.stdout.flush()
@click.group(name="dns",help="Manage DNS settings of your host")
def dns():
 pass
@dns.command(name="systemd-resolved",help="Manage DNS settings of systemd-resolved (Ubuntu, Debian etc.)")
@click.option("--revert",is_flag=NIlnA,help="Revert systemd-resolved settings for the docker interface")
def cmd_dns_systemd(revert:NIlno):
 import localstack_ext.services.dns_server
 from localstack_ext.bootstrap.dns_utils import configure_systemd
 console.print("Configuring systemd-resolved...")
 logger_name=localstack_ext.services.dns_server.LOG.name
 localstack_ext.services.dns_server.LOG=ConsoleLogger(logger_name)
 configure_systemd(revert)
def _cpvcs_initialized(pod_name:NIlna)->NIlno:
 from localstack_ext.bootstrap.cpvcs.utils.common import config_context
 config_context.set_pod_context(pod_name=pod_name)
 if not config_context.is_initialized():
  console.print("[red]Error:[/red] Could not find local CPVCS instance")
  return NIlnD
 return NIlnA
@click.group(name="cpvcs",help="Experimental Cloud Pods with elaborate versioning mechanism")
def cpvcs():
 from localstack_ext.bootstrap.licensing import is_logged_in
 if not is_logged_in():
  console.print("[red]Error:[/red] not logged in, please log in first")
  sys.exit(1)
@cpvcs.command(name="init",help="Creates a new cloud pod with cpvcs enabled")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_init(name:NIlna):
 from localstack_ext.bootstrap import pods_client
 from localstack_ext.bootstrap.cpvcs.utils.common import config_context
 config_context.set_pod_context(name)
 if config_context.is_initialized():
  console.print(f"[red]Error:[/red] CPVCS already instanciated for pod {name}")
 else:
  pods_client.init_cpvcs(pod_name=name,pre_config={"backend":"cpvcs"})
  console.print("Successfully created local CPVCS instance!")
@cpvcs.command(name="delete",help="Deletes the specified cloud pod. By default only locally")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
@click.option("-r","--remote",help="Whether the Pod should also be deleted remotely.",is_flag=NIlnA,default=NIlnD)
def cmd_cpvcs_delete(name:NIlna,remote:NIlno):
 from localstack_ext.bootstrap import pods_client
 result=pods_client.delete_pod(pod_name=name,remote=remote,pre_config={"backend":"cpvcs"})
 if result:
  console.print(f"Successfully deleted {name}")
 else:
  console.print(f"[yellow]{name} not available locally[/yellow]")
@cpvcs.command(name="register",help="Registers a local cloudpod instance with platform")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_register_remote(name:NIlna):
 from localstack_ext.bootstrap import pods_client
 if _cpvcs_initialized(pod_name=name):
  result=pods_client.register_remote(pod_name=name,pre_config={"backend":"cpvcs"})
  if result:
   console.print(f"Successfully registred {name} with remote!")
  else:
   console.print(f"[red]Error:[/red] Pod with name {name} is already registered")
@cpvcs.command(name="rename",help="Renames the pod. If the pod is remotely registered, change is also propagated to remote")
@click.option("-n","--name",help="Current Name of the cloud pod",required=NIlnA)
@click.option("-nn","--new-name",help="New name of the cloud pod",required=NIlnA)
def cmd_cpvcs_rename(name:NIlna,new_name:NIlna):
 from localstack_ext.bootstrap import pods_client
 if _cpvcs_initialized(pod_name=name):
  result=pods_client.rename_pod(current_pod_name=name,new_pod_name=new_name,pre_config={"backend":"cpvcs"})
  if result:
   console.print(f"Successfully renamed {name} to {new_name}")
  else:
   console.print(f"[red]Error:[/red] Failed to rename {name} to {new_name}")
@cpvcs.command(name="commit",help="Commits the current expansion point and creates a new (empty) revision")
@click.option("-m","--message",help="Add a comment describing the revision")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_commit(message:NIlna,name:NIlna):
 from localstack_ext.bootstrap import pods_client
 if _cpvcs_initialized(pod_name=name):
  pods_client.commit_state(pod_name=name,pre_config={"backend":"cpvcs"},message=message)
  console.print("Successfully commited the current state")
@cpvcs.command(name="push",help="Creates a new version by using the state files in the current expansion point (latest commit)")
@click.option("--squash",is_flag=NIlnA,help="Squashes commits together, so only the latest commit is stored in the revision graph")
@click.option("-m","--message",help="Add a comment describing the version")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_push(squash:NIlno,message:NIlna,name:NIlna):
 from localstack_ext.bootstrap import pods_client
 if _cpvcs_initialized(pod_name=name):
  pods_client.push_state(pod_name=name,pre_config={"backend":"cpvcs"},squash_commits=squash,comment=message)
  console.print("Successfully pushed the current state")
@cpvcs.command(name="inject",help="Injects the state from a version into the application runtime")
@click.option("-v","--version",default="-1",type=NIlne,help="Loads the state of the specified version - Most recent one by default")
@click.option("--reset",is_flag=NIlnA,default=NIlnD,help="Will reset the application state before injecting")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_inject(version:NIlne,reset:NIlno,name:NIlna):
 from localstack_ext.bootstrap import pods_client
 if _cpvcs_initialized(pod_name=name):
  pods_client.inject_state(pod_name=name,version=version,reset_state=reset,pre_config={"backend":"cpvcs"})
@click.option("--inject/--no-inject",default=NIlnA,help="Whether the latest version of the pulled pod should be injected")
@click.option("--reset/--no-reset",default=NIlnA,help="Whether the current application state should be reset after the pod has been pulled")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
@cpvcs.command(name="pull",help="Injects the state from a version into the application runtime")
def cmd_cpvcs_pull(name:NIlna,inject:NIlno,reset:NIlno):
 from localstack_ext.bootstrap import pods_client
 pods_client.pull_state(pod_name=name,inject_version_state=inject,reset_state_before=reset,pre_config={"backend":"cpvcs"})
@cpvcs.command(name="list-pods",help="Lists all pods and indicates which pods exist locally and, by default, which ones are managed remotely")
@click.option("--remote","-r",is_flag=NIlnA,default=NIlnD)
def cmd_cpvcs_list_pods(remote:NIlno):
 from localstack_ext.bootstrap import pods_client
 pods=pods_client.list_pods_cpvcs(remote=remote,pre_config={"backend":"cpvcs"})
 if not pods:
  console.print(f"[yellow]No pods available {'locally' if not remote else ''}[/yellow]")
 else:
  console.print("\n".join(pods))
@cpvcs.command(name="versions",help="Lists all available version numbers")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_versions(name:NIlna):
 if _cpvcs_initialized(pod_name=name):
  from localstack_ext.bootstrap import pods_client
  version_list=pods_client.list_versions(pod_name=name,pre_config={"backend":"cpvcs"})
  result="\n".join(version_list)
  console.print(result)
@cpvcs.command(name="version-info")
@click.option("-v","--version",required=NIlnA,type=NIlne)
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_version_info(version:NIlne,name:NIlna):
 if _cpvcs_initialized(pod_name=name):
  from localstack_ext.bootstrap import pods_client
  info=pods_client.get_version_info(version=version,pod_name=name,pre_config={"backend":"cpvcs"})
  console.print_json(info)
@cpvcs.command(name="metamodel",help="Displays the content metamodel as json")
@click.option("-v","--version",type=NIlne,default=-1,help="Latest version by default")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_version_metamodel(version:NIlne,name:NIlna):
 if _cpvcs_initialized(pod_name=name):
  from localstack_ext.bootstrap import pods_client
  metamodel=pods_client.get_version_metamodel(version=version,pod_name=name,pre_config={"backend":"cpvcs"})
  if metamodel:
   console.print_json(metamodel)
  else:
   console.print(f"[red]Could not find metaodel for pod {name} with version {version}[/red]")
@cpvcs.command(name="set-version",help="Set HEAD to a specific version")
@click.option("-v","--version",required=NIlnA,type=NIlne,help="The version the state should be set to")
@click.option("--inject/--no-inject",default=NIlnA,help="Whether the state should be directly injected into the application runtime after changing version")
@click.option("--reset/--no-reset",default=NIlnA,help="Whether the current application state should be reset before changing version")
@click.option("--commit-before",is_flag=NIlnD,help="Whether the current application state should be commited to the currently selected version before changing version")
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_set_version(version:NIlne,inject:NIlno,reset:NIlno,commit_before:NIlno,name:NIlna):
 if _cpvcs_initialized(pod_name=name):
  from localstack_ext.bootstrap import pods_client
  pods_client.set_version(version=version,inject_version_state=inject,reset_state=reset,commit_before=commit_before,pod_name=name,pre_config={"backend":"cpvcs"})
@cpvcs.command(name="commits",help="Shows the commit history of a version")
@click.option("--version","-v",default=-1)
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_commits(version:NIlne,name:NIlna):
 if _cpvcs_initialized(pod_name=name):
  from localstack_ext.bootstrap import pods_client
  commits=pods_client.list_version_commits(version=version,pod_name=name,pre_config={"backend":"cpvcs"})
  result="\n".join(commits)
  console.print(result)
@cpvcs.command(name="commit-diff",help="Shows the changes made by a commit")
@click.option("--version","-v",required=NIlnA)
@click.option("--commit","-c",required=NIlnA)
@click.option("-n","--name",help="Name of the cloud pod",required=NIlnA)
def cmd_cpvcs_commit_diff(version:NIlne,commit:NIlne,name:NIlna):
 if _cpvcs_initialized(pod_name=name):
  from localstack_ext.bootstrap import pods_client
  commit_diff=pods_client.get_commit_diff(version=version,commit=commit,pod_name=name,pre_config={"backend":"cpvcs"})
  if commit_diff:
   console.print_json(commit_diff)
  else:
   console.print(f"[red]Error:[/red] Commit {commit} not found for version {version}")
@click.group(name="pod",help="Manage state of local cloud pods")
def pod():
 from localstack_ext.bootstrap.licensing import is_logged_in
 if not is_logged_in():
  console.print("[red]Error:[/red] not logged in, please log in first")
  sys.exit(1)
@pod.command(name="list",help="Get a list of available local cloud pods")
def cmd_pod_list():
 status=console.status("Fetching list of pods from server ...")
 status.start()
 from localstack import config
 from localstack.utils.common import format_bytes
 from localstack_ext.bootstrap import pods_client
 try:
  result=pods_client.list_pods(NIlnk)
  status.stop()
  columns={"pod_name":"Name","backend":"Backend","url":"URL","size":"Size","state":"State"}
  print_table(columns,result,formatters={"size":format_bytes})
 except NIlnT as e:
  status.stop()
  if config.DEBUG:
   console.print_exception()
  else:
   console.print("[red]Error:[/red]",e)
@pod.command(name="create",help="Create a new local cloud pod")
def cmd_pod_create():
 msg="Please head over to https://app.localstack.cloud to create a new cloud pod. (CLI support is coming soon)"
 console.print(msg)
@pod.command(name="push",help="Push the state of the LocalStack instance to a cloud pod")
@click.argument("name")
def cmd_pod_push(name:NIlna):
 from localstack_ext.bootstrap import pods_client
 pods_client.push_state(name)
@pod.command(name="pull",help="Pull the state of a cloud pod into the running LocalStack instance")
@click.argument("name")
def cmd_pod_pull(name:NIlna):
 from localstack_ext.bootstrap import pods_client
 pods_client.pull_state(name)
@pod.command(name="reset",help="Reset the local state to get a fresh LocalStack instance")
def cmd_pod_reset():
 from localstack_ext.bootstrap import pods_client
 pods_client.reset_local_state()
def print_table(columns:Dict[NIlna,NIlna],rows:List[Dict[NIlna,Any]],formatters:Dict[NIlna,Callable[[Any],NIlna]]=NIlnk):
 from rich.table import Table
 if formatters is NIlnk:
  formatters=NIlnU()
 t=Table()
 for k,name in columns.items():
  t.add_column(name)
 for row in rows:
  cells=NIlnd()
  for c in columns.keys():
   cell=row.get(c)
   if c in formatters:
    cell=formatters[c](cell)
   if cell is NIlnk:
    cell=""
   if not NIlnO(cell,NIlna):
    cell=NIlna(cell)
   cells.append(cell)
  t.add_row(*cells)
 console.print(t)
class ConsoleLogger(logging.Logger):
 def __init__(self,name):
  NIlnJ(ConsoleLogger,self).__init__(name)
 def info(self,msg:Any,*args:Any,**kwargs:Any)->NIlnk:
  console.print(msg%args)
 def warning(self,msg:Any,*args:Any,**kwargs:Any)->NIlnk:
  console.print("[red]Warning:[/red] ",msg%args)
 def error(self,msg:Any,*args:Any,**kwargs:Any)->NIlnk:
  console.print("[red]Error:[/red] ",msg%args)
 def exception(self,msg:Any,*args:Any,**kwargs:Any)->NIlnk:
  console.print("[red]Error:[/red] ",msg%args)
  console.print_exception()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
