# ZZU 大学物理实验数据处理脚本
### 写在前面
这些脚本均为自用工具，在[HITSZ仓库](https://github.com/HITSZ-OpenAuto/PHYS1002) 的开源理念启发下，决定开源部分实验数据处理代码，助力实验数据处理计算。

大部分变量命名不够规范，欢迎提交PR

鉴于个人水平有限，部分脚本的计算逻辑或表述可能存在不足，非常欢迎大家提出宝贵意见，共同提升代码可用性！

### 关于数据
禁止使用仓库内代码中的实验数据，抄袭数据是严重的**违规行为**

在子文件夹内的README会详细说明各个numpy数组应当输入哪些数据

### 使用方法
1. 克隆仓库
```
git clone https://github.com/NestorRay/ZZU-Physics-Data-Tools.git
cd ./ZZU-Physics-Data-Tools
```
> **推荐使用更为现代化的uv管理依赖和虚拟环境**

2. uv创建虚拟环境
```
uv venv
```

3. 安装依赖
```
uv pip install -r requirement.txt
```

4. 进入对应的文件夹
```
cd ./Exp01
```
5. 参照文件夹内README修改数据

6. 运行脚本
```
 uv run Exp01.py
```
|文件夹|实验名称|
|:-----:|:-----:|
|Exp01|[分光计的调节和使用](https://github.com/NestorRay/pygraph/tree/main/Exp01)|
|Exp02|[钢丝杨氏模量测量](https://github.com/NestorRay/pygraph/tree/main/Exp02)|
