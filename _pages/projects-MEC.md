---
layout: archive
title: "Mobile Edge Computing Experiment Platform"
permalink: /projects-MEC/
author_profile: true
redirect_from:
  - /projects/projects-MEC
---

The experiment platform consists of four parts: mobile device, base station, edge server and cloud server.

1. Mobile Device: A Huawei honor 8 smart phone is used as the mobile device. This smart phone is equipped with 4 Coretex A72 2.3GHz and 4 Cortex A53 1.8GHz, and Android 7.0. It also has a 32 GB internal storage and 4GB RAM. We implement an APP, ``ImagCat'', to capture images and send them to edge and cloud servers.

2. Base Station: The base station is based on Open Air Interface, and the hardware of the base station consists of three components: radio-frequency signal generator, base station server A and base station server B, respectively. The radio-frequency signal generator is equipped with USRP-B210. The base station server A is equipped with Intel i7-6700@3.4GHz CPU and 16GB RAM running Ubuntu 14.04.3 and used to run eNodeB. The radio-frequency signal generator and the base station A are connected through USB 3.0. The base station server B is equipped with Intel i5-6500@3.2GHz CPU and 4GB RAM running Ubuntu 14.04.3 and used to run HSS+MME+SGW+PGW. The base station server A and base station server B are connected through LAN. The base station works on Band7 (uplink 2500MHz-2570MHz, downlink 2620MHz-2690MHz).

3. Edge Server: The edge server is a computer equipped with Intel i5-4590@3.3GHz CPU and 12GB RAM. Operations with image preprocessing run on the edge server by using Java to invoke the OpenCV libraries. The mobile device and edge server are connected through LTE base station with upload link speed 1000KB/s and the downlink speed 1.36MB/s.

4. Cloud Server: The cloud server is Ali Cloud, which is equipped with 4 quad-core 2.5 GHz Intel Xeon E5-2682 v4 and 16GB RAM running Ubuntu 14.04.3 and implements the GLSP algorithm and image matching by Matlab. The edge server and cloud server are connected through Internet backbone.

> [Demo Video Download](../images/MEC-experiment-platform.mp4)
