#**Secure serverless function**

The pipeline we have implemented provides an initial layer of security at the design stage of serverless functions. This process automates the creation of Docker images, which are then used by a serverless function manager for deployment.
At this stage, a security check is performed to detect potential vulnerabilities in the source code of the functions, particularly those developed in Python.
