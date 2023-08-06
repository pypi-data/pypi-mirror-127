<p align="center">
    <a href="https://github.com/zjunlp/deepke"> <img src="pics/logo.png" width="400"/></a>
<p>
<p align="center">  
    <a href="https://deepke.openkg.cn">
        <img alt="Documentation" src="https://img.shields.io/badge/DeepKE-website-green">
    </a>
    <a href="https://pypi.org/project/deepke/#files">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/deepke">
    </a>
    <a href="https://github.com/zjunlp/DeepKE/blob/master/LICENSE">
        <img alt="GitHub" src="https://img.shields.io/github/license/zjunlp/deepke">
    </a>
</p>
<p align="center">
    <b>简体中文 | <a href="https://github.com/zjunlp/DeepKE/blob/main/README_ENGLISH.md">English</a></b>
</p>

<h1 align="center">
    <p>基于深度学习的开源中文知识图谱抽取框架</p>
</h1>

DeepKE 是一个支持<b>低资源、长篇章</b>的知识抽取工具，可以基于<b>PyTorch</b>实现<b>命名实体识别</b>、<b>关系抽取</b>和<b>属性抽取</b>功能。

<br>

## 在线演示

在线演示 [demo](https://deepke.openkg.cn)

### 进行预测
下面使用一个demo展示预测过程<br>
<img src="pics/demo.gif" width="636" height="494" align=center>

<br>

## 模型架构

Deepke的架构图如下所示

<h3 align="center">
    <img src="pics/architectures.png">
</h3>

DeepKE包括了三个模块，可以进行命名实体识别、关系抽取以及属性抽取任务，在各个模块下包括各自的子模块。其中关系抽取模块就有常规模块、文档级抽取模块以及低资源少样本模块。在每一个子模块中，包含实现分词、预处理等功能的一个工具集合，以及编码、训练和预测部分。

<br>

## 快速上手

DeepKE支持pip安装使用，以常规全监督设定关系抽取为例，经过以下五个步骤就可以实现一个常规关系抽取模型

**Step 1** 下载代码 ```git clone https://github.com/zjunlp/DeepKE.git```（别忘记star和fork哈！！！）

**Step 2** 使用anaconda创建虚拟环境，进入虚拟环境 

```
conda create -n deepke python=3.8

conda activate deepke
```
1） 基于pip安装，直接使用

```
pip install deepke
```

2） 基于源码安装

```
python setup.py install

python setup.py develop
```

**Step 3**  进入任务文件夹，以常规关系抽取为例

```
cd DeepKE/example/re/standard
```

**Step 4**  模型训练，训练用到的参数可在conf文件夹内修改

```
python run.py
```

**Step 5**  模型预测。预测用到的参数可在conf文件夹内修改

```
python predict.py
```

### 环境依赖

> python == 3.8

- torch == 1.5
- hydra-core == 1.0.6
- tensorboard == 2.4.1
- matplotlib == 3.4.1
- transformers == 3.4.0
- jieba == 0.42.1
- scikit-learn == 0.24.1
- pytorch-transformers == 1.2.0
- seqeval == 1.2.2
- tqdm == 4.60.0
- opt-einsum==3.3.0
- ujson

### 具体功能介绍

#### 1. 命名实体识别NER

- 命名实体识别是从非结构化的文本中识别出实体和其类型。数据为txt文件，样式范例为：

  |                           Sentence                           |           Person           |    Location    |          Organization          |
  | :----------------------------------------------------------: | :------------------------: | :------------: | :----------------------------: |
  | 本报北京9月4日讯记者杨涌报道：部分省区人民日报宣传发行工作座谈会9月3日在4日在京举行。 |            杨涌            |      北京      |            人民日报            |
  | 《红楼梦》是中央电视台和中国电视剧制作中心根据中国古典文学名著《红楼梦》摄制于1987年的一部古装连续剧，由王扶林导演，周汝昌、王蒙、周岭等多位红学家参与制作。 | 王扶林，周汝昌，王蒙，周岭 |      中国      | 中央电视台，中国电视剧制作中心 |
  | 秦始皇兵马俑位于陕西省西安市，1961年被国务院公布为第一批全国重点文物保护单位，是世界八大奇迹之一。 |           秦始皇           | 陕西省，西安市 |             国务院             |

- 具体流程请进入详细的README中
  - **[常规全监督STANDARD](https://github.com/zjunlp/deepke/blob/main/example/ner/standard)** 
  
     **Step1**: 进入`DeepKE/example/ner/standard`，数据集和参数配置可以分别在`data`和`conf`文件夹中修改；<br>
     
     **Step2**: 模型训练
     
     ```
     python run.py
     ```
     
     **Step3**: 模型预测
     ```
     python predict.py
     ```
     
  - **[少样本FEW-SHOT](https://github.com/zjunlp/DeepKE/tree/main/example/ner/few-shot)** 
  
    **Step1**: 进入`DeepKE/example/ner/few-shot`，模型加载和保存位置以及参数配置可以在`conf`文件夹中修改；<br>
    
    **Step2**：模型训练，默认使用`CoNLL-2003`数据集进行训练
    
     ```
     python run.py +train=few_shot
     ```
    
    若要加载模型，修改`few_shot.yaml`中的`load_path`；<br>
    
    **Step3**：在`config.yaml`中追加`- predict`，`predict.yaml`中修改`load_path`为模型路径以及`write_path`为预测结果的保存路径，完成修改后使用
    
    ```
    python predict.py
    ```

#### 2. 关系抽取RE

- 关系抽取是从非结构化的文本中抽取出实体之间的关系，以下为几个样式范例，数据为csv文件：

  |                        Sentence                        | Relation |    Head    | Head_offset |    Tail    | Tail_offset |
  | :----------------------------------------------------: | :------: | :--------: | :---------: | :--------: | :---------: |
  | 《岳父也是爹》是王军执导的电视剧，由马恩然、范明主演。 |   导演   | 岳父也是爹 |      1      |    王军    |      8      |
  |  《九玄珠》是在纵横中文网连载的一部小说，作者是龙马。  | 连载网站 |   九玄珠   |      1      | 纵横中文网 |      7      |
  |     提起杭州的美景，西湖总是第一个映入脑海的词语。     | 所在城市 |    西湖    |      8      |    杭州    |      2      |

- 具体流程请进入详细的README中，RE包括了以下三个子功能
  - **[常规全监督STANDARD](https://github.com/zjunlp/deepke/blob/main/example/re/standard)**  

    **Step1**：进入`DeepKE/example/re/standard`，数据集和参数配置可以分别进入`data`和`conf`文件夹中修改；<br>
    
    **Step2**：模型训练

    ```
    python run.py
    ```
    
    **Step3**：模型预测

    ```
    python predict.py
    ```
  
  - **[少样本FEW-SHOT](https://github.com/zjunlp/deepke/blob/main/example/re/few-shot)**
  
    **Step1**：进入`DeepKE/example/re/few-shot`，数据集和参数配置可以分别进入`data`和`conf`文件夹中修改；<br>
  
    **Step2**：模型训练，如需从上次训练的模型开始训练：设置`conf/train.yaml`中的`train_from_saved_model`为上次保存模型的路径，每次训练的日志默认保存在根目录，可用`log_dir`来配置；<br>
    
    ```
    python run.py
    ```
    
    **Step3**：模型预测

    ```
    python predict.py
    ```

  - **[文档级DOCUMENT](https://github.com/zjunlp/deepke/blob/main/example/re/document)** <br>
    ```train_distant.json```由于文件太大，请自行从Google Drive上下载到data/目录下；<br>
    
    **Step1**：进入`DeepKE/example/re/document`，数据集和参数配置可以分别进入`data`和`conf`文件夹中修改；<br>
  
    **Step2**：模型训练，如需从上次训练的模型开始训练：设置`conf/train.yaml`中的`train_from_saved_model`为上次保存模型的路径，每次训练的日志默认保存在根目录，可用`log_dir`来配置；
  
    ```
    python run.py
    ```
    **Step3**：模型预测
    
    ```
    python predict.py
    ```

#### 3. 属性抽取AE

- 数据为csv文件，样式范例为：

  |                           Sentence                           |   Att    |   Ent    | Ent_offset |      Val      | Val_offset |
  | :----------------------------------------------------------: | :------: | :------: | :--------: | :-----------: | :--------: |
  |          张冬梅，女，汉族，1968年2月生，河南淇县人           |   民族   |  张冬梅  |     0      |     汉族      |     6      |
  | 杨缨，字绵公，号钓溪，松溪县人，祖籍将乐，是北宋理学家杨时的七世孙 |   朝代   |   杨缨   |     0      |     北宋      |     22     |
  |        2014年10月1日许鞍华执导的电影《黄金时代》上映         | 上映时间 | 黄金时代 |     19     | 2014年10月1日 |     0      |

- 具体流程请进入详细的README中
  - **[常规全监督STANDARD](https://github.com/zjunlp/deepke/blob/main/example/ae/standard)**  
    
    **Step1**：进入`DeepKE/example/re/standard`，数据集和参数配置可以分别进入`data`和`conf`文件夹中修改；<br>
    
    **Step2**：模型训练

    ```
    python run.py
    ```
    
    **Step3**：模型预测

    ```
    python predict.py
    ```

### Notebook教程

本工具提供了若干Notebook和Google Colab教程，用户可针对性调试学习。

- 常规设定：

    [命名实体识别Notebook](https://github.com/zjunlp/DeepKE/blob/main/tutorial-notebooks/ner/standard/tutorial.ipynb)

    [命名实体识别Colab](https://colab.research.google.com/drive/1rFiIcDNgpC002q9BbtY_wkeBUvbqVxpg?usp=sharing)
    
    [关系抽取Notebook](https://github.com/zjunlp/DeepKE/blob/main/tutorial-notebooks/re/standard/tutorial.ipynb)

    [关系抽取Colab](https://colab.research.google.com/drive/1o6rKIxBqrGZNnA2IMXqiSsY2GWANAZLl?usp=sharing)
   
    [属性抽取Notebook](https://github.com/zjunlp/DeepKE/blob/main/tutorial-notebooks/ae/standard/tutorial.ipynb)

    [属性抽取Colab](https://colab.research.google.com/drive/1pgPouEtHMR7L9Z-QfG1sPYkJfrtRt8ML?usp=sharing)

- 低资源：

    [命名实体识别Notebook](https://github.com/zjunlp/DeepKE/blob/main/tutorial-notebooks/ner/few-shot/tutorial.ipynb)

    [命名实体识别Colab](https://colab.research.google.com/drive/1Xz0sNpYQNbkjhebCG5djrwM8Mj2Crj7F?usp=sharing)

    [关系抽取Notebook](https://github.com/zjunlp/DeepKE/blob/main/tutorial-notebooks/re/few-shot/tutorial.ipynb)
    
    [关系抽取Colab]()
    
- 篇章级：

    [关系抽取Notebook](https://github.com/zjunlp/DeepKE/blob/main/tutorial-notebooks/re/document/tutorial.ipynb)

    [关系抽取Colab]()


<!-- ![image](https://user-images.githubusercontent.com/31753427/140022588-c3b38495-89b1-4f3c-8298-bcc1086f78bf.png) -->

## 备注（常见问题）

1. 使用 Anaconda 时，建议添加国内镜像，下载速度更快。如[镜像](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)。
2. 使用 pip 时，建议使用国内镜像，下载速度更快，如阿里云镜像。
3. 安装后提示 `ModuleNotFoundError: No module named 'past'`，输入命令 `pip install future` 即可解决。
4. 使用语言预训练模型时，在线安装下载模型比较慢，更建议提前下载好，存放到 pretrained 文件夹内。具体存放文件要求见文件夹内的 `README.md`。
5. DeepKE老版本位于[deepke-v1.0](https://github.com/zjunlp/DeepKE/tree/deepke-v1.0)分支，用户可切换分支使用老版本，老版本的能力已全部迁移到标准设定关系抽取([example/re/standard](https://github.com/zjunlp/DeepKE/blob/main/example/re/standard/README.md))中。

<br>

## 项目成员

浙江大学：张宁豫、陶联宽、余海洋、陈想、徐欣、田玺、李磊、黎洲波、邓淑敏、姚云志、叶宏彬、谢辛、郑国轴、陈华钧

达摩院：谭传奇、陈漠沙、黄非

