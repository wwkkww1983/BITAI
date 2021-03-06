## Swarm Intelligence

#### 1. Outline

1. SI (Swarm Intelligence)
2. Communication
3. Algorithm for Search
4. Quantum Computing

#### 2. SI

* 群体是由简单的个体组成的，但是群体可以表现出高度的智能

  自底向上行为：简单规则遵循简单规则生成复杂的结构/行为

* 群体的自组织和解决方案对问题的解决提供了智能的解决方案

* 群体智能的行为模型解释`Boid`

  1. 分离原则
     * 避免拥挤
     * 包括避免和环境中的其他的实体发生冲突
     * 该准则的优先级比其他准则的优先级高
  2. 定位(调整方向)
     * 转向群体的平均的移动方向
     * 加强和群体移动的一致性
  3. 内聚
     * 引导个体移动到平均位置
     * 保证空间位置的一致性

* 什么是群体智能

  1. 群体智能（SI）是一种基于分散自组织系统中群体行为研究的人工智能技术
  2. SI系统通常由一组简单的个体组成，它们之间相互作用，并与环境相互作用
  3. 组成
     * 个体
     * 行为
     * 个体的通信(重要)
  4. 特点
     * 分布式，没有统一的领导者
     * 受限通信

* 通信的重要性

  * 交互性

  * 方式

    * 间接沟通

      1. 利用周围的介质传播信息

         环境可以是一个巨大的交换知识，存储知识和数据的公共区域

      2. 注意信息的耗散度(挥发性)

    * 直接沟通

#### 3. Algorithm for Search 

##### 1. ACO蚁群算法

1. 算法思想

   * 蚂蚁在移动的时候会在沿途分泌一些浓度的信息素
   * 蚂蚁选择路径是存在**概率的**
   * 信息素存在挥发机制
   * 这个过程是一个正反馈循环系统，因为在路径上信息素的强度越高
   * 最终的路径会收敛到一个足够优秀的路径上，这个路径上的信息素的浓度足够高，并且蚂蚁会尽可能在更大的概率上选择这样的道路去行进

2. 伪代码

   ![ACO](/home/lantian/File/AI/photo/ACO.png)

3. ACO对TSP算法的示例
   $$
   p_{ij}^k(t) = \left\{
   \begin{array}{rcl}
   \frac{(\tau_{ij}(t))^{\alpha}(\eta_{ij}(t))^{\beta}}{\sum (\tau_{ij}(t))^{\alpha}(\eta_{ij}(t))^{\beta}} \\
   0
   \end{array}\right.
   $$

   * $$\tau_{ij}(t)$$ : 代表的是第$$t$$次迭代的时候 $$i\rightarrow j$$ 路劲上的信息素的质量
   * $$\eta_{ij}(t)$$ : 代表的是第$$t$$次迭代的时候 $$i \rightarrow j$$ 路径的启发式距离
   * $$p_{ij}^k(t)$$ : 代表第$$k$$个蚂蚁在 $$i$$ 出边路径上选择的 $$j$$ 作为下一个要访问的节点的概率

   $$
   \tau_{ij}(t+1)=(1-\rho)\times \tau_{ij}(t)+\Delta\tau_{ij}(t)
   $$

   * $$\rho$$ : 代表信息素的挥发系数
   * 上式代表 $$i\rightarrow j$$ 路径上的信息素的浓度随着迭代次数的变化

   $$
   \Delta\tau_{ij}(t)=\sum_{k=1}^m\Delta\tau_{ij}^k(t) 
   $$

   * $$i \rightarrow j $$ 路径上的信息素的变化量是对所有的蚂蚁的在该路径上的信息素的求和

   $$
   \Delta\tau_{ij}^k(t) = \frac{Q}{L^k}
   $$

   * $$Q$$ : 是信息素的浓度质量系数，设定的常数
   * $$L^k$$ : 是第$$k$$只蚂蚁(解)的路径的长度

4. 蚁群算法的变体

   蚁群算法收敛快速，但是结果不一定很好，需要调整蚁群算法的一些机制加以优化

   * MMAS(MAX-MIN Ant system) : 当前的解如果很好的但是加上一些**限制**，目的是为了避免我们快速的将结果收敛到这个解上，保证其他的接的情况得到充分的考虑
   * EAS : 
     * 精英蚁群系统
     * ![EAS](/home/lantian/File/AI/photo/EAS.png)
     * 只将全局最优的蚂蚁的信息素撒播到路径上
   * AKrank
     * 解的排序蚁群系统
     * ![ACORank](/home/lantian/File/AI/photo/ACORank.png)
     * 按照解的优劣进行排序

##### 2. PSO粒子群算法

1. 要点

   * $$pbest$$ : 个体历史最优解
   * $$gbest$$ : 群体历史最优解
   * $$lbest$$ : 局部群体历史最优解(局部可以按照解空间进行划分)
   * $$vol$$ : 每一个个体都存在一个速度(每一个个体不相同)
   * $$dir$$ : 每一个个体都存在下一步移动的方向，这个方向会受到$$pbest$$, $$gbest$$, $$lbest$$ 的影响

2. 算法步骤

   * 初始化种群
   * 评估每个粒子(解)的适应度(优劣)
   * 修正速度和方向，执行位置的变化，每个粒子搜索下一个解
   * 迭代直到满足终止条件

3. 优点

   * 容易实现
   * 计算效率高
   * 适合各种问题

4. 与神经网络的结合

   ![PSONN](/home/lantian/File/AI/photo/PSONN.png)

   * 神经网络的权重调整的经典算法是BP,我们都知道这一点，但是这个经典的算法是建立在我们存在一个精准的误差估计函数上的

   * 但是我们需要认识到，优秀问题很难得到一个误差精准函数(比如上面这个问题，我们对于图片的自动标注的好坏结果没有办法量化分析,可能很接近也可能错的很离谱)，这时候我们没有办法执行反向传播算法

   * 但是我们可以使用群体智能算法(PSO)来对神经网络的权值矩阵进行优化

     * 个体是每一个初始的神经网络(随机初始化权重)

     * 执行上图的流程，不断的将结果逼近一个优秀的最优的权重

     * **这里使用群体智能算法来进行神经网络参数矩阵的调整**

       ？？？？？？个体的适应度函数的实现？？？？？？

       ？？？？？？和之前的遗传算法调整神经网络的思想一致？？？？？？

#### 4. 量子计算 (Shor算法)

