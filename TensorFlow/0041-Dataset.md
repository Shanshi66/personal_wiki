# Dataset

如果需要训练的数据大小不大，例如不到1G，那么可以直接全部读入内存中进行训练，这样一般效率最高。
数据量很大时，使用tf.data API 可以构建数据输入管道，轻松处理大量的数据，不同的数据格式，以及不同的数据转换。

可以从 
1. Numpy array
2. Pandas DataFrame
3. Python generator
4. csv文件
5. 文本文件
6. 文件路径
7. tfrecords文件，对样本构建tf.Example后压缩成字符串写到tfrecoreds文件，读取后再解析成tf.Example。tfrecoreds文件的优点是压缩后文件较小，便于网络传播，加载速度较快。

等方式构建数据管道。


## 从Numpy array构建数据管道

```python
iris = datasets.load_iris()
ds1 = tf.data.Dataset.from_tensor_slices((iris["data"],iris["target"]))
for features,label in ds1.take(5):
    print(features,label)
```

## 从Pandas DataFrame构建数据管道

```python
iris = datasets.load_iris()
dfiris = pd.DataFrame(iris["data"],columns = iris.feature_names)
ds2 = tf.data.Dataset.from_tensor_slices((dfiris.to_dict("list"),iris["target"]))

for features,label in ds2.take(3):
    print(features,label)
```

## 从Python generator构建数据管道

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 定义一个从文件中读取图片的generator
image_generator = ImageDataGenerator(rescale=1.0/255).flow_from_directory(
                    "data/cifar2/test/",
                    target_size=(32, 32),
                    batch_size=20,
                    class_mode='binary')

classdict = image_generator.class_indices
print(classdict)

def generator():
    for features,label in image_generator:
        yield (features,label)

ds3 = tf.data.Dataset.from_generator(generator,output_types=(tf.float32,tf.int32))
```

## 从csv文件构建管道

```python
ds4 = tf.data.experimental.make_csv_dataset(
      file_pattern = ["data/titanic/train.csv","data/titanic/test.csv"],
      batch_size=3, 
      label_name="Survived",
      na_value="",
      num_epochs=1,
      ignore_errors=True)

for data,label in ds4.take(2):
    print(data,label)
```

## 从文本文件构建管道

```python
ds5 = tf.data.TextLineDataset(
    filenames = ["data/titanic/train.csv","data/titanic/test.csv"]
    ).skip(1) #略去第一行header

for line in ds5.take(5):
    print(line)
```

## 从文件路径构建数据管道

```python
ds6 = tf.data.Dataset.list_files("data/cifar2/train/*/*.jpg")
from matplotlib import pyplot as plt 
def load_image(img_path,size = (32,32)):
    label = 1 if tf.strings.regex_full_match(img_path,".*/automobile/.*") else 0
    img = tf.io.read_file(img_path)
    img = tf.image.decode_jpeg(img) #注意此处为jpeg格式
    img = tf.image.resize(img,size)
    return(img,label)

%matplotlib inline
%config InlineBackend.figure_format = 'svg'
for i,(img,label) in enumerate(ds6.map(load_image).take(2)):
    plt.figure(i)
    plt.imshow((img/255.0).numpy())
    plt.title("label = %d"%label)
    plt.xticks([])
    plt.yticks([])
```

## 从tfrecords构建数据管道

```python
import os
import numpy as np

# inpath：原始数据路径 outpath:TFRecord文件输出路径
def create_tfrecords(inpath,outpath): 
    writer = tf.io.TFRecordWriter(outpath)
    dirs = os.listdir(inpath)
    for index, name in enumerate(dirs):
        class_path = inpath +"/"+ name+"/"
        for img_name in os.listdir(class_path):
            img_path = class_path + img_name
            img = tf.io.read_file(img_path)
            example = tf.train.Example(
               features=tf.train.Features(feature={
                    'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[index])),
                    'img_raw': tf.train.Feature(bytes_list=tf.train.BytesList(value=[img.numpy()]))
               }))
            writer.write(example.SerializeToString())
    writer.close()

def parse_example(proto):
    description ={ 'img_raw' : tf.io.FixedLenFeature([], tf.string),
                   'label': tf.io.FixedLenFeature([], tf.int64)} 
    example = tf.io.parse_single_example(proto, description)
    img = tf.image.decode_jpeg(example["img_raw"])   #注意此处为jpeg格式
    img = tf.image.resize(img, (32,32))
    label = example["label"]
    return(img,label)

ds7 = tf.data.TFRecordDataset("data/cifar2_test.tfrecords").map(parse_example).shuffle(3000)
```

## Dataset基本操作

Dataset数据结构应用非常灵活，因为它本质上是一个Sequece序列，其每个元素可以是各种类型，例如可以是张量，列表，字典，也可以是Dataset。
1. Dataset包含了非常丰富的数据转换功能。
2. map: 将转换函数映射到数据集每一个元素。
3. flat_map: 将转换函数映射到数据集的每一个元素，并将嵌套的Dataset压平。
4. interleave: 效果类似flat_map,但可以将不同来源的数据夹在一起。
5. filter: 过滤掉某些元素。
6. zip: 将两个长度相同的Dataset横向铰合。
7. concatenate: 将两个Dataset纵向连接。
8. reduce: 执行归并操作。
9. batch : 构建批次，每次放一个批次。比原始数据增加一个维度。 其逆操作为unbatch。
10. padded_batch: 构建批次，类似batch, 但可以填充到相同的形状。
11. window :构建滑动窗口，返回Dataset of Dataset.
12. shuffle: 数据顺序洗牌。
13. repeat: 重复数据若干次，不带参数时，重复无数次。
14. shard: 采样，从某个位置开始隔固定距离采样一个元素。
15. take: 采样，从开始位置取前几个元素。

```python
# map
ds = tf.data.Dataset.from_tensor_slices(["hello world","hello China","hello Beijing"])
ds_map = ds.map(lambda x:tf.strings.split(x," "))

