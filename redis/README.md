# ZeroMQ Tests

Important note! Since all the pub/sub systems we're looking at (RabbitMQ, ZeroMQ, ROS 1/2) are built on either UDP or TCP, they should be subject to similar hard limits in terms of resource scaling and network peformance. This ZeroMQ test is meant to be more of a quick test to probe of what
some of those hard limits may be since it's easier to write than bare sockets and potentially something still useful.
