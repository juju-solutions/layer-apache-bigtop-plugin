## Overview

This charm is intended to serve as a platform for Hadoop client software.
That is, software such as Apache Hive, or Apache Pig, which need to interact
with Hadoop as a client, but are not otherwise concerned with the details of
the particular distribution or deployment.  This charm is intended to make it
easy to create charms for that client software, by managing the Hadoop
libraries and connections.


## Usage: Creating Workload Charms

To create a charm which communicates with Hadoop, you only need to implement
a single relation interface: `hadoop-plugin`.  Your `metadata.yaml` should
contain:

    provides:
      hadoop-plugin:
        interface: hadoop-plugin

This is a subordinate relation which deploys this charm alongside the
workload charm.  The benefit of using this subordinate interface is that your
charm only needs to handle the single relation, it does not need to install or
manage the Apache Hadoop libraries, and it is decoupled from the distribution,
enabling easy swapping of the plugin from one distribution (in this case,
Apache Bigtop Hadoop) with another.

Additionally, the `JAVA_HOME`, `HADOOP_HOME`, `HADOOP_CONF_DIR`, and other
environment variables will be set via `/etc/environment`.  This includes putting
the Hadoop bin and sbin directories on the `PATH`.  There are
[helpers](https://git.launchpad.net/bigdata-data/tree/common/noarch)
in `charmhelpers.contrib.bigdata.utils` to assist with using the environment
file. For example, to run the `hdfs` command to create a directory as the
`ubuntu` user:

    from charmhelpers.contrib.bigdata.utils import run_as
    run_as('ubuntu', 'hdfs', 'dfs', '-mkdir', '-p', '/home/ubuntu/foo')


## Provided Relations

  *There are no relations provided*

## Required Relations

### hadoop-plugin (interface: hadoop-plugin)

This relation connects this charm as a subordinate to the workload charm, as
described above.  The relation exchanges the following keys:

* Sent to the workload charm:

  * `set_hdfs_ready(namenodes, port)`: indicating that HDFS is ready to store data
  * `set_yarn_ready(hosts, port, hs_http_port, hs_ipc_port)`: indicating that YARN is ready

* Received from the workload charm:

  * There are no keys received from the workload charm*


## Manual Deployment

[apache bigtop bundles](https://jujucharms.com/u/bigdata-charmers/#bundles).
For example:

    juju quickstart bigtop-processing-mapreduce

However, to manually deploy the base Apache Bigtop Hadoop platform without using one
of the bundles, you can do the following:

    juju deploy apache-bigtop-namenode namenode
    juju deploy apache-bigtop-datanode datanode
    juju deploy apache-bigtop-resourcemanager resourcemgr
    juju deploy apache-bigtop-plugin plugin

    juju add-relation namenode datanode
    juju add-relation namenode resourcemgr
    juju add-relation namenode plugin
    juju add-relation resourcemgr plugin
