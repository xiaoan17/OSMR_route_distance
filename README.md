欢迎大家访问本项目。

基于下面两个项目，本项目实现了调用OSMR项目提供的HTTP访问接口，批量的计算节点之间开车距离，并最终得到一个表示节点邻接关系的矩阵。

本项目是复现工作[LargeST: A Benchmark Dataset for Large-Scale Traffic Forecasting (NeurIPS 2023 DB Track)]的过程中，开展的部分工作，Largest项目的地址为：https://github.com/liuxu77/LargeST。

其中，该项目主要涉及计算检测器节点之间的驾驶距离，这部分工作主要参考一项名为OSMR（Open Source Routing Machine - C++ backend）的研究，这是一项非常有趣的研究，该项目的地址为：https://github.com/Project-OSRM/osrm-backend。

需要提醒的是，本项目的代码和数据分别归类到了两个文件夹（coda、data），进行复现或者调用的时候，**需要修改相关的文件路径**。

本代码的更新时间为2024年6月12日。
Anbc
