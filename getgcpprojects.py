import subprocess
import sys
import logging
import threading
import pprint

logger = logging.Logger('catch_all')


def execute_cmd(parameters):
    try:
        return subprocess.check_output(parameters, shell=True)
    except Exception as e:
        logger.error(e)
        logger.error('ERROR: Looking in console for more information')


def getProjectList():
    list_projects = execute_cmd(['gcloud', 'projects', 'list', '--format=value(projectId)']).decode("utf-8").split('\n')
    # for project in list_projects :
    # print (project)
    return list_projects


def getK8SClusterList(project):
    # gcloud container clusters list --project nth-bucksaw-328005
    print ("Setting Project context to ", project)
    output = execute_cmd(['gcloud', 'config', 'set', 'project', project]).decode(
        "utf-8").split(
        '\n')
    list_k8s = execute_cmd(
        ["gcloud", "container", "clusters", "list", '--format=value(name)']).decode(
        "utf-8").split(
        '\n')
    # for project in list_projects :
    # print (project)
    return list_k8s

def connectK8S(cluster,project):
    # gcloud container clusters list --project nth-bucksaw-328005
    print ("connecting Project context to ", project)
    k8sconnect = "gcloud container clusters get-credentials " + cluster + " --project " + project
    execute_cmd(k8sconnect)

