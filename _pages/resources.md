---
layout: archive
title: "Resources"
permalink: /resources/
author_profile: true
redirect_from:
  - /resources
---

## 1. High-Performance Spaceborne Core Network based on eBPF Technology
The On-Board Data Processing capability of 5G NTN Regenerative Satellites generates massive data traffic, posing significant challenges to the forwarding efficiency of the 5G Core's User Plane Function (UPF). Traditional free5GC UPFs face performance bottlenecks when handling high-rate sessions, primarily because of frequent data copying and context switching within the kernel protocol stack. To solve this, we enhance free5GC by leveraging eBPF (Extended Berkeley Packet Filter) technology, implementing Kernel Bypass forwarding. This approach minimizes data copies and significantly reduces CPU overhead, thereby boosting data packet forwarding efficiency to meet the stringent throughput requirements of 5G NTN and On-Board Data Processing applications.

Related Repository Link: [https://github.com/BUPT-SKLoNST-CorenetGroup/Sat5GC.git](https://github.com/BUPT-SKLoNST-CorenetGroup/Sat5GC.git)

### 1.1 In-Orbit Verification

The Core Network systems deployed on BUPT-2 and BUPT-3 satellites are used for architecture validation and performance measurement.

Related repository links ：[https://github.com/BUPT-SKLoNST-CorenetGroup/modified-sat5gc-BUPT2And3.git](https://github.com/BUPT-SKLoNST-CorenetGroup/modified-sat5gc-BUPT2And3.git)

### 1.2 Distributed Service Registration and Discovery

A distributed service registration and discovery mechanism that utilizes an improved consistent hashing algorithm to rapidly store and discover service registration information, thereby enhancing the reliability and efficiency of the Core Network.

Related repository links ： [https://github.com/BUPT-SKLoNST-CorenetGroup/ServiceRegistry.git](https://github.com/BUPT-SKLoNST-CorenetGroup/ServiceRegistry.git)

Relevant Publication Links ：[https://www.computer.org/csdl/proceedings-article/satellite/2023/058800a043/1VYxzn3pDj2](https://www.computer.org/csdl/proceedings-article/satellite/2023/058800a043/1VYxzn3pDj2)

### 1.3 Fine-grained QoS

We have designed and implemented a fine-grained QoS control framework based on Service Tags and Cross-Layer Design. This framework utilizes Service Tags, determined through communication between the Core Network and the Application Service Provider (ASP), to subdivide QoS flows into several sub-flows. Subsequently, differentiated services are provisioned specifically for these sub-flows.

Related repository links ：[https://github.com/BUPT-SKLoNST-CorenetGroup/FGQos.git](https://github.com/BUPT-SKLoNST-CorenetGroup/FGQos.git)

### 1.4 User Plane Awareness

A Traffic Scheduling System designed for the 5G Core Network User Plane (UPF), which comprises a Network State Information Perception Subsystem and a Route Decision Subsystem.

The Network State Information Perception Subsystem achieves dynamic in-path network state measurement by inserting telemetry information into the GTP-U packet extension header to monitor UPF status information in real-time.

The Route Decision Subsystem implements a traffic scheduling algorithm based on an improved Ant Colony Optimization (ACO) algorithm, performing route decisions based on the real-time network state.

Related repository links ：[https://github.com/BUPT-SKLoNST-CorenetGroup/NetObserver.git](https://github.com/BUPT-SKLoNST-CorenetGroup/NetObserver.git)

Relevant Publication Links ：[https://qikan.cqvip.com/Qikan/Article/Detail?id=7110855341](https://qikan.cqvip.com/Qikan/Article/Detail?id=7110855341)


### 1.5 Intelligent Scheduling

This work focuses on decentralizing the 5G Core Network's centralized Network Data Analytics Function (NWDAF) and specifically targets the implementation of intelligent decision-making processes within the Core Network Control Plane. We propose a Distributed Network Data Analytics Function (NWDAF) based on the Raft consensus algorithm to support the intelligent decision tasks of the Core Network Control Plane.

Related repository links ：[https://github.com/BUPT-SKLoNST-CorenetGroup/Decision-Hub.git](https://github.com/BUPT-SKLoNST-CorenetGroup/Decision-Hub.git)

## Earlier
1. Prototype-system for detecting SIP flooding attacks [[Source Code]](../files/Detection%20Tool%20for%20SIP%20flooding%20attacks.rar)
2. Cloud model and MIP for Reliable Service Selection [[Source Code]](../files/Reliable%20Service%20Selection.zip)
3. Detecting SYN flooding attacks based on CUSUM [[Source Code]](../files/Detection.rar)
4. QoS measurement of Web services [[Source Code]](../files/QoS%20mesure%20of%20Web%20service.rar)
5. CXCS for mobile service adaptation [[Source Code]](../files/XCSNew_Coevolution.zip)
6. Energy-aware VM replacement optimization [[Source Code]](../files/Energy-aware%20VM%20replacement%20scheme.zip)
7. Predict unknown Web service QoS values [[Demo]](../files/QoS-prediction.wmv) [[YouTube]](http://youtu.be/DD7K0yrTPJ4)
8. Simulation Tool for Cloud Service Reliability [[Demo]](../files/FTCloudSim.wmv) [[YouTube]](http://youtu.be/yMyz2gesywA) [[China-YouKu]](http://v.youku.com/v_show/id_XNzA3NDY3OTUy.html)
9.  FTCloudSim source code casual version [[Source Code]](../files/FTCloudSim.zip). More detailed information is in "Zhou A, Wang S, Sun Q, Zou H, Yang F. [FTCloudSim: a simulation tool for cloud service reliability enhancement mechanisms](../files/FTCLOUDSIMdemo.pdf). Proceedings of ACM/IFIP/USENIX International Middleware Conference Demo & Poster Track, 2013." If FTCloudSim can help you, please cite it in your paper.
10. WebCloudSim is a cloud simulation system that supports fat-tree cloud data centers for reliability, QoS, energy, and network resource metrics. You can use it by [www.webcloudsim.org](http://www.webcloudsim.org)
11. [Dataset: Shanghai Telecom Dataset for Mobile Edge Computing](./telecom_dataset)