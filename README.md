## Overview

The Apache Hadoop software library is a framework that allows for the
distributed processing of large data sets across clusters of computers
using a simple programming model.

This charm facilitates communication between core Apache Bigtop cluster
components and workload charms.


## Usage

This charm is intended to be deployed via one of the
[apache bigtop bundles](https://jujucharms.com/u/bigdata-dev/#bundles).
For example:

    juju quickstart bigtop-processing-mapreduce

This will deploy the Apache Bigtop platform with a workload node
preconfigured to work with the cluster.

You could extend this deployment, for example, to analyze data using Apache Pig.
Simply deploy Pig and attach it to the same plugin:

    juju deploy apache-pig pig
    juju add-relation plugin pig


## Status and Smoke Test

Apache Bigtop charms provide extended status reporting to indicate when they
are ready:

    juju status --format=tabular

This is particularly useful when combined with `watch` to track the on-going
progress of the deployment:

    watch -n 0.5 juju status --format=tabular

The message for each unit will provide information about that unit's state.
Once they all indicate that they are ready, you can perform a "smoke test"
to verify HDFS or YARN services are working as expected. Trigger the
`smoke-test` action by:

    juju action do namenode/0 smoke-test
    juju action do resourcemanager/0 smoke-test

After a few seconds or so, you can check the results of the smoke test:

    juju action status

You will see `status: completed` if the smoke test was successful, or
`status: failed` if it was not.  You can get more information on why it failed
via:

    juju action fetch <action-id>


## Contact Information

- <bigdata@lists.ubuntu.com>


## Resources

- [Apache Bigtop](http://bigtop.apache.org/) home page
- [Apache Bigtop issue tracking](http://bigtop.apache.org/issue-tracking.html)
- [Apache Bigtop mailing lists](http://bigtop.apache.org/mail-lists.html)
- [Apache Bigtop charms](https://jujucharms.com/q/apache/bigtop)
