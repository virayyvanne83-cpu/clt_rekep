## ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation

#### [[Project Page]](https://rekep-robot.github.io/) [[Paper]](https://rekep-robot.github.io/rekep.pdf) [[Video]](https://youtu.be/2S8YhBdLdww)

[Wenlong Huang](https://wenlong.page)<sup>1</sup>, [Chen Wang](https://www.chenwangjeremy.net/)<sup>1*</sup>, [Yunzhu Li](https://yunzhuli.github.io/)<sup>2*</sup>, [Ruohan Zhang](https://ai.stanford.edu/~zharu/)<sup>1</sup>, [Li Fei-Fei](https://profiles.stanford.edu/fei-fei-li)<sup>1</sup> (\* indicates equal contributions)

<sup>1</sup>Stanford University, <sup>3</sup>Columbia University

<img  src="media/pen-in-holder-disturbances.gif" width="550">

This is the official demo code for [ReKep](https://rekep-robot.github.io/) implemented in [OmniGibson](https://behavior.stanford.edu/omnigibson/index.html). ReKep is a method that uses large vision models and vision-language models in a hierarchical optimization framework to generate closed-loop trajectories for manipulation tasks.


## Setup Instructions

Note that this codebase is best run with a display. For running in headless mode, refer to the [instructions in OmniGibson](https://behavior.stanford.edu/omnigibson/getting_started/installation.html).

- Install [OmniGibson](https://behavior.stanford.edu/omnigibson/getting_started/installation.html). This code is tested on [this commit](https://github.com/StanfordVL/OmniGibson/tree/cc0316a0574018a3cb2956fcbff3be75c07cdf0f).

NOTE: If you encounter the warning `We did not find Isaac Sim under ~/.local/share/ov/pkg.` when running `./scripts/setup.sh` for OmniGibson, first ensure that you have installed Isaac Sim. Assuming Isaac Sim is installed in the default directory, then provide the following path `/home/[USERNAME]/.local/share/ov/pkg/isaac-sim-2023.1.1` (replace `[USERNAME]` with your username).

- Install ReKep in the same conda environment:
```Shell
conda activate omnigibson
cd ..
git clone https://github.com/huangwl18/ReKep.git
cd ReKep
pip install -r requirements.txt
```

- Obtain an [OpenAI API](https://openai.com/blog/openai-api) key and set it up as an environment variable:
```Shell
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

##这篇是对于3个新增self_learnx文件夹的说明
###self_learn1_xxx
这个是对与仿真环境的熟悉与初步使用，包括加载不同机器人、控制机器人简单运动、以及仿真环境如何使用采样法获取物体大概坐标
###self_learn2_xxx
这个是如何获取图像上视觉和空间关键点
分为获取相机画面、对画面进行预处理（修改尺寸、不同物体的前景图、等）、以及最后的处理图像并标记关键点
###self_learn3_xxx
这个是把上一部标记的关键点注册到具体的mesh结构上，然后接下来的就是把这些都给gpt4o大模型并让它生成约束函数，然后让main.py调用这些约束代价。


