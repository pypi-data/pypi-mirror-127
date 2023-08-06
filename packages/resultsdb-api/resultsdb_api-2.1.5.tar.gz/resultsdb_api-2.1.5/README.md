# ResultsDB library

The ResultsDB API module provides a Python API for using ResultsDB's JSON/REST interface in a more pythonic way. It has functions which match the JSON/REST methods, but allow the common goodies as named parameters, and parameters skipping.

# Building ResultsDB API

You can use provided Makefile in order to build ResultsDB API. By default, it'll use buildroot equal to your current OS. You can override this behaviour by sepcifiyng variables for Make manually.

To build ResultsDB API:
`make mockbuild`

To build ResultsDB API for Fedora 27:
`make BUILDTARGET=fedora-27-x86_64 TARGETDIST=fc27 mocksrpm`

To build ResultsDB API for CentOS 7:
`make BUILDTARGET=epel-7-x86_64 TARGETDIST=el7 mocksrpm`

# License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

# Repositories

* ResultsDB - [GIT repo](https://pagure.io/taskotron/resultsdb)
* ResultsDB Frontend - [GIT repo](https://pagure.io/taskotron/resultsdb_frontend)
