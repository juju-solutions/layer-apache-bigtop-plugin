## Overview

The Apache Hadoop software library is a framework that allows for the
distributed processing of large data sets across clusters of computers
using a simple programming model.

This charm plugs in to a workload charm to provide the
Apache Bigtop Gateway that includes all the Bigtop clients.

## Usage

This charm is intended to be deployed via one of the
[apache bundles](https://jujucharms.com/u/bigdata-charmers/#bundles).
For example:

    juju quickstart bigtop-processing-mapreduce

This will deploy the Apache Bigtop Hadoop platform with a workload node
which is running Apache Bigtop Gateway.

If you wanted to also wanted to be able to analyze your data using Apache Pig,
you could deploy it and attach it to the same plugin:

    juju deploy apache-pig pig
    juju add-relation plugin pig


## Contact Information

- <bigdata@lists.ubuntu.com>


## Hadoop

- [Apache Hadoop](http://hadoop.apache.org/) home page
- [Apache Hadoop bug trackers](http://hadoop.apache.org/issue_tracking.html)
- [Apache Hadoop mailing lists](http://hadoop.apache.org/mailing_lists.html)
- [Apache Hadoop Juju Charm](http://jujucharms.com/?text=hadoop)
