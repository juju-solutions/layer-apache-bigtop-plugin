# pylint: disable=unused-argument
import subprocess
from charms.reactive import when, when_not, set_state, remove_state
from charmhelpers.core import hookenv


def get_hadoop_version():
    hadoop_out = subprocess.check_output(['hadoop', 'version']).decode()
    version = hadoop_out.split('\n')[0].split()[1]
    return version


@when('components.installed')
@when('hadoop-plugin.joined', 'namenode.joined', 'resourcemanager.joined')
def set_installed(client, hdfs, yarn):
    if hdfs.namenodes() and yarn.resourcemanagers():
        version = get_hadoop_version()
        client.set_installed(version)
        client.set_hdfs_ready(hdfs.namenodes(), hdfs.port())
        client.set_yarn_ready(
            yarn.resourcemanagers(), yarn.port(),
            yarn.hs_http(), yarn.hs_ipc())
        set_state('hadoop.installed')
        hookenv.status_set('active', 'ready')
    else:
        hookenv.status_set('waiting',
                           'waiting for namenode and resource manager to become ready')


@when('hadoop-plugin.joined')
@when_not('component.installed')
def clear_hadoop_ready(client):
    client.clear_hdfs_ready()
    client.clear_yarn_ready()
    remove_state('hadoop.installed')
