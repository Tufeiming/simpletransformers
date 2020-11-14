# simpletransformers阅读理解
fork自[simpletransformers](https://github.com/ThilinaRajapakse/simpletransformers)，并删除了与阅读理解无关的文件。
## 运行
运行example/question_answering/my_predict.py即可实现对单条数据的预测，输入为一篇文本，输出为事先设定好的9个问题对应的答案。
### 说明
先运行transformers的run_squad.py，训练完后保存bert模型至example/model目录。应该含有以下三个文件：
- config.json
- pytorch_model.bin
- vocab.txt
### 环境
以下为使用实验室电脑（无GPU）运行的操作记录：
1. 创建conda虚拟环境，名为st。

   ```bash
   conda create -n st python pandas tqdm
   ```

2. 激活刚刚创建的环境。

   ```bash
   conda activate st
   ```

3. 安装pytorch（cpu only）。

   ```bash
   conda install pytorch cpuonly -c pytorch
   ```

4. 安装simpletransformers。

   ```bash
   pip install simpletransformers
   ```