# flap_map
ds = tf.data.Dataset.from_tensor_slices(["hello world","hello China","hello Beijing"])
ds_flatmap = ds.flat_map(lambda x:tf.data.Dataset.from_tensor_slices(tf.strings.split(x," ")))

# interleave
ds = tf.data.Dataset.from_tensor_slices(["hello world","hello China","hello Beijing"])
ds_interleave = ds.interleave(lambda x:tf.data.Dataset.from_tensor_slices(tf.strings.split(x," ")), cycle_length = 1, block_length = 1)  # == flat_map

# filter
ds = tf.data.Dataset.from_tensor_slices(["hello world","hello China","hello Beijing"])
#找出含有字母a或B的元素
ds_filter = ds.filter(lambda x: tf.strings.regex_full_match(x, ".*[a|B].*"))

# zip
ds1 = tf.data.Dataset.range(0,3)
ds2 = tf.data.Dataset.range(3,6)
ds3 = tf.data.Dataset.range(6,9)
ds_zip = tf.data.Dataset.zip((ds1,ds2,ds3)) 
for x,y,z in ds_zip:
    print(x.numpy(),y.numpy(),z.numpy())

# 0 3 6
# 1 4 7
# 2 5 8

# concat
ds1 = tf.data.Dataset.range(0,3)
ds2 = tf.data.Dataset.range(3,6)
ds_concat = tf.data.Dataset.concatenate(ds1,ds2)
for x in ds_concat:
    print(x)

# tf.Tensor(0, shape=(), dtype=int64)
# tf.Tensor(1, shape=(), dtype=int64)
# tf.Tensor(2, shape=(), dtype=int64)
# tf.Tensor(3, shape=(), dtype=int64)
# tf.Tensor(4, shape=(), dtype=int64)
# tf.Tensor(5, shape=(), dtype=int64)

# reduce
ds = tf.data.Dataset.from_tensor_slices([1,2,3,4,5.0])
result = ds.reduce(0.0,lambda x,y:tf.add(x,y))

# batch
ds = tf.data.Dataset.range(12)
ds_batch = ds.batch(4)
for x in ds_batch:
    print(x)

# tf.Tensor([0 1 2 3], shape=(4,), dtype=int64)
# tf.Tensor([4 5 6 7], shape=(4,), dtype=int64)
# tf.Tensor([ 8  9 10 11], shape=(4,), dtype=int64)

# padded_batch:构建批次，类似batch, 但可以填充到相同的形状。

elements = [[1, 2],[3, 4, 5],[6, 7],[8]]
ds = tf.data.Dataset.from_generator(lambda: iter(elements), tf.int32)

ds_padded_batch = ds.padded_batch(2,padded_shapes = [4,])
for x in ds_padded_batch:
    print(x) 

# tf.Tensor(
# [[1 2 0 0]
#  [3 4 5 0]], shape=(2, 4), dtype=int32)
# tf.Tensor(
# [[6 7 0 0]
#  [8 0 0 0]], shape=(2, 4), dtype=int32)

# window:构建滑动窗口，返回Dataset of Dataset.
ds = tf.data.Dataset.range(12)
# window返回的是Dataset of Dataset,可以用flat_map压平
# flat_map之后是一维，batch一下分批
ds_window = ds.window(3, shift=1).flat_map(lambda x: x.batch(3,drop_remainder=True))
for x in ds_window:
    print(x)

# shuffle: 数据顺序洗牌
ds = tf.data.Dataset.range(12)
ds_shuffle = ds.shuffle(buffer_size = 5)

# repeat: 重复数据若干次，不带参数时，重复无数次。
ds = tf.data.Dataset.range(3)
ds_repeat = ds.repeat(3)

# shard: 采样，从某个位置开始隔固定距离采样一个元素。
ds = tf.data.Dataset.range(12)
ds_shard = ds.shard(3,index = 1)

# take:采样，从开始位置取前几个元素
ds = tf.data.Dataset.range(12)
ds_take = ds.take(3)

```

## 提升管道性能

训练深度学习模型常常会非常耗时。

模型训练的耗时主要来自于两个部分，一部分来自数据准备，另一部分来自参数迭代。

参数迭代过程的耗时通常依赖于GPU来提升。

而数据准备过程的耗时则可以通过构建高效的数据管道进行提升。

以下是一些构建高效数据管道的建议:
1. 使用 prefetch 方法让数据准备和参数迭代两个过程相互并行。
2. 使用 interleave 方法可以让数据读取过程多进程执行,并将不同来源数据夹在一起。
3. 使用 map 时设置num_parallel_calls 让数据转换过程多进行执行。
4. 使用 cache 方法让数据在第一个epoch后缓存到内存中，仅限于数据集不大情形。
5. 使用 map转换时，先batch, 然后采用向量化的转换方法对每个batch进行转换。
